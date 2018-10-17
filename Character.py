characterList = [
    "Apollo", 
    "Artemis", 
    "Hecate", 
    "Zeus"
]

class Character:
    def __init__(self):
        self.workers = []
        self.numWorkers = 2
        self.selectedWorker = None  
        self.isTurn = False

class Worker:
    def __init__(self, id, space):
        self.space = space
        self.pos = space.pos
        self.id = id

    def move(self, pos):
        self.space = pos
        # make board spaces unavailable / check build availables

class Apollo(Character):
    def __init__(self):
        super(Apollo, self).__init__()
        self.name = "Apollo"
        self.description = "You may move into an opponent's square and trade places" \
                           " with him"

class Artemis(Character):
    def __init__(self):
        super(Artemis, self).__init__()
        self.name = "Artemis"
        self.description = "Queer as a Steer"
