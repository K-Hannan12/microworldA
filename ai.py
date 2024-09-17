# NAME(S): Kaleb Hannan, Shashank Reddy
#
# APPROACH: [WRITE AN OVERVIEW OF YOUR APPROACH HERE.]
#       When first looking at this the first think that I was think that I needed to do was ask 
#     my self what should my agent do when I see the goal or if it is on the goal.
#    

import random


class AI:
    def __init__(self):
        """
        Called once before the sim starts. You may use this function
        to initialize any data or data structures you need.
        """
        self.turn = 0

    def update(self, percepts):
        
        # If the agent is on the goal then return 'U'
        if percepts['X'] == 'r':
            return 'U'
        
        return random.choice(['N', 'S', 'E', 'W'])
    
"""
PERCEPTS:
Called each turn. Parameter "percepts" is a dictionary containing
nine entries with the following keys: X, N, NE, E, SE, S, SW, W, NW.
Each entry's value is a single character giving the contents of the
map cell in that direction. X gives the contents of the cell the agent
is in.

COMAMND:
This function must return one of the following commands as a string:
N, E, S, W, U

N moves the agent north on the map (i.e. up)
E moves the agent east
S moves the agent south
W moves the agent west
U uses/activates the contents of the cell if it is useable. For
example, stairs (o, b, y, p) will not move the agent automatically
to the corresponding hex. The agent must 'U' the cell once in it
to be transported.

The same goes for goal hexes (0, 1, 2, 3, 4, 5, 6, 7, 8, 9).
"""