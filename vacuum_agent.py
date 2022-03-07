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
coords = {0 : [0,0,0]}
hit = 0
trade = 0
height = 0
width = 0
curr_len = 0
prev_len = 0
state = "foward"
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

def change_coord():
  global dir
  global coords
  global x
  print(coords, x)
  if dir == "north":
      coords[x] = [coords[x-1][0], coords[x-1][1] + 1, hit]
  if dir == "south":
      coords[x] = [coords[x-1][0], coords[x-1][1] - 1, hit]
  if dir == "east":
      coords[x] = [coords[x-1][0] + 1, coords[x-1][1], hit]
  if dir == "west":
      coords[x] = [coords[x-1][0] - 1, coords[x-1][1], hit]
  # print(coords[-1])



def state_agent(placement): # true is dirty, false is clean

    global ill_dir
    global dir
    global path
    global coords
    global hit
    global dirs
    global state
    global x

    l_dir = []
    oppdir = ""
    # print(coords)
    if placement: # cleaning
        path.append("dirty")
        return "clean"
    else:
        if path == ["dirty"]: # first case
            path.append("clean")
            dir = "south"
            dirs.append(dir)
            # coords.pop(0) # pop dummy first initializer coords
            change_coord()
            x += 1
            return dir
        else:
            if path[-1] == "clean": # i've hit a boundary
                state = "backward"
                hit += 1
                print("in clean: ", coords, x)
                if coords[x-1][2] == 1: # init back track
                    if len(dirs) > 0:
                        dir = exc_none1[exc_none.index(dirs.pop())]
                        ill_dir.append(dir)
                        # coords.pop()
                    else:
                        dir = random.choice(exc_none)
                        dirs.append(dir)
                        # change_coord()
                if coords[x-1][2] == 2: # dir = perp of init dir
                    if dir == "north" or dir == "south":
                        if "east" not in ill_dir: l_dir.append("east")
                        if "west" not in ill_dir: l_dir.append("west")
                        ill_dir.append(dir)
                        dir = random.choice(l_dir)
                    else:
                        if "north" not in ill_dir: l_dir.append("north")
                        if "south" not in ill_dir: l_dir.append("south")
                        ill_dir.append(dir)
                        dir = random.choice(l_dir)
                    print("go perp")
                    dirs.append(dir)
                    # change_coord()
                if coords[x-1][2] == 3: # come back to path
                    dir = exc_none1[exc_none.index(dirs[-1])]
                    # coords.pop()
                if coords[x-1][2] == 4: # continue that dir
                    dirs.append(dir)
                    # change_coord()
                    return dir
                if coords[x-1][2] == 5: # come back to the path
                    dir = exc_none1[exc_none.index(dirs.pop())]
                    # coords.pop()
                    ill_dir.clear()
                if coords[x-1][2] == 6: # move backward on the path
                    dir = exc_none1[exc_none.index(dirs.pop())]
                    # coords.pop()
                x += 1
                change_coord()
                return dir


            else: # im cleaning a line
                change_coord()
                hit = 0
                x += 1
                # hit should only equal zero at beginning of maneuver
                ill_dir.clear()
                state = "foward"
                dirs.append(dir)
                path.append("clean")
                return dir



run(6, 50000, state_agent)
# print(many_runs(20, 50000, 10, state_agent, state_agent_reset))
