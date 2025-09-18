"""
Bagging Example with Wine Dataset
Demonstrates:
- Base Decision Tree classifier performance
- Bagging (Bootstrap Aggregation) with different n_estimators
- Accuracy visualization
- Out-of-Bag (OOB) score estimation
- Visualization of individual decision trees from the ensemble
"""

# ------------------------------
# Step 1: Import required modules
# ------------------------------
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import BaggingClassifier

# ------------------------------
# Step 2: Load Wine dataset
# ------------------------------
print("Step 2: Loading Wine dataset...")
data = datasets.load_wine(as_frame=True)
X = data.data
y = data.target
print(f"Dataset loaded with {X.shape[0]} samples and {X.shape[1]} features.\n")

# ------------------------------
# Step 3: Split dataset into train/test sets
# ------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=22
)
print(f"Train samples: {X_train.shape[0]}, Test samples: {X_test.shape[0]}\n")

# ------------------------------
# Step 4: Evaluate Base Decision Tree
# ------------------------------
print("Step 4: Training base Decision Tree classifier...")
dtree = DecisionTreeClassifier(random_state=22)
dtree.fit(X_train, y_train)

y_train_pred = dtree.predict(X_train)
y_test_pred = dtree.predict(X_test)

print("Base Decision Tree Accuracy:")
print(f"Train data accuracy: {accuracy_score(y_train, y_train_pred):.4f}")
print(f"Test data accuracy: {accuracy_score(y_test, y_test_pred):.4f}\n")
print("Important Note: Base Decision Tree may overfit (100% train accuracy) leading to lower test accuracy.\n")

# ------------------------------
# Step 5: Bagging with multiple n_estimators
# ------------------------------
print("Step 5: Evaluating Bagging Classifier with multiple n_estimators...")
estimator_range = [2, 4, 6, 8, 10, 12, 14, 16]
scores = []

for n_estimators in estimator_range:
    clf = BaggingClassifier(n_estimators=n_estimators, random_state=22)
    clf.fit(X_train, y_train)
    test_score = accuracy_score(y_test, clf.predict(X_test))
    scores.append(test_score)
    print(f"n_estimators={n_estimators}, Test Accuracy={test_score:.4f}")

# Plotting accuracy vs n_estimators
plt.figure(figsize=(9,6))
plt.plot(estimator_range, scores, marker='o')
plt.title("Bagging Classifier Accuracy vs n_estimators", fontsize=16)
plt.xlabel("Number of Estimators (n_estimators)", fontsize=14)
plt.ylabel("Test Accuracy", fontsize=14)
plt.xticks(estimator_range)
plt.grid(True)
plt.show()
print("Important Note: Bagging improves test accuracy by reducing overfitting.\n")

# ------------------------------
# Step 6: Bagging with Out-of-Bag (OOB) Score
# ------------------------------
print("Step 6: Training Bagging Classifier with OOB estimation...")
oob_model = BaggingClassifier(n_estimators=12, oob_score=True, random_state=22)
oob_model.fit(X_train, y_train)

print(f"OOB Score: {oob_model.oob_score_:.4f}")
print("Important Note: OOB score provides a quick estimate of model accuracy without separate validation set.\n")

# ------------------------------
# Step 7: Visualizing first Decision Tree from Bagging Ensemble
# ------------------------------
print("Step 7: Visualizing first Decision Tree from Bagging Classifier...")

plt.figure(figsize=(20, 15))
plot_tree(
    oob_model.estimators_[0],
    feature_names=X.columns,
    class_names=data.target_names,
    filled=True,
    rounded=True
)
plt.title("First Decision Tree from Bagging Ensemble", fontsize=16)
plt.show()
print("Important Note: Each tree in the ensemble contributes to majority vote for final prediction.")
