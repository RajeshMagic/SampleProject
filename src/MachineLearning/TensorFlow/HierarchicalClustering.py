# Machine Learning - Hierarchical Clustering Demonstration
# Author: Training Script
# -------------------------------------------------
# This script demonstrates:
#   - Creating 2D data points
#   - Visualizing raw data points
#   - Computing hierarchical clustering using Ward linkage and Euclidean distance
#   - Visualizing dendrogram
#   - Using scikit-learn AgglomerativeClustering for clustering
#   - Visualizing clusters in a 2D scatter plot
# -------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# -------------------------------------------------
# Step 1: Create and visualize data points
# -------------------------------------------------
x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# Combine x and y into a single dataset
data = list(zip(x, y))
print("\n--- Step 1: Data Points ---")
for i, point in enumerate(data):
    print(f"Point {i}: {point}")

# Visualize raw data points
plt.scatter(x, y, color='blue')
plt.title("Raw Data Points")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Important Note
print("\nImportant Note: Each point is treated as its own cluster initially.")

# -------------------------------------------------
# Step 2: Compute linkage and visualize dendrogram
# -------------------------------------------------
linkage_data = linkage(data, method='ward', metric='euclidean')

print("\n--- Step 2: Linkage Data (Ward, Euclidean) ---")
print(linkage_data)

# Plot dendrogram
plt.figure(figsize=(10, 5))
dendrogram(linkage_data, labels=range(1, len(data)+1))
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Data Point Index")
plt.ylabel("Euclidean Distance")
plt.show()

# Important Note
print("\nImportant Note: Dendrogram shows hierarchical merging from individual points to single cluster.")

# -------------------------------------------------
# Step 3: Agglomerative Clustering using scikit-learn
# -------------------------------------------------
# Create AgglomerativeClustering object
hierarchical_cluster = AgglomerativeClustering(
    n_clusters=2,   # Number of clusters to form
    affinity='euclidean', 
    linkage='ward'
)

# Fit and predict cluster labels
labels = hierarchical_cluster.fit_predict(data)

print("\n--- Step 3: Cluster Labels ---")
for i, label in enumerate(labels):
    print(f"Point {i} -> Cluster {label}")

# -------------------------------------------------
# Step 4: Visualize clusters in 2D
# -------------------------------------------------
plt.scatter(x, y, c=labels, cmap='rainbow', edgecolor='k', s=100)
plt.title("Hierarchical Clustering - 2D Cluster Visualization")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Important Notes for Understanding:
print("\nImportant Notes:")
print("1. Agglomerative Clustering starts with each point as its own cluster and merges clusters iteratively.")
print("2. 'ward' linkage minimizes variance between clusters.")
print("3. 'affinity=euclidean' specifies Euclidean distance for measuring similarity.")
print("4. Dendrogram visualizes hierarchical relationships among data points.")
print("5. 2D scatter plot shows points colored by their cluster assignment.")
