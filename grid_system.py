import random
def generate_grid(size):
    terrain_types = ["tree", "plain", "food"]
    grid = {}
    counts = {"tree": 0, "plain": 0, "food": 0}
    for x in range(size):
        for y in range(size):
            grid[(x, y)] = random.choice(terrain_types)

    return grid

world = generate_grid(10)
for i in world:
    print(i)