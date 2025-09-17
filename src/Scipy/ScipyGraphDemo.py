import numpy as np
import matplotlib.pyplot as plt
import networkx as nx  # For visualization
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import (
    connected_components, dijkstra, floyd_warshall, 
    bellman_ford, depth_first_order, breadth_first_order
)

print("============================")
print("     SciPy Graphs Demo      ")
print("============================\n")

# ---------------------------------------------------------------
# 1. Adjacency Matrix
# ---------------------------------------------------------------
print("[INFO] Graphs can be represented using adjacency matrices.")
arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr = csr_matrix(arr)
print("\nAdjacency Matrix:\n", arr)

# Visualization using NetworkX
G = nx.from_numpy_array(arr, create_using=nx.DiGraph)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(i, j): arr[i][j] for i in range(len(arr)) for j in range(len(arr)) if arr[i][j] != 0})
plt.title("Graph Visualization")
plt.show()

# ---------------------------------------------------------------
# 2. Connected Components
# ---------------------------------------------------------------
print("============================")
print(" Connected Components")
print("============================")
components = connected_components(newarr)
print("Connected Components Result:", components)

# ---------------------------------------------------------------
# 3. Dijkstra Shortest Path
# ---------------------------------------------------------------
print("\n============================")
print(" Dijkstra Shortest Path")
print("============================")
shortest_paths, predecessors = dijkstra(newarr, return_predecessors=True, indices=0)
print("Shortest path distances from node 0:", shortest_paths)
print("Predecessor matrix:\n", predecessors)

# ---------------------------------------------------------------
# 4. Floyd Warshall
# ---------------------------------------------------------------
print("\n============================")
print(" Floyd Warshall")
print("============================")
fw_paths, fw_pred = floyd_warshall(newarr, return_predecessors=True)
print("All-pairs shortest path distances:\n", fw_paths)
print("Predecessor matrix:\n", fw_pred)

# ---------------------------------------------------------------
# 5. Bellman Ford (Handles negative weights)
# ---------------------------------------------------------------
print("\n============================")
print(" Bellman Ford")
print("============================")
arr_bf = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr_bf = csr_matrix(arr_bf)
bf_paths, bf_pred = bellman_ford(newarr_bf, return_predecessors=True, indices=0)
print("Shortest path distances from node 0 (with negative weights):", bf_paths)
print("Predecessor matrix:\n", bf_pred)

# ---------------------------------------------------------------
# 6. Depth First Order
# ---------------------------------------------------------------
print("\n============================")
print(" Depth First Traversal")
print("============================")
arr_dfs = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])
newarr_dfs = csr_matrix(arr_dfs)
dfs_order, dfs_predecessors = depth_first_order(newarr_dfs, 1)
print("DFS Order starting from node 1:", dfs_order)
print("DFS Predecessors:", dfs_predecessors)

# ---------------------------------------------------------------
# 7. Breadth First Order
# ---------------------------------------------------------------
print("\n============================")
print(" Breadth First Traversal")
print("============================")
arr_bfs = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])
newarr_bfs = csr_matrix(arr_bfs)
bfs_order, bfs_predecessors = breadth_first_order(newarr_bfs, 1)
print("BFS Order starting from node 1:", bfs_order)
print("BFS Predecessors:", bfs_predecessors)

# ---------------------------------------------------------------
# End of Demo
# ---------------------------------------------------------------
print("\n============================")
print(" End of SciPy Graphs Demo ")
print("============================")
