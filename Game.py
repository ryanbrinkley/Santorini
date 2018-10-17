from Character import Character
from Board import Board

characterList = ["Apollo", "Artemis", "Hecate", "Zeus"]

def initialize():
    print(characterList)
    # player1 = Character(int(input()), int(input()))
    # player2 = Character(int(input()), int(input()))
    # choose chars / random chars
    player1.isTurn = True

player1 = Character(1, 1)
player2 = Character(0, 0)
board = Board()

gameOver = False

def check_game_over():
    # check win/loss conditions
    global gameOver
    if not gameOver:
        gameOver = True

initialize()

# Game loop
while not gameOver:
    if player1.isTurn:
        print("Player 1's Turn")
        activePlayer = player1
    else:
        print("Player 2's Turn")
        activePlayer = player2

    #Current Positions
    print("Player 1" + str(player1.position) + "; Player 2" + str(player2.position))

    activePlayer.check_available_moves(board)
    board.get_available_spaces()
    # activePlayer.getMoveInput()

    # activePlayer.check_available_builds(board)
    # board.get_available_builds
    # activePlayer.getBuildInput()
    activePlayer.build(board, 0, 0)

    #print board
    for i in range(5):
        for j in range(5):
            print(board.spaces[i][j].buildingSize, end=" ")
        print()

    check_game_over()
