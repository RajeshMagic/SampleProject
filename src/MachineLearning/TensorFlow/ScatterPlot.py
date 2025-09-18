"""
scatter_plot_demo.py
Demonstrates Scatter Plots in Machine Learning & Data Visualization
Author: OpenAI ChatGPT

Concepts Covered:
 - Scatter plot basics with real data (car ages vs speeds)
 - Interpreting scatter plots
 - Scatter plots with random data (using NumPy normal distribution)
 - Visualization of patterns and spreads
 - Important Notes explained in console output
"""

import numpy as np
import matplotlib.pyplot as plt

print("\n================ SCATTER PLOT DEMONSTRATION ==================\n")
print("A scatter plot represents values from two arrays as points (dots) on a plane.")
print("It is useful for detecting relationships/correlations between two variables.\n")

# ------------------------------------------------------------
# 1) Scatter Plot with Car Data
# ------------------------------------------------------------
print("1) Example with Car Data:")
print(" - X-axis: Age of car (years)")
print(" - Y-axis: Speed of car (km/h)")
print("We want to see if newer cars are faster than older ones.\n")

# Data
x_car = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y_speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Visualization
plt.scatter(x_car, y_speed, color='blue', marker='o', s=80, edgecolor='black')
plt.title("Car Age vs Speed (Scatter Plot)")
plt.xlabel("Car Age (years)")
plt.ylabel("Car Speed (km/h)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print("Observation from plot:")
print(" - Two fastest cars were both 2 years old.")
print(" - Slowest car was 12 years old.")
print(" - It seems newer cars tend to be faster, but with only 13 data points,")
print("   this might just be coincidence.\n")

# ------------------------------------------------------------
# 2) Scatter Plot with Random Data
# ------------------------------------------------------------
print("2) Example with Randomly Generated Data:")
print(" - When testing algorithms, we may not have real-world data.")
print(" - Instead, we can generate random data using NumPy.")
print(" - Here we create 1000 values for X and Y, sampled from Normal distributions.\n")

# Random data: Normal distribution
x_random = np.random.normal(5.0, 1.0, 1000)   # mean=5, std=1
y_random = np.random.normal(10.0, 2.0, 1000)  # mean=10, std=2

# Visualization
plt.scatter(x_random, y_random, color='green', alpha=0.5, s=30)
plt.title("Random Data (Scatter Plot) from Normal Distribution")
plt.xlabel("X values ~ N(5,1)")
plt.ylabel("Y values ~ N(10,2)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print("Observation from random data scatter plot:")
print(" - Dots are concentrated near (x≈5, y≈10).")
print(" - Spread along Y-axis is wider because std dev = 2 vs std dev = 1 for X.")
print(" - This illustrates how data distributions influence scatter plots.\n")

# ------------------------------------------------------------
# 3) Method Demonstration & Notes
# ------------------------------------------------------------
print("3) Method Demonstration:")
print("The Matplotlib method used here is plt.scatter(x, y, ...).")
print("Important parameters:")
print(" - x, y : arrays of same length, values to plot")
print(" - color : point color (e.g., 'blue', 'green')")
print(" - marker : shape of point (e.g., 'o', 'x', '^')")
print(" - s : size of points")
print(" - alpha : transparency (0 to 1)\n")

print("================ SUMMARY / IMPORTANT NOTES =================")
print(" - Scatter plots show how two variables relate to each other.")
print(" - They help detect correlations, clusters, and outliers.")
print(" - With few data points, trends may be misleading (like car dataset).")
print(" - With many data points (random example), patterns become clearer.")
print(" - plt.scatter() is the key method for creating scatter plots in Matplotlib.")
print("============================================================\n")
