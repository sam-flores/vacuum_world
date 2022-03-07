from vacuum import *


path = []
ill_dir = []
dirs = []
dir = ""
actions = ["north", "east", "south", "west", "clean"]
exc_none = ["north", "east", "south", "west"]
exc_none1 = ["south", "west", "north", "east"]
ns = ['north', 'south']
we = ['west', 'east']
coords = {() : []}
hit = 0
x = 1



def reflex_agent(placement):
    if placement:
        return "clean"
    else:
        return "south"

def random_agent(placement):
    if placement:
        return "clean"
    else:
        return random.choice(exc_none)


def state_agent_reset():
    global ill_dir
    global x
    global dir
    global path
    global dirs
    global hit

    path = []
    ill_dir = []
    dirs = []
    dir = ""
    hit = 0
    x = 0

def change_coord(dir, hit):
  global coords
  global x
  print(coords, x)
  if dir == "north":
      coords[]
      coords[] = [coords[x-1][0], coords[x-1][1] + 1, hit]
  if dir == "south":
      coords[x] = [coords[x-1][0], coords[x-1][1] - 1, hit]
  if dir == "east":
      coords[x] = [coords[x-1][0] + 1, coords[x-1][1], hit]
  if dir == "west":
      coords[x] = [coords[x-1][0] - 1, coords[x-1][1], hit]
  # print(coords[-1])



def state_agent(placement): # true is dirty, false is clean

    global dir

    if placement:
        return "clean"
    else:
        dir = random.choice(exc_none)
        hit = 0
        change_coord(dir, hit)
        return dir



run(6, 50000, state_agent)
# print(many_runs(20, 50000, 10, state_agent, state_agent_reset))
