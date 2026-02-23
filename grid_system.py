import random
def generate_grid(size):
    grid_attribute = ["tree", "plain", "food"]
    grid = {}
    counts = {"tree": 0, "plain": 0, "food": 0}
    for x in range(size + 1):
        for y in range(size + 1):
            point = (x, y)
            tile = random.choice(grid_attribute, weights=[0.3,0.4,0.3])
            grid[point] = tile
            counts[tile] += 1

    return grid,counts

