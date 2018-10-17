class Board:

    def __init__(self):
        self.spaces = [[Space() for i in range(5)] for i in range(5)]

    def build(self, x, y):
        self.spaces[x][y].increment_size()

    # def check_available_move(self):


class Space:

    def __init__(self):
        # 0 = no building
        # 1,2,3 = size 1,2,3 building
        # 4 = domed building
        self.buildingSize = 0
        self.maxBuildingSize = 4
        self.availability = False

    def increment_size(self):
        if self.buildingSize < self.maxBuildingSize:
            self.buildingSize += 1
