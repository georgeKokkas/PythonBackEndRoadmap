# Write a function to detect if a cycle exists in an undirected 
# graph using DFS.

# Define a class for the Graph
class Graph:
    def __init__(self):
        self.graph = {}  # Initialize an empty dictionary to represent the graph

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []  # Initialize an empty list if the node is not in the graph
        if v not in self.graph:
            self.graph[v] = []  # Initialize an empty list if the node is not in the graph
        self.graph[u].append(v)  # Add the edge
        self.graph[v].append(u)  # Add the reverse edge (since the graph is undirected)

    # Function to detect a cycle in an undirected graph
    def has_cycle(self):
        visited = set()  # Set to keep track of visited nodes

        for node in self.graph:
            if node not in visited:
                if self._dfs(node, visited, -1):
                    return True
        return False

    # Helper function for DFS traversal
    def _dfs(self, node, visited, parent):
        visited.add(node)  # Mark the node as visited

        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self._dfs(neighbor, visited, node):
                    return True
            elif parent != neighbor:
                return True
        return False

# Create a graph and check for cycles
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)

print("Does the graph have a cycle?", g.has_cycle())  # Output: True
