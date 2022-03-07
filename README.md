# vacuum_world

The description of the vacuum world assignment from my artificial intelligence and machine learning class written by Peter Drake.


The Vacuum World
The vacuum world is a two-dimensional grid of spaces. Each space either contains an impassable wall, is dirty, or is clean. The agent (the simulated vacuum cleaner) is dropped into a random non-wall space. Its task is to clean up the world as quickly as possible. This is measured by “loss”; in each step of the simulation, the agent’s loss increases by the number of spaces in the world that are still dirty.

In each step, the agent receives a boolean percept. This is true if it is in a dirty space, false otherwise. The agent chooses one of the following actions:
'clean' (clean the current space)
'north' (move north)
'east' (move east)
'south' (move south)
'west' (move west)

If the agent cleans while in a dirty space, that space becomes clean. Cleaning a clean space has no effect. Moving moves to an adjacent space in the specified direction, unless that would move the agent into a wall or off the edge of the world; in that case, the action has no effect.

The agent does not know where it is, where the walls are, or whether its move actions have succeeded! The only thing it can sense is whether the current space is dirty.

The agent is defined as a function, which takes the percept as an argument and returns the action.
Your Agents
Reflex Agent
The reflex agent receives a percept and returns an action, with no randomness or memory. This is extremely ineffective, but easy to implement with an if statement.
Random Agent
The random agent also has no memory, but can act randomly. Surprisingly, this can be more effective than the reflex agent.
State Agent
The state agent is allowed to remember what it has seen and done in the past. This allows it to perform even better than the random agent.
