import grid_system
import human

world = grid_system.generate_grid(100)
list_of_humans = []
tick = 0

for agent in range(100):
    agent = human.Human(world)
    list_of_humans.append(agent)
for ticks in range(19):
    survivors = []
    h0_position = list_of_humans[0].position
    for agents in list_of_humans:
        agents.move()
        agents.energy -= 5
        if not agents.energy <= 0:
            survivors.append(agents)
    list_of_humans = survivors
    print(f"{tick}: {h0_position} ---> {list_of_humans[0].position} {list_of_humans[0].energy}")
    tick += 1
print(len(list_of_humans))
