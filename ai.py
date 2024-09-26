# NAME(S): Kaleb Hannan, Shashank Reddy
#
# We were working in the same github repo 
#
# APPROACH: [WRITE AN OVERVIEW OF YOUR APPROACH HERE.]
#
# 

# The first case that needed to be solved was determining what to do when the agent was on the goal. 
# We implemented an if-statement that checks if the agent is at the goal (r), and if so, the agent returns 'U'.
# We implemented base cases for situations where the goal is in sight, 
# meaning the goal is present in one of the four directional percepts (N, S, E, W).
# In such cases, the agent immediately moves toward the goal in that direction.
# Now we needed to know where the agent is and track it 
# For this, we  created a structure that tracks where the agent has been using a graph-like map, represented with XY coordinates. 
# This allows the agent to detect if it is revisiting a node, helping to prevent loops or redundant exploration of the same area.
# Now we to update the node as the agent moves
#So The next step was to implement a map (or graph) of the environment that updates as the agent moves. 
# This map allows the agent to know where it has been and what areas are still unexplored. 
# As the agent moves, it updates the map with the current node and links it to neighboring nodes, 
# based on percepts indicating possible directions to move.
# For agents movement At first, we had the agent follow a fixed set of directions
# This approach gave the agent some predictability and always found the goal
# but made it prone to getting stuck in loops or revisiting the same areas unnecessarily.
# The agent wasn't exploring new regions and different worlds effectively because it always prioritized the same directions.
# To improve flexibility and avoid getting stuck, we later changed the agent's movement strategy to choose directions randomly
# when multiple unexplored directions were available. This random exploration allowed the agent to better cover new areas,
# avoiding predictable and redundant movements. The agent now selects a random direction from the available unexplored directions, 
# which helps it explore the environment more thoroughly.
# For backtracking,we  implemented a stack-based backtracking mechanism. 
# When the agent reaches a node where all neighboring areas have been explored or blocked, 
# it backtracks to the most recent unexplored node. This prevents the agent from getting stuck at dead ends.
# We also to need make sure the agent priotizes the maze to find a goal
# we did this by keeping track of unexplored directions from its current position. 
# It randomly chooses from these directions to explore, aiming to uncover new regions
#  and avoid visiting previously explored nodes unless necessary.
# When the agent moves, it updates its coordinates based on the direction (N, S, E, W). 
# It also updates the map with the newly visited node and its neighbors. T
# the agent ensures it does not move into walls (w) and only explores ground (g).



import random
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

        posibleDirection = []

        
        for direction in ['N', 'S', 'E', 'W']:
            next_node = self.get_neighbor_node(direction)
            if next_node and not next_node.visited:
                posibleDirection.append(direction)

        if len(posibleDirection) != 0:
            direction = random.choice(posibleDirection)
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
