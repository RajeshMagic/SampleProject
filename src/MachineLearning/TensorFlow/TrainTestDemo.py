# Machine Learning - Train/Test Demonstration
# Author: Training Script
# -------------------------------------------------
# This script demonstrates:
#   - Splitting a dataset into training and testing sets
#   - Fitting a polynomial regression model
#   - Evaluating the model using R-squared (R²)
#   - Predicting new values using the trained model
#   - Visualizing data and regression lines
# -------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# -------------------------------------------------
# Step 1: Generate Random Data
# -------------------------------------------------
# Seed for reproducibility
np.random.seed(2)

# x: minutes before making a purchase
x = np.random.normal(3, 1, 100)

# y: amount of money spent divided by x (to simulate dependency)
y = np.random.normal(150, 40, 100) / x

print("\n--- Step 1: Sample Data ---")
print("First 5 x values:", x[:5])
print("First 5 y values:", y[:5])

# Visualize full dataset
plt.scatter(x, y)
plt.xlabel("Minutes in Shop")
plt.ylabel("Money Spent ($)")
plt.title("Customer Spend vs Time in Shop")
plt.show()

# -------------------------------------------------
# Step 2: Split into Training and Testing Sets
# -------------------------------------------------
train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

print("\n--- Step 2: Split Data ---")
print(f"Training set size: {len(train_x)}")
print(f"Testing set size: {len(test_x)}")

# Visualize training set
plt.scatter(train_x, train_y, color='blue')
plt.xlabel("Minutes in Shop")
plt.ylabel("Money Spent ($)")
plt.title("Training Set")
plt.show()

# Visualize testing set
plt.scatter(test_x, test_y, color='green')
plt.xlabel("Minutes in Shop")
plt.ylabel("Money Spent ($)")
plt.title("Testing Set")
plt.show()

# -------------------------------------------------
# Step 3: Fit Polynomial Regression (Degree 4)
# -------------------------------------------------
mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))

# Generate smooth line for plotting
myline = np.linspace(min(x)-1, max(x)+1, 100)

plt.scatter(train_x, train_y, color='blue', label='Training Data')
plt.plot(myline, mymodel(myline), color='red', label='Polynomial Regression Line')
plt.xlabel("Minutes in Shop")
plt.ylabel("Money Spent ($)")
plt.title("Polynomial Regression Fit on Training Data")
plt.legend()
plt.show()

# -------------------------------------------------
# Step 4: Evaluate Model with R² Score
# -------------------------------------------------
r2_train = r2_score(train_y, mymodel(train_x))
r2_test = r2_score(test_y, mymodel(test_x))

print("\n--- Step 4: Evaluate Model ---")
print(f"R² Score on Training Set: {r2_train:.3f}  (Closer to 1 = good fit)")
print(f"R² Score on Testing Set: {r2_test:.3f}   (Closer to 1 = good generalization)")

# Important Note
print("\nImportant Note:")
print("1. R² measures how well the model explains the variance in data.")
print("2. A high training R² with similar testing R² indicates low overfitting.")
print("3. Large discrepancy between train and test R² may indicate overfitting or underfitting.")

# -------------------------------------------------
# Step 5: Predict New Values
# -------------------------------------------------
minutes_in_shop = 5
predicted_spend = mymodel(minutes_in_shop)

print("\n--- Step 5: Predict Future Values ---")
print(f"Predicted money spent for a customer staying {minutes_in_shop} minutes: ${predicted_spend:.2f}")

# Visualize prediction on graph
plt.scatter(x, y, color='grey', alpha=0.5, label='All Data')
plt.scatter(minutes_in_shop, predicted_spend, color='orange', s=100, label='Predicted Value')
plt.plot(myline, mymodel(myline), color='red', label='Polynomial Regression Line')
plt.xlabel("Minutes in Shop")
plt.ylabel("Money Spent ($)")
plt.title("Prediction Example")
plt.legend()
plt.show()

# -------------------------------------------------
# Step 6: Summary
# -------------------------------------------------
print("\n--- Step 6: Summary ---")
print("1. We split the data into 80% training and 20% testing sets.")
print("2. Fitted a 4th-degree polynomial regression to training data.")
print("3. Evaluated model using R² score to measure goodness of fit.")
print("4. Predicted future value for a new input and visualized it.")
print("5. Visualized both original and scaled data for understanding.")
