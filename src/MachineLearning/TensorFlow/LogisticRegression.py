# Machine Learning - Logistic Regression Demonstration
# -----------------------------------------------------
# This script demonstrates:
#   - Creating a dataset for binary classification
#   - Fitting a Logistic Regression model
#   - Predicting class labels
#   - Calculating odds and probabilities
#   - Visualizing logistic regression curve
# -----------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# -----------------------------------------------------
# Step 1: Create dataset
# -----------------------------------------------------
# X represents tumor sizes (cm), y represents binary outcome (0=Non-cancerous, 1=Cancerous)
X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

print("\n--- Step 1: Dataset ---")
for i in range(len(X)):
    print(f"Tumor size: {X[i][0]} cm -> Cancerous: {y[i]}")

# Important Note
print("\nImportant Note: Logistic Regression is used for classification, predicting categorical outcomes.")

# -----------------------------------------------------
# Step 2: Fit Logistic Regression model
# -----------------------------------------------------
logr = LogisticRegression()
logr.fit(X, y)

print("\n--- Step 2: Model Coefficient & Intercept ---")
print(f"Coefficient (log-odds change per cm): {logr.coef_[0][0]}")
print(f"Intercept: {logr.intercept_[0]}")

# -----------------------------------------------------
# Step 3: Predict a new observation
# -----------------------------------------------------
new_tumor = np.array([3.46]).reshape(-1, 1)
predicted_class = logr.predict(new_tumor)
print(f"\n--- Step 3: Prediction ---")
print(f"Predicted class for tumor size {new_tumor[0][0]} cm: {predicted_class[0]}")

# -----------------------------------------------------
# Step 4: Calculate odds and probability for each observation
# -----------------------------------------------------
def logit2prob(model, X):
    """
    Convert log-odds from logistic regression to probability.
    """
    log_odds = model.coef_ * X + model.intercept_
    odds = np.exp(log_odds)
    probability = odds / (1 + odds)
    return probability

probabilities = logit2prob(logr, X)
print("\n--- Step 4: Probability for each tumor ---")
for i, prob in enumerate(probabilities):
    print(f"Tumor size: {X[i][0]} cm -> Probability cancerous: {prob[0]:.2f}")

# Important Note
print("\nImportant Note: The probability is derived from the logistic function: p = odds / (1 + odds)")

# -----------------------------------------------------
# Step 5: Visualize Logistic Regression curve
# -----------------------------------------------------
# Generate a range of tumor sizes for smooth curve
X_range = np.linspace(0, 7, 300).reshape(-1, 1)
y_prob = logit2prob(logr, X_range)

plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X_range, y_prob, color='red', linewidth=2, label='Logistic Regression Curve')
plt.title("Logistic Regression - Tumor Size vs Cancer Probability")
plt.xlabel("Tumor Size (cm)")
plt.ylabel("Probability of Cancer")
plt.legend()
plt.grid(True)
plt.show()

# Important Notes for Understanding:
print("\nImportant Notes:")
print("1. Logistic Regression outputs probabilities (0 to 1) instead of continuous values.")
print("2. Threshold of 0.5 is commonly used for binary classification.")
print("3. Coefficient represents change in log-odds per unit increase in X.")
print("4. Visualization helps understand how tumor size affects probability of being cancerous.")
