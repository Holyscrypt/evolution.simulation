import grid_system
import human
world = grid_system.generate_grid(100)
list_of_humans = []
tick = 0

for agent in range(100):
    agent = human.Human(world)
    list_of_humans.append(agent)
for ticks in range(1000):
    h0_position = list_of_humans[0].position
    for agents in list_of_humans:
        agents.move()
    print(f"{h0_position} ---> {list_of_humans[0].position}")
    tick+= 1
