import random
import stddraw
import statistics

OFFSETS = {'north': (0, 1), 'east': (1, 0), 'south': (0, -1), 'west': (-1, 0)}


def generate_world(width):
    def f():
        r = random.random()
        if r < 0.05:
            return 'wall'
        elif r < 1.0:
            return 'dirt'
        else:
            return 'clear'
    return [[f() for _ in range(width)] for _ in range(width)]


def place_agent(world):
    width = len(world)
    while True:
        x = random.randrange(width)
        y = random.randrange(width)
        if world[x][y] != 'wall':
            return x, y


def draw_world(world, agent):
    width = len(world)
    stddraw.clear()
    for x in range(width):
        for y in range(width):
            here = world[x][y]
            if here == 'wall':
                stddraw.setPenColor(stddraw.BLACK)
                stddraw.filledSquare(x, y, 0.45)
            elif here == 'dirt':
                stddraw.setPenColor(stddraw.ORANGE)
                stddraw.filledCircle(x, y, 0.45)
            if agent == (x, y):
                stddraw.setPenColor(stddraw.BLUE)
                stddraw.filledPolygon([x - 0.45, x + 0.45, x], [y - 0.45, y - 0.45, y + 0.45])
    stddraw.show(100)


def vector_sum(p, q):
    return tuple([a + b for a, b in zip(p, q)])


def take_action(world, agent, agent_function):
    x, y = agent
    width = len(world)
    action = agent_function(world[x][y] == 'dirt')
    if action == 'clean':
        world[x][y] = 'clean'
        return agent
    else:
        x, y = vector_sum(agent, OFFSETS[action])
        if 0 <= x < width and 0 <= y < width and world[x][y] != 'wall':
            return x, y
        else:
            return agent


def count_dirt(world):
    width = len(world)
    result = 0
    for x in range(width):
        for y in range(width):
            if world[x][y] == 'dirt':
                result += 1
    return result


def run(width, steps, agent_function, agent_reset_function=lambda : None, animate=True):
    agent_reset_function()
    if animate:
        stddraw.setXscale(-0.5, width - 0.5)
        stddraw.setYscale(-0.5, width - 0.5)
    world = generate_world(width)
    agent = place_agent(world)
    loss = 0
    if animate:
        draw_world(world, agent)
    for i in range(steps):
        agent = take_action(world, agent, agent_function)
        loss += count_dirt(world)
        if animate:
            draw_world(world, agent)
    if animate:
        print('Loss: ', loss)
        print('Click in window to exit')
        while True:
            if stddraw.mousePressed():
                exit()
            stddraw.show(0)
    return loss


def many_runs(width, steps, runs, agent_function, agent_reset_function=lambda : None):
    return statistics.mean([run(width, steps, agent_function, agent_reset_function, False) for i in range(runs)])
