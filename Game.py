from Character import Character
from Board import Board

gameOver = False

# player1 = Character(int(input()), int(input()))
# player2 = Character(int(input()), int(input()))
player1 = Character(0, 0)
player2 = Character(0, 0)
board = Board()


def check_game_over():
    global gameOver
    if not gameOver:
        gameOver = True


player1.isTurn = True

while not gameOver:
    if player1.isTurn:
        print("Player 1's Turn")
    else:
        print("Player 2's Turn")

    # Check available moves
    # Move input

    # Check available builds
    # Build input

    print("Player 1" + str(player1.position))
    print("Player 2" + str(player2.position))

    player1.build(board, 0, 0)

    for i in range(5):
        for j in range(5):
            print(board.spaces[i][j].buildingSize, end=" ")
        print()

    check_game_over()

