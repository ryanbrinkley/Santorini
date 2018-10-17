import Character
#import uncle_gui as gui
#from enum import Enum
#from uncle_gui import GUI

class Game:
    def __init__(self):
        self.spaces = [Space(i) for i in range(25)]
        self.player1 = Character.Apollo()
        self.player2 = Character.Artemis()
        self.stage = "PLACE" # Enum("PLACE", "SELECT", "MOVE", "BUILD")
        self.player1.isTurn = True
        self.gameOver = False
        #gui = GUI()

    def check_game_over(self):
        # check win/loss conditions
        if not self.gameOver:
            self.gameOver = True

    def check_valid_spaces(self):
        if self.stage == "PLACE":
            checkvalid = True
        if self.stage == "SELECT":
            checkvalid = True
        if self.stage == "MOVE":
            checkvalid = True
        if self.stage == "BUILD":
            checkvalid = True
        """x = self.position[0]
        y = self.position[1]
        board.make_available(x - 1, y - 1)
        board.make_available(x, y - 1)
        board.make_available(x + 1, y - 1)
        board.make_available(x - 1, y)
        board.make_available(x + 1, y)
        board.make_available(x - 1, y + 1)
        board.make_available(x, y + 1)
        board.make_available(x + 1, y + 1)"""

    def place_workers(self):
        for i in range(self.player1.numWorkers):
            if i % 2 == 0:
                id = "B"
            else:
                id = "G"
            self.player1.workers.append(Character.Worker(id, i))

        for i in range(self.player2.numWorkers):
            if i % 2 == 0:
                id = "B"
            else:
                id = "G"
            self.player1.workers.append(Character.Worker(id, 10+i))
        

    def game_loop(self):
        while not self.gameOver:
            if self.player1.isTurn:
                print("Player 1's Turn")
                activePlayer = self.player1
            else:
                print("Player 2's Turn")
                activePlayer = self.player2
            
            # Select Worker

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
            #print("Player 1 Pos: " + str(player1.firstPosition) + str(player1.secondPosition))
            #print("Player 2 Pos: " + str(player2.firstPosition) + str(player2.secondPosition))

            #print board
            for i in range(5):
                for j in range(5):
                    print(self.spaces[i + (j * 5)].buildingSize, end=" ")
                print()

            self.player1.isTurn = not self.player1.isTurn
            self.player2.isTurn = not self.player2.isTurn

            self.check_game_over()

class Space:
    def __init__(self, pos):
        # 0 = no building
        # 1,2,3 = size 1,2,3 building
        # 4 = domed building
        self.pos = pos
        self.buildingSize = 0
        self.inhabited = False
        self.inhabitant = None

    def build(self):
        if self.buildingSize < 4:
            self.buildingSize += 1
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
game.game_loop()
