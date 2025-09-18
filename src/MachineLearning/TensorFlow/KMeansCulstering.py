# Machine Learning - K-means Clustering
# --------------------------------------
# This script demonstrates:
#   - Visualizing data points
#   - Using the elbow method to estimate the optimal number of clusters (K)
#   - Performing K-means clustering
#   - Visualizing clusters with colors
#   - Explaining inertia and cluster assignment
# --------------------------------------

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# -------------------------------------------------
# Step 1: Create Sample Data
# -------------------------------------------------
# Data represents two variables for 10 data points
x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# Combine the two lists into a single dataset of points
data = list(zip(x, y))

print("\n--- Step 1: Dataset Overview ---")
print(data)

# Visualize the data
plt.scatter(x, y, color='blue')
plt.title("Step 1: Scatter Plot of Data Points")
plt.xlabel("X Variable")
plt.ylabel("Y Variable")
plt.grid(True)
plt.show()

print("\nImportant Note: Visualizing raw data helps understand natural groupings.")

# -------------------------------------------------
# Step 2: Use Elbow Method to Find Optimal K
# -------------------------------------------------
# The elbow method evaluates inertia for different values of K
inertias = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

# Plot inertia vs number of clusters
plt.plot(range(1, 11), inertias, marker='o')
plt.title("Step 2: Elbow Method to Determine Optimal K")
plt.xlabel("Number of clusters (K)")
plt.ylabel("Inertia")
plt.grid(True)
plt.show()

print("\nImportant Note: The 'elbow' point is where inertia decreases linearly. "
      "This suggests the optimal number of clusters. In this example, K=2 seems appropriate.")

# -------------------------------------------------
# Step 3: Fit K-means with Optimal K
# -------------------------------------------------
optimal_k = 2
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(data)

# Get cluster labels for each data point
labels = kmeans.labels_
print("\n--- Step 3: Cluster Labels ---")
for idx, label in enumerate(labels):
    print(f"Data point {data[idx]} assigned to Cluster {label}")

# Get cluster centroids
centroids = kmeans.cluster_centers_
print("\n--- Step 3: Cluster Centroids ---")
print(centroids)

# -------------------------------------------------
# Step 4: Visualize Clusters
# -------------------------------------------------
# Color points based on cluster assignment
plt.scatter(x, y, c=labels, cmap='viridis', s=100)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title(f"Step 4: K-means Clustering with K={optimal_k}")
plt.xlabel("X Variable")
plt.ylabel("Y Variable")
plt.legend()
plt.grid(True)
plt.show()

print("\nImportant Note: Each color represents a cluster. The red 'X' marks are the centroids.")

# -------------------------------------------------
# Step 5: Optional Explanation
# -------------------------------------------------
print("\nStep 5: Key Points")
print("1. K-means clusters data into K groups by minimizing intra-cluster variance (inertia).")
print("2. The elbow method helps select a suitable K by visualizing inertia vs number of clusters.")
print("3. Each iteration reassigns points to nearest centroids and updates centroid positions.")
print("4. Convergence occurs when point assignments no longer change.")
