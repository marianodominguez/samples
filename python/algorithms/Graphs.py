'''
Graphs are a collection of vertices and edges. 
Vertices are the nodes of the graph.
Edges are the connections between nodes.

There are two types of graphs:
    directed graphs
    undirected graphs

Graphs can be represented in two ways:
    adjacency matrix
    adjacency list

Graphs can be traversed in two ways:
    depth first search
    breadth first search
'''

# Graph class
class Graph:

    # Graph constructor
    def __init__(self, size):
        self.vertexList = []
        self.adjMatrix = [0] * size
        self.adjList= [ [] for i in range(size) ]

        # Initialize the adjacency matrix
        for i in range(size):
            self.adjMatrix[i] = [0] * size

    # Add a vertex to the graph
    def addVertex(self, v):
        self.vertexList.append(v)
    
    # Add an edge to the graph
    def addEdge(self, a, b):
        node1 = self.vertexList.index(a)
        node2 = self.vertexList.index(b)
        #check that nodes exist
        #avoid repetitions
        self.adjList[node1].append(node2)
        self.adjList[node2].append(node1)
        self.adjMatrix[node1][node2] = 1
        self.adjMatrix[node2][node1] = 1

    # Depth First Search path
    def dfs_path(self, a, b):
        # Get the index of the start and end vertices
        start = self.vertexList.index(a)
        end = self.vertexList.index(b)
        # Initialize the stack
        stack = [start]
        path = [start]
        visited = [start]
        current = start

        # While there are nodes to visit
        while stack:
            # Get the next nodes
            nextNodes = self.adjList[current]
            for next in nextNodes:
                # If the next node is the end node
                found = False
                # If the next node is not visited
                if next not in visited:
                    # Add the next node to the stack
                    stack.append(next)
                    # Set the current node to the next node
                    current = next;
                    # Add the current node to the path
                    path.append(current)
                    # Set found to true
                    found = True
                    # Break the loop
                    break
            # If the next node is visited
            if not found and stack:
                # Pop the stack
                current = stack.pop()
            visited.append(current)
            # If the current node is the end node
            if current == end:
                return path
        return []

    # Breadth First Search path
    def bfs_path(self, a, b):
        # Get the index of the start and end vertices
        start = self.vertexList.index(a)
        end = self.vertexList.index(b)
        # Initialize the queue
        queue = [start]
        path = []
        visited = [start]
        current = None
        while queue:
            # Print the queue and current node
            print(queue, current)
            current = queue[0]
            path.append(current)
            visited.append(current)
            queue.remove(current)
            # If the current node is the end node
            if current == end:
                return path
            # Get the next nodes
            nextNodes = self.adjList[current]
            for n in nextNodes:
                # If the next node is not visited
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
        return []

    # Path values
    def pathValues(self, path=[]):
        return [self.vertexList[i] for i in path]
