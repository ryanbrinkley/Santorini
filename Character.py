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
        self.workersLeftToPlace = self.numWorkers
        self.selectedWorker = None  
    
    def get_positions(self):
        posList = []
        for i in range (self.numWorkers):
            posList.append(self.workers[i].pos)
        return posList

class Worker:
    def __init__(self, player, gender, space):
        self.player = player
        self.space = space
        self.pos = space.pos
        self.gender = gender
        self.validMoves = None

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
