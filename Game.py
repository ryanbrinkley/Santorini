import Character
import random

def coord_to_pos(x, y):
    return int(y * 5 + x)

def pos_to_coord(pos):
    x = int(pos % 5)
    y = int((pos - x) / 5)
    return x, y

def select_random_characters():
    chars = Character.characterList
    player1 = random.choice(chars)
    player2 = random.choice(chars)
    while player1 == player2:
        player2 = random.choice(chars)
    return player1, player2

class Game:
    def __init__(self):
        self.spaces = [Space(i) for i in range(25)]
        char1, char2 = select_random_characters()
        player1 = getattr(Character, char1)
        player2 = getattr(Character, char2)
        self.player1 = player1()
        self.player2 = player2()
        self.activePlayer = 1 # just an int 1 or 2
        self.currPlayer = self.player1
        self.stage = "PLACE" # "PLACE", "SELECT", "MOVE", "BUILD"
        self.gameOver = False

    def get_player_positions(self):
        return self.player1.get_positions(), self.player2.get_positions()

    def get_active_player(self):
        return self.activePlayer

    def get_stage(self):
        return self.stage

    def set_currPlayer(self):
        self.currPlayer = self.player1 if self.activePlayer == 1 else self.player2

    def valid_spaces(self, spaceClicked):
        # if currPlayer.has_valid_spaces_override:
        # currPlayer.valid_spaces(spaceClicked)
        # else:
        #                               or
        # return currPlayer.valid_spaces(spaceClicked)

        x, y = pos_to_coord(spaceClicked)
        currSpace = self.spaces[spaceClicked]
        validList = set() #return all valid spaces in this list
        validRange = set()

        # edge checking
        if not x == 0:
            validRange.add(coord_to_pos(x - 1, y))
        if not y == 0:
            validRange.add(coord_to_pos(x, y - 1))
        if not x == 4:
            validRange.add(coord_to_pos(x + 1, y))
        if not y == 4:
            validRange.add(coord_to_pos(x, y + 1))
        if not x == 0 and not y == 0:
            validRange.add(coord_to_pos(x - 1, y - 1))
        if not x == 4 and not y == 0:
            validRange.add(coord_to_pos(x + 1, y - 1))
        if not x == 0 and not y == 4:
            validRange.add(coord_to_pos(x - 1, y + 1))
        if not x == 4 and not y == 4:
            validRange.add(coord_to_pos(x + 1, y + 1))

        if self.stage == "PLACE":
            for i in range(5):
                for j in range(5):
                    space = self.spaces[coord_to_pos(i, j)]
                    if (space.inhabited == False):
                        validList.add(space.pos)
        elif self.stage == "SELECT":
            for i in range(self.currPlayer.numWorkers):
                validList.add(self.currPlayer.workers[i].pos)
        elif self.stage == "MOVE":
            for i in range(5):
                for j in range(5):
                    space = self.spaces[coord_to_pos(i, j)]
                    # space is out of reach / space is too tall / space is inhabited
                    if space.pos in validRange and space.height - currSpace.height < 2 and not space.height == 4 and space.inhabited == False:
                        validList.add(space.pos)
        elif self.stage == "BUILD":
            for i in range(5):
                for j in range(5):
                    space = self.spaces[coord_to_pos(i, j)]
                    # space is out of reach / space is too tall / space is inhabited
                    if space.pos in validRange and not space.height == 4 and space.inhabited == False:
                        validList.add(space.pos)
        return validList
        

    def place_workers(self, spaceClicked):
        gender = "G"
        if self.currPlayer.workersLeftToPlace % 2 == 0:
            gender = "B"

        worker = Character.Worker(self.activePlayer, gender, self.spaces[spaceClicked])
        self.currPlayer.workers.append(worker)
        self.spaces[spaceClicked].inhabited = True
        self.spaces[spaceClicked].inhabitant = worker

        self.currPlayer.workersLeftToPlace -= 1
        if self.currPlayer.workersLeftToPlace == 0:
            if self.activePlayer == 2:
                self.stage = "SELECT"
            self.activePlayer = (self.activePlayer % 2) + 1
            self.set_currPlayer()

    def select_worker(self, spaceClicked):
        self.currPlayer.selectedWorker = self.spaces[spaceClicked].inhabitant
        self.stage = "MOVE"

    def move_worker(self, spaceClicked):
        #worker move function returns a stage
        self.stage = self.currPlayer.move(self.spaces[spaceClicked])

    def build(self, spaceClicked):
        self.spaces[spaceClicked].build()
        self.activePlayer = (self.activePlayer % 2) + 1
        self.set_currPlayer()
        self.stage = "SELECT"

    def check_game_over(self):
        #ToDo
        if False:
            self.gameOver = True

#    def game_loop(self):
#        print board
#        for i in range(5):
#            for j in range(5):
#                print(self.spaces[i + (j * 5)].height, end=" ")
#            print()

class Space:
    def __init__(self, pos):
        # 0 = no building
        # 1,2,3 = size 1,2,3 building
        # 4 = domed building
        self.pos = pos
        self.height = 0
        self.inhabited = False
        self.inhabitant = None

    def build(self):
        if self.height < 4:
            self.height += 1

    def place(self, worker):
        if self.inhabited == False:
            self.inhabited = True
            self.inhabitant = worker
            worker.space = self
            worker.pos = self.pos

    def free(self):
        self.inhabited = False
        self.inhabitant = None

# game = Game()
# gui = uncle_gui.GUI()
# print(Character.characterList)
# choose chars / random chars
# game.place_workers(10)
# game.game_loop()
