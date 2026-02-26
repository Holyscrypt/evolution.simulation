import random


def random_cell(grid):
    """
    returns a random cell from the given grid
    returns it as a tuple
    """
    return random.choice(list(grid.keys()))


class Human:
    def __init__(self, grid):
        self.grid = grid
        self.position = random_cell(grid)
        self.energy = None

    def move(self):
        """
        This method makes the humans to move
        """
        x = self.position[0]
        y = self.position[1]
        movements = {"Up": (x, y + 1), "Down": (x, y - 1),
                     "Left": (x - 1, y), "Right": (x + 1, y)}
        new_position = random.choice(list(movements.values()))
        if new_position in self.grid:
            self.position = new_position
        else:
            pass
