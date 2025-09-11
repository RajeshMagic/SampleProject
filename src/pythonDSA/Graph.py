# ================================================================
# PYTHON DEMO: Graphs and Their Representations
# ================================================================
# Graph = Non-linear data structure with vertices (nodes) and edges
#
# Applications:
#   - Social Networks
#   - Maps & Navigation
#   - Internet (webpages & hyperlinks)
#   - Biology (neural networks, disease spread)
#
# Graph Representations:
#   1. Adjacency Matrix
#   2. Adjacency List
#
# Each representation has pros/cons:
#   - Matrix: Easy to understand, works for all graph types, but may waste space
#   - List: Saves space for sparse graphs, efficient for adjacency queries
# ================================================================


# ==============================
# GRAPH USING ADJACENCY MATRIX
# ==============================
class GraphMatrix:
    def __init__(self, vertices, directed=False, weighted=False):
        self.vertices = vertices  # List of vertex labels
        self.size = len(vertices)
        self.directed = directed
        self.weighted = weighted
        self.matrix = [[0] * self.size for _ in range(self.size)]

    def add_edge(self, u, v, weight=1):
        i, j = self.vertices.index(u), self.vertices.index(v)
        self.matrix[i][j] = weight if self.weighted else 1
        if not self.directed:
            self.matrix[j][i] = weight if self.weighted else 1

    def display(self):
        print("\n📊 Adjacency Matrix Representation")
        print("Vertices:", self.vertices)
        print("Matrix:")
        for row in self.matrix:
            print(row)

    def neighbors(self, u):
        i = self.vertices.index(u)
        return [self.vertices[j] for j, val in enumerate(self.matrix[i]) if val != 0]


# ==============================
# GRAPH USING ADJACENCY LIST
# ==============================
class GraphList:
    def __init__(self, vertices, directed=False, weighted=False):
        self.vertices = vertices
        self.directed = directed
        self.weighted = weighted
        self.adj_list = {v: [] for v in vertices}

    def add_edge(self, u, v, weight=1):
        if self.weighted:
            self.adj_list[u].append((v, weight))
            if not self.directed:
                self.adj_list[v].append((u, weight))
        else:
            self.adj_list[u].append(v)
            if not self.directed:
                self.adj_list[v].append(u)

    def display(self):
        print("\n📜 Adjacency List Representation")
        for v, edges in self.adj_list.items():
            print(f"{v} → {edges}")

    def neighbors(self, u):
        return self.adj_list[u]


# ==============================
# DEMONSTRATION
# ==============================
if __name__ == "__main__":
    print("\n==============================")
    print(" DEMO: Graphs in Python ")
    print("==============================\n")

    # -----------------------------------
    # 1. Undirected Graph - Adjacency Matrix
    # -----------------------------------
    print("\n🔹 Example 1: Undirected Graph (Adjacency Matrix)")
    vertices = ["A", "B", "C", "D"]
    g1 = GraphMatrix(vertices, directed=False, weighted=False)
    g1.add_edge("A", "B")
    g1.add_edge("A", "C")
    g1.add_edge("B", "D")
    g1.add_edge("C", "D")
    g1.display()
    print("Neighbors of A:", g1.neighbors("A"))

    # -----------------------------------
    # 2. Directed & Weighted Graph - Adjacency Matrix
    # -----------------------------------
    print("\n🔹 Example 2: Directed & Weighted Graph (Adjacency Matrix)")
    g2 = GraphMatrix(vertices, directed=True, weighted=True)
    g2.add_edge("A", "B", 3)
    g2.add_edge("A", "C", 1)
    g2.add_edge("B", "D", 2)
    g2.add_edge("C", "D", 4)
    g2.display()
    print("Neighbors of A:", g2.neighbors("A"))

    # -----------------------------------
    # 3. Undirected Graph - Adjacency List
    # -----------------------------------
    print("\n🔹 Example 3: Undirected Graph (Adjacency List)")
    g3 = GraphList(vertices, directed=False, weighted=False)
    g3.add_edge("A", "B")
    g3.add_edge("A", "C")
    g3.add_edge("B", "D")
    g3.add_edge("C", "D")
    g3.display()
    print("Neighbors of A:", g3.neighbors("A"))

    # -----------------------------------
    # 4. Directed & Weighted Graph - Adjacency List
    # -----------------------------------
    print("\n🔹 Example 4: Directed & Weighted Graph (Adjacency List)")
    g4 = GraphList(vertices, directed=True, weighted=True)
    g4.add_edge("A", "B", 3)
    g4.add_edge("A", "C", 1)
    g4.add_edge("B", "D", 2)
    g4.add_edge("C", "D", 4)
    g4.display()
    print("Neighbors of A:", g4.neighbors("A"))

    # -----------------------------------
    # Important Notes
    # -----------------------------------
    print("\n==============================")
    print(" IMPORTANT NOTES ")
    print("==============================")
    print("1. Graph = Vertices (nodes) + Edges (connections).")
    print("2. Adjacency Matrix: Easy, works for all cases, but may waste memory (O(V^2)).")
    print("3. Adjacency List: Saves memory for sparse graphs, efficient for adjacency (O(V+E)).")
    print("4. Directed Graph: Edges have a direction (A → B).")
    print("5. Weighted Graph: Edges carry weights (e.g., distances, costs).")
    print("6. Use List for large sparse graphs, Matrix for dense graphs or when quick edge lookup is needed.\n")
