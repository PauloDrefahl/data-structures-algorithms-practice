class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list representation

    def add_edge(self, u, v, directed=False):
        """
        Adds an edge to the graph.
        
        Parameters:
        - u: Starting vertex of the edge.
        - v: Ending vertex of the edge.
        - directed: If True, the edge is directed (u -> v).
                    If False, the edge is undirected (u <-> v).
        """
        # Add edge from u to v
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

        # If the graph is undirected, add the reverse edge as well
        if not directed:
            if v not in self.graph:
                self.graph[v] = []
            self.graph[v].append(u)

    def display(self):
        """
        Prints the adjacency list of the graph.
        """
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")

# Create a new graph
g = Graph()

# Add edges to the graph
# u = 0, v = 1: Edge between vertex 0 and vertex 1
g.add_edge(0, 1)

# u = 0, v = 2: Edge between vertex 0 and vertex 2
g.add_edge(0, 2)

# u = 1, v = 3: Edge between vertex 1 and vertex 3
g.add_edge(1, 3)

# u = 3, v = 4: Directed edge from vertex 3 to vertex 4
g.add_edge(3, 4, directed=True)

# Display the graph
g.display()
