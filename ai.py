# NAME(S): Kaleb Hannan, Shashank Reddy
#
# We were working in the same github repo 
#
# APPROACH: [WRITE AN OVERVIEW OF YOUR APPROACH HERE.]
#
#   The first case that I had to solve was what to do when the agent was on the Goal.
# For this I made and if statment so if the agent was on the goal then it would return 'U'.
# After this I created more of the base cases were if the goal is in sight (were the goal is in the list of any
# of the 4 direction) then the agent would move towrds the goal.  
# 
#   The next thing that we needed to do is to make a Graph so that we know where are AI has been.  
# We made XY Coordinates for the AI so if we do end up in a loop of node we 
# we know that we have alread be to that node.
#    

import random


class AI:
    def __init__(self):
        # Coordinates to know were the AI is in the map
        self.xCoord = 0
        self.yCoord = 0
        StartNode = Node(0,0)
        StartNode.setVisitedToYes
        self.currentNode = StartNode
        # Map to see where the agent has been 
        self.map = [StartNode]
        self.frontier = []

    def update(self, percepts):

        # If the agent is on the goal then return 'U'
        if percepts['X'][0] == 'r':
            return 'U'
        
        #If the goal is in the 'N' dictionary then go North
        for i in percepts['N']:
            if i == 'r':
                self.xCoord += 1
                return 'N'
        
        #If the goal is in the 'S' dictionary then go South
        for i in percepts['S']:
            if i == 'r':
                self.xCoord += -1
                return 'S'
        
        #If the goal is in the 'E' dictionary then go East
        for i in percepts['E']:
            if i == 'r':
                self.yCoord += 1
                return 'E'
        
        #If the goal is in the 'W' dictionary then go West
        for i in percepts['W']:
            if i == 'r':
                self.yCoord += -1
                return 'W'
        

        #Sets North node if it exist 
        if percepts['N'][0] == 'g':
            if self.currentNode.northNode == None:
                for node in self.map:
                    if node.xCoord == (self.currentNode.xCoord + 1) and node.yCoord == (self.currentNode.yCoord):
                        self.currentNode.setNorthNode(node)
                        node.setSouthNode(self.currentNode)
                        break
                newNode = Node(self.currentNode.xCoord + 1,self.currentNode.yCoord)
                self.map.append(newNode)
                self.currentNode.setNorthNode(newNode)

        #Sets South node if it exist 
        if percepts['S'][0] == 'g':
            if self.currentNode.southNode == None:
                for node in self.map:
                    if node.xCoord == (self.currentNode.xCoord - 1) and node.yCoord == (self.currentNode.yCoord):
                        self.currentNode.setSouthNode(node)
                        node.setNorthNode(self.currentNode)
                        break
                newNode = Node(self.currentNode.xCoord - 1,self.currentNode.yCoord)
                self.map.append(newNode)
                self.currentNode.setSouthNode(newNode)
                newNode.setNorthNode(self.currentNode)

        #Sets East node if it exist 
        if percepts['E'][0] == 'g':
            if self.currentNode.eastNode == None:
                for node in self.map:
                    if node.xCoord == (self.currentNode.xCoord) and node.yCoord == (self.currentNode.yCoord + 1):
                        self.currentNode.setEastNode(node)
                        node.setWestNode(self.currentNode)
                        break
                newNode = Node(self.currentNode.xCoord,self.currentNode.yCoord + 1)
                self.map.append(newNode)
                self.currentNode.setEastNode(newNode)
                newNode.setWestNode(self.currentNode)
        
        #Sets West node if it exist 
        if percepts['E'][0] == 'g':
            if self.currentNode.eastNode == None:
                for node in self.map:
                    if node.xCoord == (self.currentNode.xCoord) and node.yCoord == (self.currentNode.yCoord - 1):
                        self.currentNode.setWestNode(node)
                        node.setEastNode(self.currentNode)
                        break
                newNode = Node(self.currentNode.xCoord,self.currentNode.yCoord - 1)
                self.map.append(newNode)
                newNode.setEastNode(self.currentNode)
                self.currentNode.setWestNode(newNode) 

        return random.choice(['N', 'S', 'E', 'W'])

class Node:
    def __init__(self,X,Y):
        self.xCoord = X
        self.yCoord = Y
        self.northNode = None
        self.southNode = None
        self.eastNode = None
        self.westNode = None
        self.visited = "no"
    
    def setNorthNode(self,node):
        self.northNode = node
    
    def setSouthNode(self,node):
        self.southNode = node
    
    def setEastNode(self,node):
        self.eastNode = node
    
    def setWestNode(self,node):
        self.SouthNode = node
    
    def setVisitedToYes(self):
        self.visited = "yes"
    
    