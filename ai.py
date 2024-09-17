# NAME(S): Kaleb Hannan, Shashank Reddy
#
# APPROACH: [WRITE AN OVERVIEW OF YOUR APPROACH HERE.]
#
#   The first case that I had to solve was what to do when the agent was on the Goal.
# For this I made and if statment so if the agent was on the goal then it would return 'U'.
# After this I created more of the base cases were if the goal is in sight (were the goal is in the list of any
# of the 4 direction) then the agent would move towrds the goal.  
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
        if percepts['X'][0] == 'r':
            return 'U'
        
        #If the goal is in the 'N' dictionary then go North
        for i in percepts['N']:
            if i == 'r':
                return 'N'
        
        #If the goal is in the 'S' dictionary then go South
        for i in percepts['S']:
            if i == 'r':
                return 'S'
        
        #If the goal is in the 'E' dictionary then go East
        for i in percepts['E']:
            if i == 'r':
                return 'E'
        
        #If the goal is in the 'W' dictionary then go West
        for i in percepts['W']:
            if i == 'r':
                return 'W'
        
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