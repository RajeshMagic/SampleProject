# Machine Learning - Grid Search Demonstration
# ---------------------------------------------
# This script demonstrates:
#   - Loading the Iris dataset
#   - Training a Logistic Regression model
#   - Evaluating the default model
#   - Implementing a Grid Search over the regularization parameter C
#   - Visualizing the model performance against different C values
# ---------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

# -----------------------------------------------------
# Step 1: Load dataset
# -----------------------------------------------------
iris = datasets.load_iris()
X = iris['data']      # Features: Sepal and Petal measurements
y = iris['target']    # Target: Iris species

print("\n--- Step 1: Dataset Overview ---")
print(f"Number of samples: {X.shape[0]}, Number of features: {X.shape[1]}")
print(f"Target classes: {np.unique(y)}")
print("First 5 samples of X:\n", X[:5])
print("First 5 labels of y:\n", y[:5])

# Important Note
print("\nImportant Note: Logistic Regression can classify data into multiple categories (multinomial) as seen here.")

# -----------------------------------------------------
# Step 2: Train Logistic Regression with default parameters
# -----------------------------------------------------
logit_default = LogisticRegression(max_iter=10000, multi_class='multinomial', solver='lbfgs')
logit_default.fit(X, y)
default_score = logit_default.score(X, y)

print("\n--- Step 2: Default Logistic Regression ---")
print(f"Default model score (accuracy on training data): {default_score:.3f}")

# Important Note
print("Default C value = 1. Regularization controls overfitting. Higher C -> less regularization.")

# -----------------------------------------------------
# Step 3: Grid Search over C parameter
# -----------------------------------------------------
C_values = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2]
scores = []

logit_grid = LogisticRegression(max_iter=10000, multi_class='multinomial', solver='lbfgs')

for C_choice in C_values:
    logit_grid.set_params(C=C_choice)
    logit_grid.fit(X, y)
    score = logit_grid.score(X, y)
    scores.append(score)
    print(f"C={C_choice}: Model accuracy = {score:.3f}")

# Find best C
best_index = np.argmax(scores)
best_C = C_values[best_index]
best_score = scores[best_index]
print(f"\nBest C value: {best_C} with score: {best_score:.3f}")

# Important Note
print("\nImportant Notes:")
print("1. Grid Search evaluates different hyperparameters to optimize model performance.")
print("2. Be careful: scoring on training data can lead to overfitting. Always validate on unseen test data.")

# -----------------------------------------------------
# Step 4: Visualize the Grid Search Results
# -----------------------------------------------------
plt.figure(figsize=(8,5))
plt.plot(C_values, scores, marker='o', linestyle='-', color='blue')
plt.title("Grid Search: Logistic Regression Accuracy vs C")
plt.xlabel("C (Inverse of regularization strength)")
plt.ylabel("Training Accuracy")
plt.grid(True)
plt.axvline(best_C, color='red', linestyle='--', label=f'Best C={best_C}')
plt.legend()
plt.show()

# Important Note
print("Visualization helps understand how changing C affects model accuracy on training data.")
print("Typically, a separate validation set is used to avoid overfitting.")
