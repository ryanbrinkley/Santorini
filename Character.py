class Character:

    def __init__(self, x, y):
        self.position = (x, y)
        self.isTurn = False
        self.buildRange = 1

    def move(self, x, y):
        self.position = (x, y)

    def build(self, board, x, y):
        board.build(x, y)

    def check_available_move(self, board):
        x = self.position[0]
        y = self.position[1]
        for i in range(3):
            for j in range(3):
                space = board.spaces[i][j]


class Apollo(Character):

    def __init__(self, x, y):
        super(x, y)
        self.description = "You may move into an opponent's square and trade places" \
                           " with him"


class Artemis(Character):

    def __init__(self, x, y):
        super(x, y)
        self.description = "You may move into an opponent's square and trade places" \
                           " with him"
