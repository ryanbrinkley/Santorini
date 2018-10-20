import Character
import random

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
        # char1, char2 = select_random_characters()
        player1 = getattr(Character, "Apollo") #getattr(Character, char1)
        player2 = getattr(Character, "Artemis") #getattr(Character, char2)
        self.player1 = player1()
        self.player2 = player2()
        self.activePlayer = 1 # just an int 1 or 2
        self.currPlayer = self.player1
        self.stage = "PLACE" # "PLACE", "SELECT", "MOVE", "BUILD"
        self.gameOver = False
        self.winner = None

    def get_player_positions(self):
        return self.player1.get_positions(), self.player2.get_positions()

    def set_currPlayer(self):
        self.currPlayer = self.player1 if self.activePlayer == 1 else self.player2

    def valid_spaces(self, spaceClicked):
        currSpace = self.spaces[spaceClicked]
        if self.stage == "PLACE":
            return self.currPlayer.valid_place(self.spaces)
        elif self.stage == "SELECT":
            return self.currPlayer.valid_select()
        elif self.stage == "MOVE":
            return self.currPlayer.valid_move(currSpace, self.spaces)
        elif self.stage == "BUILD":
            return self.currPlayer.valid_build(currSpace, self.spaces)
        
    def place_workers(self, spaceClicked):
        gender = "M" if self.currPlayer.workersLeftToPlace % 2 == 0 else "F"
        # todo: add support for non-binary gender

        worker = Character.Worker(self.currPlayer, gender)
        self.currPlayer.workers.append(worker)
        self.spaces[spaceClicked].place(worker)

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

    # todo:
    # make character build function
    def build(self, spaceClicked):
        self.spaces[spaceClicked].build()
        self.activePlayer = (self.activePlayer % 2) + 1
        self.set_currPlayer()
        self.stage = "SELECT"

    # todo:
    def check_game_over(self):
        if False:
            self.gameOver = True


class Space:
    def __init__(self, pos):
        # 0 = no building; 1,2,3 = size 1,2,3 building; 4 = domed building
        self.pos = pos
        self.height = 0
        self.inhabited = False
        self.inhabitant = None

    def build(self):
        if self.height < 4:
            self.height += 1

    def place(self, worker):
        self.inhabited = True
        self.inhabitant = worker
        worker.space = self
        worker.pos = self.pos

    def free(self):
        self.inhabited = False
        self.inhabitant = None
