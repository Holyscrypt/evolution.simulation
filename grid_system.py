import random


def generate_grid(size):
    """
    returns the grid with a given attribute to it.
    it is returned as a dictionary with the keys
    being coordinates and the values being the
    attributes
    """
    terrain_types = ["tree", "plain", "food"]
    grid = {}
    for x in range(size):
        for y in range(size):
            grid[(x, y)] = random.choice(terrain_types)

    return grid
