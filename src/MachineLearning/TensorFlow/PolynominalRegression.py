"""
polynomial_regression_demo.py
Demonstrates Polynomial Regression using Python, NumPy, Matplotlib, and Sklearn.
Author: OpenAI ChatGPT

Concepts Covered:
 - Scatter plot of raw data
 - Polynomial regression model using numpy.polyfit() and numpy.poly1d()
 - Evaluating model fit using R-squared (r2_score from sklearn)
 - Predicting future values
 - Identifying bad fits with low R²
 - Console explanations with Important Notes
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

print("\n================ POLYNOMIAL REGRESSION DEMONSTRATION ==================\n")
print("Polynomial Regression fits a curved line (polynomial) to data points.")
print("It is useful when data does not follow a straight-line relationship.\n")

# ------------------------------------------------------------
# 1) Scatter Plot of Car Speed Data
# ------------------------------------------------------------
print("1) Example: Car Speed vs Time of Day (hours)\n")

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]   # Hours of the day
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]   # Speed

print("We collected car speed at different hours of the day.")
print("Let's first visualize the raw data in a scatter plot.\n")

plt.scatter(x, y, color='blue', edgecolor='black')
plt.title("Car Speed vs Time of Day (Scatter Plot)")
plt.xlabel("Hour of the Day")
plt.ylabel("Car Speed (km/h)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

# ------------------------------------------------------------
# 2) Polynomial Regression Fit
# ------------------------------------------------------------
print("2) Polynomial Regression Curve (Degree 3)\n")

mymodel = np.poly1d(np.polyfit(x, y, 3))   # Fit cubic polynomial
myline = np.linspace(1, 22, 100)          # Line for smooth curve

plt.scatter(x, y, color='blue', edgecolor='black')
plt.plot(myline, mymodel(myline), color='red')
plt.title("Polynomial Regression (Degree 3)")
plt.xlabel("Hour of the Day")
plt.ylabel("Car Speed (km/h)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

print("Important Note:")
print(" - np.polyfit(x, y, degree) fits a polynomial curve of chosen degree.")
print(" - np.poly1d() creates a model function we can use for predictions.\n")

# ------------------------------------------------------------
# 3) Evaluating the Fit using R²
# ------------------------------------------------------------
print("3) Evaluating the Fit with R-squared (R²)\n")

r2 = r2_score(y, mymodel(x))
print(f"R² score: {r2:.3f}\n")

print("Important Note:")
print(" - R² ranges from 0 to 1.")
print(" - R² = 1 means perfect fit, R² = 0 means no relationship.")
print(f" - Here R² = {r2:.2f}, showing a very good fit.\n")

# ------------------------------------------------------------
# 4) Predicting Future Values
# ------------------------------------------------------------
print("4) Predicting Future Values\n")

pred_x = 17
pred_y = mymodel(pred_x)
print(f"Predicted speed of a car passing at {pred_x}:00 = {pred_y:.2f} km/h\n")

plt.scatter(x, y, color='blue', edgecolor='black')
plt.plot(myline, mymodel(myline), color='red')
plt.scatter(pred_x, pred_y, color='green', s=100, marker='X', label="Prediction")
plt.title("Prediction Example (Polynomial Regression)")
plt.xlabel("Hour of the Day")
plt.ylabel("Car Speed (km/h)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

print("Important Note:")
print(" - Once fitted, the polynomial model can be used to predict future values.")
print(" - Always check R² before trusting predictions.\n")

# ------------------------------------------------------------
# 5) Bad Fit Example
# ------------------------------------------------------------
print("5) Bad Fit Example\n")

x_bad = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y_bad = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel_bad = np.poly1d(np.polyfit(x_bad, y_bad, 3))
myline_bad = np.linspace(2, 95, 100)

plt.scatter(x_bad, y_bad, color='purple', edgecolor='black')
plt.plot(myline_bad, mymodel_bad(myline_bad), color='orange')
plt.title("Bad Fit Example (Polynomial Regression)")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

r2_bad = r2_score(y_bad, mymodel_bad(x_bad))
print(f"R² score for bad fit data: {r2_bad:.3f}\n")

print("Important Note:")
print(" - A very low R² indicates the model is not a good fit.")
print(" - For this dataset, R² ≈ 0, so polynomial regression is unreliable.\n")

# ------------------------------------------------------------
# 6) Method Explanation
# ------------------------------------------------------------
print("================ METHOD EXPLANATION =================")
print("Method used: numpy.polyfit(x, y, degree)")
print(" - Fits a polynomial curve of given degree to x, y data.\n")

print("Method used: numpy.poly1d(coeffs)")
print(" - Creates a polynomial function model from coefficients.\n")

print("Method used: numpy.linspace(start, stop, num)")
print(" - Generates evenly spaced values for plotting smooth curve.\n")

print("Method used: sklearn.metrics.r2_score(y_true, y_pred)")
print(" - Calculates R² score to evaluate fit quality.\n")

print("================ SUMMARY / IMPORTANT POINTS =================")
print(" - Polynomial Regression fits curved data patterns better than Linear Regression.")
print(" - Always evaluate the model using R² before trusting predictions.")
print(" - A good R² (close to 1) means reliable model; low R² means poor fit.")
print(" - Use polyfit() + poly1d() for creating and using polynomial models.")
print("============================================================\n")
