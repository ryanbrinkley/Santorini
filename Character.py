characterList = [
    "Apollo", 
    "Artemis", 
    "Athena", 
    "Atlas",
    "Demeter",
    "Hephaestus",
    "Hermes",
    "Minotaur",
    "Pan",
    "Prometheus"
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

    #Override in specific characters for different move function
    def move(self, space):
        self.selectedWorker.space.free()
        space.place(self.selectedWorker)
        self.selectedWorker = None
        return "BUILD"

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
        self.difficulty = "Simple"
        self.description = ("Your Move : Your worker may move into an opponent worker's space by "
                            "forcing their worker to the space you just vacated.")
    
    def ability(self):
        pass
        # valid space on opponent chars
        # if space contains opponent
        # opponent position = self's old position
        # make valid_spaces function a character function with possible override?
        # or just receive validList and alter it


# Ability time = Game stage?


class Artemis(Character):
    def __init__(self):
        super(Artemis, self).__init__()
        self.name = "Artemis"
        self.difficulty = "Simple"
        self.description = ("Your Move: Your worker may move one additional time, but not back to "
                            "its initial space.")

    def ability(self):
        pass
        # after move, allow move again
        # allow move to first move spot (like only moved once)
        # remove old position from valid list

    def move(self, space):
        self.selectedWorker.space.free()
        space.place(self.selectedWorker)
        self.selectedWorker = None
        #return "SELECT"
        return "BUILD"
    
        

class Athena(Character):
    def __init__(self):
        super(Athena, self).__init__()
        self.name = "Athena"
        self.difficulty = "Simple"
        self.description = ("Opponent's Turn: If one of your workers moved up on your last turn, "
                            "opponent workers cannot move up this turn.")

        # opponent cant go up = True if height > prev height else False

class Atlas(Character):
    def __init__(self):
        super(Atlas, self).__init__()
        self.name = "Atlas"
        self.difficulty = "Simple"
        self.description = "Your Build: Your worker may build a dome at any level."

        # need to make dome attribute in space
        # could temporarily set height to 4 on a build
        # needs option to differentiate between dome build and reg build

class Demeter(Character):
    def __init__(self):
        super(Demeter, self).__init__()
        self.name = "Demeter"
        self.difficulty = "Simple"
        self.description = ("Your Build: Your worker may build one additional time, but not on the "
                            " same space.")

        # after build, allow build again
        # remove first build spot from valid list

class Hephaestus(Character):
    def __init__(self):
        super(Hephaestus, self).__init__()
        self.name = "Hephaestus"
        self.difficulty = "Simple"
        self.description = ("Your Build: Your Worker may build one additional block (not dome) " 
                            "on top of your first block.")
        # after build, allow build again
        # but second's valid list is only on the first spot
        # needs option to not build twice
        # no build if height will be dome

class Hermes(Character):
    def __init__(self):
        super(Hermes, self).__init__()
        self.name = "Hermes"
        self.difficulty = "Simple"
        self.description = ("Your Turn: If your Workers do not move up or down, they may "
                            "each move any number of times (even zero), and then either builds")

        # while currheight == height
        # possibility to move again or not at all
        # both can build (still in if state)

class Minotaur(Character):
    def __init__(self):
        super(Minotaur, self).__init__()
        self.name = "Minotaur"
        self.difficulty = "Simple"
        self.description = ("Your Move: Your Worker may move into an opponent Worker’s space, "
                            "if their Worker can be forced one space straight backwards to an "
                            "unoccupied space at any level.")

class Pan(Character):
    def __init__(self):
        super(Pan, self).__init__()
        self.name = "Pan"
        self.difficulty = "Simple"
        self.description = ("Win Condition: You also win if your Worker moves down two or "
                            "more levels.")

class Prometheus(Character):
    def __init__(self):
        super(Prometheus, self).__init__()
        self.name = "Prometheus"
        self.difficulty = "Simple"
        self.description = ("Your Turn: If your Worker does not move up, it may build both "
                            "before and after moving.")
