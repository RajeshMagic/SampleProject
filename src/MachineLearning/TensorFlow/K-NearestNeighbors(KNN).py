"""
K-Nearest Neighbors (KNN) Demonstration
This script demonstrates:
- KNN algorithm for classification
- Effect of different K values on predictions
- Visualization of the dataset and new points
- Console outputs with explanations
"""

# ------------------------------
# Step 1: Import required modules
# ------------------------------
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# ------------------------------
# Step 2: Create example dataset
# ------------------------------
print("Step 2: Creating example dataset...")

# Input features
x = [4, 5, 10, 4, 3, 11, 14, 8, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
# Target class labels
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

# Combine features into a list of points
data = list(zip(x, y))
print("Feature points:")
print(data)
print("Class labels:")
print(classes)
print("Important Note: Each point has a corresponding class label (0 or 1).")

# ------------------------------
# Step 3: Visualize dataset
# ------------------------------
plt.figure(figsize=(6,5))
plt.scatter(x, y, c=classes, cmap='bwr', edgecolor='k', s=100)
plt.xlabel("Feature X")
plt.ylabel("Feature Y")
plt.title("Original Dataset")
plt.show()
print("Important Note: Blue represents class 0, Red represents class 1.\n")

# ------------------------------
# Step 4: KNN with K=1
# ------------------------------
print("Step 4: Fit KNN with K=1...")
knn1 = KNeighborsClassifier(n_neighbors=1)
knn1.fit(data, classes)

# Predict a new point
new_x = 8
new_y = 21
new_point = [(new_x, new_y)]
prediction1 = knn1.predict(new_point)
print(f"Prediction for new point {new_point}: Class {prediction1[0]}")

# Plot new point with dataset
plt.figure(figsize=(6,5))
plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction1[0]], cmap='bwr', edgecolor='k', s=100)
plt.text(new_x-1.7, new_y-0.7, f"new point, class: {prediction1[0]}")
plt.xlabel("Feature X")
plt.ylabel("Feature Y")
plt.title("KNN with K=1")
plt.show()
print("Important Note: With K=1, the new point is classified based on the nearest neighbor.\n")

# ------------------------------
# Step 5: KNN with K=5
# ------------------------------
print("Step 5: Fit KNN with K=5...")
knn5 = KNeighborsClassifier(n_neighbors=5)
knn5.fit(data, classes)

# Predict the same new point
prediction5 = knn5.predict(new_point)
print(f"Prediction for new point {new_point}: Class {prediction5[0]}")

# Plot new point with dataset
plt.figure(figsize=(6,5))
plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction5[0]], cmap='bwr', edgecolor='k', s=100)
plt.text(new_x-1.7, new_y-0.7, f"new point, class: {prediction5[0]}")
plt.xlabel("Feature X")
plt.ylabel("Feature Y")
plt.title("KNN with K=5")
plt.show()
print("Important Note: With K=5, the new point is classified based on majority vote of 5 nearest neighbors.\n")

# ------------------------------
# Step 6: Compare predictions for multiple K values
# ------------------------------
print("Step 6: Compare predictions for multiple K values...")
k_values = [1, 3, 5, 7]
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(data, classes)
    pred = knn.predict(new_point)
    print(f"K={k}, Predicted class for new point {new_point}: {pred[0]}")
print("Important Note: Increasing K can make predictions more stable and less sensitive to outliers.")
