import random
import grid_system
def random_cell(grid):
    return random.choice(list(grid.keys()))

class Human:
    def __init__(self, grid):
        self.grid = grid
        self.position = random_cell(grid)
        self.energy = None


