# Create a graph using adjacency lists and implement Dijkstra's 
# algorithm for finding the shortest path.

import heapq  # Import heapq for priority queue implementation

# Define a class for the Graph
class Graph:
    def __init__(self):
        self.graph = {}  # Initialize an empty dictionary to represent the graph

    # Function to add an edge to the graph
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []  # Initialize an empty list if the node is not in the graph
        if v not in self.graph:
            self.graph[v] = []  # Ensure the neighbor node is also added to the graph
        self.graph[u].append((v, weight))  # Add the edge with weight

    # Function to implement Dijkstra's algorithm
    def dijkstra(self, start):
        # Initialize distances to all nodes as infinity
        distances = {node: float('infinity') for node in self.graph}
        distances[start] = 0  # Distance to the start node is 0
        priority_queue = [(0, start)]  # Initialize the priority queue with the start node

        while priority_queue:
            # Get the node with the smallest distance
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue  # Skip if the distance is not the smallest

            for neighbor, weight in self.graph[current_node]:
                # Calculate the new distance
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    # Update the distance if it's smaller
                    distances[neighbor] = distance
                    # Add the neighbor to the priority queue
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Create a graph and perform operations
g = Graph()
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)

print("Shortest paths from node 'A':")
print(g.dijkstra('A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}

