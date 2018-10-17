class Board:

    def __init__(self):
        self.spaces = [[Space(i, j) for i in range(5)] for j in range(5)]

    def build(self, x, y):
        self.spaces[x][y].increment_size()

    def make_available(self, x, y):
        if x >= 0 and x <= 5 and y >= 0 and y <= 5:
            # Check for building level
            # Check for another character
            self.spaces[x][y].availability = True

    def get_available_spaces(self):
        print("Available Spaces:")
        for i in range(5):
            for j in range(5):
                if self.spaces[i][j].availability == True:
                    print(self.spaces[i][j].location, end=" ")
        print()


class Space:

    def __init__(self, x, y):
        # 0 = no building
        # 1,2,3 = size 1,2,3 building
        # 4 = domed building
        self.location = (x, y)
        self.buildingSize = 0
        self.maxBuildingSize = 4
        self.availability = False

    def increment_size(self):
        if self.buildingSize < self.maxBuildingSize:
            self.buildingSize += 1
