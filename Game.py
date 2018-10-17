import Character
import uncle_gui as gui
#from enum import Enum

# p locations
# curr player
# char location, currplayer,
# returns if move or build
#       every valid space, 

def coord_to_pos(x, y):
    return int(x+5*y)

def pos_to_coord(a):
    x = int(a%5)
    y = int((a-x)/5)
    return x, y

class Game:
    def __init__(self):
        self.spaces = [Space(i) for i in range(25)]
        self.player1 = Character.Apollo()
        self.player2 = Character.Artemis()
        self.activePlayer = 1
        #self.stage = "PLACE" # Enum("PLACE", "SELECT", "MOVE", "BUILD")
        self.stage = "MOVE"
        self.gameOver = False

    def check_game_over(self):
        # check win/loss conditions
        if not self.gameOver:
            self.gameOver = True

    def valid_spaces(self, spaceClicked):
        x, y = pos_to_coord(spaceClicked)
        currSpace = self.spaces[spaceClicked]
        validList = set() #return all invalid spaces in this list
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
                    if(space.inhabited == False):
                        validList.add(space.pos)
        elif self.stage == "SELECT":
            pass
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
        

    def place_workers(self):
        for i in range(self.player1.numWorkers):
            if i % 2 == 0:
                id = "B"
            else:
                id = "G"
            self.player1.workers.append(Character.Worker(id, self.spaces[i]))
            self.spaces[i].inhabited = True
            self.spaces[i].inhabitant = self.player1.workers[i]

        for i in range(self.player2.numWorkers):
            if i % 2 == 0:
                id = "B"
            else:
                id = "G"
            self.player2.workers.append(Character.Worker(id, self.spaces[12+i]))
            self.spaces[12+i].inhabited = True
            self.spaces[12+i].inhabitant = self.player2.workers[i]
    
    def get_player_positions(self):
        return self.player1.get_positions(), self.player2.get_positions()

    def get_active_player(self):
        return self.activePlayer

    def get_stage(self):
        return self.stage

    def game_loop(self):
        while not self.gameOver:
            if self.activePlayer == 1:
                print("Player 1's Turn")
                # currPlayer = player1
            elif self.activePlayer == 2:
                print("Player 2's Turn")
                # currPlayer = player2
            
            # Select Worker
            print(self.valid_spaces(10)) #need 4, 9, 14
            # Move
            # activePlayer.check_available_moves(1, board)
            # board.get_available_spaces()
            # activePlayer.getMoveInput()

            # Build
            # activePlayer.check_available_builds(board)
            # board.get_available_builds
            # activePlayer.getBuildInput()
            self.spaces[0].build()

            # Current Positions (5 * y + x for 1d?)
            self.get_player_positions()

            #print board
            for i in range(5):
                for j in range(5):
                    print(self.spaces[i + (j * 5)].height, end=" ")
                print()

            print(self.activePlayer)
            self.activePlayer = (self.activePlayer % 2) + 1
            print(self.activePlayer)

            self.check_game_over()

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
        else:
            print("Attempted to build on dome")

    def place(self, worker):
        if self.inhabited == False:
            self.inhabited = True
            self.inhabitant = worker
            worker.space = self
            worker.pos = self.pos
        else:
            print("Attempted to place on inhabited space")

    def free(self):
        self.inhabited = False
        self.inhabitant = None


game = Game()
print(Character.characterList)
# choose chars / random chars
game.place_workers()
game.game_loop()
