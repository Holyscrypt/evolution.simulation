import random
import grid_system
def random_cell(grid):
    return random.choice(list(grid.keys()))

class Human:
    def __init__(self, grid):
        self.grid = grid
        self.position = random_cell(grid)
        self.energy = None

    def move(self):
        x = self.position[0]
        y = self.position[1]
        movements = {"Up": (x, y + 1), "Down": (x, y - 1),
                     "Left": (x - 1, y), "Right": (x + 1, y)}




