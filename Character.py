class Character:

    def __init__(self, x, y):
        self.position = (x, y)
        self.isTurn = False
        self.buildRange = 1
        self.height = 0

    def move(self, x, y):
        self.position = (x, y)
        # make board spaces unavailable / check build availables

    def build(self, board, x, y):
        board.build(x, y)
        # make board spaces unavailable

    def check_available_moves(self, board):
        x = self.position[0]
        y = self.position[1]
        board.make_available(x - 1, y - 1)
        board.make_available(x, y - 1)
        board.make_available(x + 1, y - 1)
        board.make_available(x - 1, y)
        board.make_available(x + 1, y)
        board.make_available(x - 1, y + 1)
        board.make_available(x, y + 1)
        board.make_available(x + 1, y + 1)

    def check_available_builds(self, board):
        x = self.position[0]
        y = self.position[1]
        board.make_available(x - 1, y - 1)
        board.make_available(x, y - 1)
        board.make_available(x + 1, y - 1)
        board.make_available(x - 1, y)
        board.make_available(x + 1, y)
        board.make_available(x - 1, y + 1)
        board.make_available(x, y + 1)
        board.make_available(x + 1, y + 1)

class Apollo(Character):

    def __init__(self, x, y):
        super(x, y)
        self.description = "You may move into an opponent's square and trade places" \
                           " with him"


class Artemis(Character):

    def __init__(self, x, y):
        super(x, y)
        self.description = "Queer as a Steer"
