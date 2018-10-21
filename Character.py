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

def coord_to_pos(x, y):
    return int(y * 5 + x)

def pos_to_coord(pos):
    x = int(pos % 5)
    y = int((pos - x) / 5)
    return x, y

class Character:
    def __init__(self):
        self.workers = []
        self.numWorkers = 2
        self.workersLeftToPlace = self.numWorkers
        self.selectedWorker = None  
    
    # Return positions of all of this character's workers on board
    def get_positions(self):
        posList = []
        for i in range (self.numWorkers):
            posList.append(self.workers[i].pos)
        return posList

    # Override in specific characters for different move function
    def move(self, space):
        self.selectedWorker.space.free()
        space.place(self.selectedWorker)
        self.selectedWorker = None
        return "BUILD"

    def valid_place(self, spaces):
        validList = set()
        for space in spaces:
            if space.inhabited == False:
                validList.add(space.pos)
        return validList

    def valid_select(self):
        validList = set()
        for i in range(self.numWorkers):
            validList.add(self.workers[i].pos)
        return validList

    # space is in reach / space is not too tall or domed / space is not inhabited
    def valid_move(self, currSpace, spaces):
        validList = set()
        validRange = self.valid_edges(currSpace.pos)
        for space in spaces:
            if (space.pos in validRange and space.height - currSpace.height < 2 and 
                    space.height != 4 and space.inhabited == False):
                validList.add(space.pos)
        return validList

    # space is in reach / space is not domed / space is not inhabited
    def valid_build(self, currSpace, spaces):
        validList = set()
        validRange = self.valid_edges(currSpace.pos)
        for space in spaces:
            if space.pos in validRange and not space.height == 4 and space.inhabited == False:
                validList.add(space.pos)
        return validList

    def valid_edges(self, pos):
        validRange = set()
        x, y = pos_to_coord(pos)

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

        return validRange

class Worker:
    def __init__(self, character, gender):
        self.character = character
        self.space = None
        self.pos = None
        self.gender = gender

class Apollo(Character):
    def __init__(self):
        super(Apollo, self).__init__()
        self.name = "Apollo"
        self.difficulty = "Simple"
        self.description = ("Your Move : Your worker may move into an opponent worker's space by "
                            "forcing their worker to the space you just vacated.")
    
    # add opponent inhabited spaces from valid list in move
    def valid_move(self, currSpace, spaces):
        validList = set()
        validRange = self.valid_edges(currSpace.pos)
        for space in spaces:
            if (space.pos in validRange and space.height - currSpace.height < 2 and 
                    space.height != 4 and space.inhabited == False):
                validList.add(space.pos)
            if (space.pos in validRange and space.height - currSpace.height < 2 and 
                    space.height != 4 and space.inhabited == True):
                if space.inhabitant.character != self:
                    validList.add(space.pos)
        return validList

    # switch places with opponent workers
    def move(self, space):
        if space.inhabited == True:
            self.selectedWorker.space.place(space.inhabitant)
        else:
            self.selectedWorker.space.free()

        space.place(self.selectedWorker)
        return "BUILD"


class Artemis(Character):
    def __init__(self):
        super(Artemis, self).__init__()
        self.name = "Artemis"
        self.difficulty = "Simple"
        self.description = ("Your Move: Your worker may move one additional time, but not back to "
                            "its initial space.")
        self.numberOfMoves = 0
        self.prevTile = None
        self.newTile = None

    def valid_move(self, currSpace, spaces):
        if self.numberOfMoves == 0:
            self.prevTile = self.selectedWorker.pos
        else:
            self.newTile = self.selectedWorker.pos

        validList = set()
        validRange = self.valid_edges(currSpace.pos)
        for space in spaces:
            if (space.pos in validRange and space.height - currSpace.height < 2 and 
                    space.height != 4 and space.inhabited == False):
                validList.add(space.pos)
        
        if self.prevTile != None and self.prevTile in validList:
            validList.remove(self.prevTile)
            self.prevTile = None

        if self.newTile != None:
            validList.add(self.newTile)
            self.newTile = None

        return validList
        
    def move(self, space):
        self.selectedWorker.space.free()
        space.place(self.selectedWorker)

        self.numberOfMoves += 1

        if self.numberOfMoves == 2:
            self.numberOfMoves = 0
            self.selectedWorker = None
            return "BUILD"
        else:
            return "MOVE"


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
