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
# Next I needed to start making the map of the enviorment so that we know how to get back if
# get to a dead end. So when we move to the next node we see were the Agent can move then linkes the current node
# to all of the nodes that the agent can move to. 
# Set up  coordinate to track where the agent is using nodes
#set up a stack for backtracking and direction to avoid immediate backtracking
# setting up a graph and updating with the visited percepts
# priotorzing exploring 
# setup back tracking 

class AI:
    def __init__(self):
        
        self.xCoord = 0
        self.yCoord = 0
        self.currentNode = Node(0, 0)
        self.currentNode.setVisitedToYes()  
        self.map = [self.currentNode]  
        self.path_stack = []  
        self.last_direction = None  

    def update(self, percepts):

        
        if percepts['X'][0] == 'r':
            print("Goal reached! Terminating...")
            return 'U'  
       
        
        for direction in ['N', 'S', 'E', 'W']:
            if 'r' in percepts[direction]:
                return self.move_in_direction(direction)

        
        self.update_graph(percepts)

        
        for direction in ['N', 'S', 'E', 'W']:
            next_node = self.get_neighbor_node(direction)
            if next_node and not next_node.visited:
                self.path_stack.append(self.currentNode)  
                self.last_direction = direction  
                return self.move_in_direction(direction)

        
        if self.path_stack:
            print("Backtracking to previous node...")
            backtrack_node = self.path_stack.pop()
            return self.backtrack_to_node(backtrack_node)

        # If no other options are left, default to moving east
        print("No more moves available, defaulting to move east.")
        return 'E'

    def move_in_direction(self, direction):
        target_node = self.get_neighbor_node(direction)
        if target_node is None:
            print(f"Creating new node in direction {direction} before moving.")
            self.create_neighbor_node(direction)  # Ensure node exists before moving

        if direction == 'N':
            self.xCoord += 1
            self.currentNode = self.currentNode.northNode
        elif direction == 'S':
            self.xCoord -= 1
            self.currentNode = self.currentNode.southNode
        elif direction == 'E':
            self.yCoord += 1
            self.currentNode = self.currentNode.eastNode
        elif direction == 'W':
            self.yCoord -= 1
            self.currentNode = self.currentNode.westNode
        
        if self.currentNode is None:
            raise ValueError(f"Error: Moved in direction {direction}, but currentNode is None.")

        print(f"Moved {direction}, new position: x={self.xCoord}, y={self.yCoord}")
        self.currentNode.setVisitedToYes()  # Mark the node as visited
        return direction

    def backtrack_to_node(self, backtrack_node):
        if self.currentNode.northNode == backtrack_node:
            return self.move_in_direction('N')
        elif self.currentNode.southNode == backtrack_node:
            return self.move_in_direction('S')
        elif self.currentNode.eastNode == backtrack_node:
            return self.move_in_direction('E')
        elif self.currentNode.westNode == backtrack_node:
            return self.move_in_direction('W')

    def update_graph(self, percepts):
        directions = {
            'N': (1, 0),
            'S': (-1, 0),
            'E': (0, 1),
            'W': (0, -1)
        }
        for direction, (dx, dy) in directions.items():
            if percepts[direction][0] == 'g':  # Ground is walkable
                neighbor_node = self.find_or_create_node(self.xCoord + dx, self.yCoord + dy)
                self.link_nodes(direction, neighbor_node)

    def find_or_create_node(self, x, y):
        for node in self.map:
            if node.xCoord == x and node.yCoord == y:
                return node
        new_node = Node(x, y)
        self.map.append(new_node)
        print(f"Created new node at x={x}, y={y}")
        return new_node

    def create_neighbor_node(self, direction):
        directions = {
            'N': (1, 0),
            'S': (-1, 0),
            'E': (0, 1),
            'W': (0, -1)
        }
        dx, dy = directions[direction]
        new_node = self.find_or_create_node(self.xCoord + dx, self.yCoord + dy)
        self.link_nodes(direction, new_node)

    def link_nodes(self, direction, neighbor_node):
        if direction == 'N':
            self.currentNode.setNorthNode(neighbor_node)
            neighbor_node.setSouthNode(self.currentNode)
        elif direction == 'S':
            self.currentNode.setSouthNode(neighbor_node)
            neighbor_node.setNorthNode(self.currentNode)
        elif direction == 'E':
            self.currentNode.setEastNode(neighbor_node)
            neighbor_node.setWestNode(self.currentNode)
        elif direction == 'W':
            self.currentNode.setWestNode(neighbor_node)
            neighbor_node.setEastNode(self.currentNode)

    def get_neighbor_node(self, direction):
        if direction == 'N':
            return self.currentNode.northNode
        elif direction == 'S':
            return self.currentNode.southNode
        elif direction == 'E':
            return self.currentNode.eastNode
        elif direction == 'W':
            return self.currentNode.westNode
        return None

class Node:
    def __init__(self, X, Y):
        self.xCoord = X
        self.yCoord = Y
        self.northNode = None
        self.southNode = None
        self.eastNode = None
        self.westNode = None
        self.visited = False
    
    def setNorthNode(self, node):
        self.northNode = node
    
    def setSouthNode(self, node):
        self.southNode = node
    
    def setEastNode(self, node):
        self.eastNode = node
    
    def setWestNode(self, node):
        self.westNode = node
    
    def setVisitedToYes(self):
        self.visited = True
