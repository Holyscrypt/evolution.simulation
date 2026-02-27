import grid_system
import human
world = grid_system.generate_grid(100)
list_of_humans = []
tick = 0

for agent in range(100):
    agent = human.Human(world)
    list_of_humans.append(agent)

