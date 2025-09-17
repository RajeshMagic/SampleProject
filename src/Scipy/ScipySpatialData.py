import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay, ConvexHull, KDTree, distance

print("============================")
print("     SciPy Spatial Data Demo ")
print("============================\n")

# ---------------------------------------------------------------
# 1. Triangulation using Delaunay
# ---------------------------------------------------------------
print("[INFO] Triangulation divides points/polygons into triangles for analysis.")
points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])

delaunay = Delaunay(points)
print("Delaunay simplices (triangles indices):\n", delaunay.simplices)

plt.triplot(points[:, 0], points[:, 1], delaunay.simplices)
plt.scatter(points[:, 0], points[:, 1], color='red')
plt.title("Delaunay Triangulation")
plt.show()

# ---------------------------------------------------------------
# 2. Convex Hull
# ---------------------------------------------------------------
print("\n[INFO] Convex Hull is the smallest polygon enclosing all points.")
points2 = np.array([
  [2, 4], [3, 4], [3, 0], [2, 2], [4, 1],
  [1, 2], [5, 0], [3, 1], [1, 2], [0, 2]
])

hull = ConvexHull(points2)
print("Convex Hull simplices (edges indices):\n", hull.simplices)

plt.scatter(points2[:,0], points2[:,1])
for simplex in hull.simplices:
    plt.plot(points2[simplex,0], points2[simplex,1], 'k-')
plt.title("Convex Hull")
plt.show()

# ---------------------------------------------------------------
# 3. KDTree for Nearest Neighbors
# ---------------------------------------------------------------
print("\n[INFO] KDTree allows efficient nearest-neighbor queries.")
points3 = [(1, -1), (2, 3), (-2, 3), (2, -3)]
kdtree = KDTree(points3)

query_point = (1, 1)
dist, idx = kdtree.query(query_point)
print(f"Nearest neighbor to {query_point}: Distance = {dist}, Index = {idx}, Point = {points3[idx]}")

plt.scatter(*zip(*points3), c='blue', label='Points')
plt.scatter(*query_point, c='red', marker='x', s=100, label='Query Point')
plt.plot([query_point[0], points3[idx][0]], [query_point[1], points3[idx][1]], 'r--')
plt.title("KDTree Nearest Neighbor")
plt.legend()
plt.show()

# ---------------------------------------------------------------
# 4. Distance Metrics
# ---------------------------------------------------------------
print("\n[INFO] Distance metrics measure similarity or dissimilarity between points.")
p1, p2 = (1,0), (10,2)

# Euclidean Distance
eucl = distance.euclidean(p1, p2)
print("Euclidean Distance between", p1, "and", p2, ":", eucl)

# Cityblock Distance
city = distance.cityblock(p1, p2)
print("Cityblock (Manhattan) Distance:", city)

# Cosine Distance
cos = distance.cosine(p1, p2)
print("Cosine Distance:", cos)

# Hamming Distance
p3, p4 = (True, False, True), (False, True, True)
hamm = distance.hamming(p3, p4)
print("Hamming Distance between", p3, "and", p4, ":", hamm)

# Visualization of p1 and p2
plt.scatter(*p1, c='red', label='Point 1')
plt.scatter(*p2, c='blue', label='Point 2')
plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k--', label=f'Euclidean: {eucl:.2f}')
plt.title("Distance Metrics Example")
plt.legend()
plt.show()

# ---------------------------------------------------------------
# End of Demo
# ---------------------------------------------------------------
print("\n============================")
print(" End of SciPy Spatial Data Demo ")
print("============================")
