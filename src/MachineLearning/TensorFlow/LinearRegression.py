"""
linear_regression_demo.py
Demonstrates Linear Regression using Python, SciPy, and Matplotlib.
Author: OpenAI ChatGPT

Concepts Covered:
 - Scatter plot of raw data
 - Fitting a regression line using SciPy
 - Understanding slope, intercept, correlation coefficient (r), p-value, std_err
 - Predicting future values with regression model
 - Identifying when regression is a "bad fit"
 - Console explanations with Important Notes
"""

import matplotlib.pyplot as plt
from scipy import stats

print("\n================ LINEAR REGRESSION DEMONSTRATION ==================\n")
print("Regression helps us find relationships between variables and predict outcomes.")
print("Linear Regression fits a straight line to data points to model this relationship.\n")

# ------------------------------------------------------------
# 1) Scatter Plot of Car Data
# ------------------------------------------------------------
print("1) Example: Car Age vs Speed\n")

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]   # Car age
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]   # Car speed

print("We collected car age (years) and speed (km/h).")
print("Let's first visualize the data in a scatter plot.\n")

plt.scatter(x, y, color='blue', edgecolor='black')
plt.title("Car Age vs Speed (Scatter Plot)")
plt.xlabel("Car Age (years)")
plt.ylabel("Car Speed (km/h)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

# ------------------------------------------------------------
# 2) Fitting a Linear Regression Line
# ------------------------------------------------------------
print("2) Fitting a Linear Regression Line\n")

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(val):
    """Return predicted y for given x using regression line equation"""
    return slope * val + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y, color='blue', edgecolor='black')
plt.plot(x, mymodel, color='red')
plt.title("Linear Regression Line (Car Age vs Speed)")
plt.xlabel("Car Age (years)")
plt.ylabel("Car Speed (km/h)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

print(f"Slope     : {slope:.3f}")
print(f"Intercept : {intercept:.3f}")
print(f"r-value   : {r:.3f}")
print(f"p-value   : {p:.6f}")
print(f"Std Error : {std_err:.3f}\n")

print("Important Note:")
print(" - The slope tells us how much Y changes with X.")
print(" - The intercept is where the line crosses Y-axis.")
print(" - r is the correlation coefficient (from -1 to 1).")
print("   Here r = {:.2f}, meaning strong negative correlation.".format(r))
print(" - If |r| is near 0, regression is not reliable.\n")

# ------------------------------------------------------------
# 3) Predicting Future Values
# ------------------------------------------------------------
print("3) Predicting Future Values\n")
pred_x = 10
pred_y = myfunc(pred_x)
print(f"Predicted speed of a {pred_x}-year-old car: {pred_y:.2f} km/h\n")

# Show prediction visually
plt.scatter(x, y, color='blue', edgecolor='black')
plt.plot(x, mymodel, color='red')
plt.scatter(pred_x, pred_y, color='green', s=100, marker='X', label="Prediction")
plt.title("Prediction Example (10-year-old car)")
plt.xlabel("Car Age (years)")
plt.ylabel("Car Speed (km/h)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

# ------------------------------------------------------------
# 4) Bad Fit Example
# ------------------------------------------------------------
print("4) Bad Fit Example\n")

x_bad = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y_bad = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope_b, intercept_b, r_b, p_b, std_err_b = stats.linregress(x_bad, y_bad)

def bad_func(val):
    return slope_b * val + intercept_b

mymodel_bad = list(map(bad_func, x_bad))

plt.scatter(x_bad, y_bad, color='purple', edgecolor='black')
plt.plot(x_bad, mymodel_bad, color='orange')
plt.title("Bad Fit Example (Random Data)")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

print(f"r-value for bad fit data: {r_b:.3f}")
print("Important Note:")
print(" - Here r is close to 0, meaning almost no relationship.")
print(" - Linear regression is not suitable when variables are unrelated.")
print(" - Always check correlation before trusting regression models.\n")

# ------------------------------------------------------------
# 5) Method Explanation
# ------------------------------------------------------------
print("================ METHOD EXPLANATION =================")
print("Method used: stats.linregress(x, y)")
print("Returns: slope, intercept, r-value, p-value, std_err")
print(" - slope    : rate of change of Y w.r.t X")
print(" - intercept: Y value when X=0")
print(" - r-value  : correlation coefficient (-1 to 1)")
print(" - p-value  : probability of observing results by chance")
print(" - std_err  : standard error of the slope\n")

print("Method used: plt.scatter(x, y)")
print(" - Creates scatter plot with given x & y values")
print("Parameters: color, marker, s (size), alpha (transparency)\n")

print("Method used: plt.plot(x, model)")
print(" - Plots regression line using predicted values\n")

print("================ SUMMARY / IMPORTANT POINTS =================")
print(" - Linear Regression fits a line to data points to model relationships.")
print(" - The correlation coefficient r tells us how strong the relationship is.")
print(" - Regression can be used to predict future values (if relationship exists).")
print(" - A low r indicates poor fit: regression is unreliable in such cases.")
print(" - Always visualize data + check r before trusting predictions.")
print("============================================================\n")
