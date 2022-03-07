
# anna wolfe, sam flores, berto gonzalez, vic netessine

from vacuum import *

path = []
ill_dir = []
dir = ""
actions = ["north", "east", "south", "west", "clean"]
exc_none = ["north", "east", "south", "west"]
exc_none1 = ["south", "west", "north", "east"]



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

    path = []
    ill_dir = []
    dir = ""

def state_agent(placement): # true is dirty, false is clean

    global ill_dir
    global dir
    global path
    l_dir = []
    oppdir = ""
    # print(path)
    if placement: # cleaning
        path.append("dirty")
        return "clean"
    else:
        if path == ["dirty"]: # first case
            path.append("clean")
            dir = random.choice(exc_none)
            return dir
        else:
            if path[-1] == "clean": # i've hit a boundary

                # append legal dirs to legal dir list
                if "north" not in ill_dir: l_dir.append("north")
                if "south" not in ill_dir: l_dir.append("south")
                if "east" not in ill_dir: l_dir.append("east")
                if "west" not in ill_dir: l_dir.append("west")

                dir = random.choice(l_dir) # choose random legal dir
                oppdir = exc_none1[exc_none.index(dir)]
                # make the opposite dir an illegal dir

                if oppdir not in ill_dir:
                    ill_dir.append(exc_none1[exc_none.index(dir)])

                if dir == "east" or dir == "west":
                    if "north" in ill_dir:
                        ill_dir.remove("north")
                    if "south" in ill_dir:
                        ill_dir.remove("south")
                if dir == "south" or dir == "north":
                    if "east" in ill_dir:
                        ill_dir.remove("east")
                    if "west" in ill_dir:
                        ill_dir.remove("west")
                return dir
            else: # im cleaning a line
                path.append("clean")
                return dir



run(20, 50000, state_agent)
# print(many_runs(20, 50000, 10, state_agent, state_agent_reset))
