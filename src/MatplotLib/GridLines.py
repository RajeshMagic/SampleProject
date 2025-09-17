"""
Matplotlib Grid Lines Demonstration
Author: OpenAI ChatGPT

This script demonstrates:
1. Adding grid lines to a plot
2. Specifying which grid lines to display (x, y, or both)
3. Customizing grid line properties (color, linestyle, linewidth)
4. Console explanations and important notes for understanding
"""

# ---------------------------------------------------
# Import required libraries
# ---------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# Sample data
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

print("\n================= Matplotlib Grid Lines Tutorial =================\n")
print("Grid lines help in visually estimating the values of points in a plot.\n")
print("Important Note: Grids improve readability and interpretation of charts.\n")

# ---------------------------------------------------
# Example 1: Add default grid lines (both axes)
# ---------------------------------------------------
print("[Example 1] Default grid lines on both x and y axes.\n")

plt.figure(figsize=(7, 5))
plt.plot(x, y, marker='o', color='b', linestyle='-')
plt.title("Sports Watch Data with Default Grid")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid()  # Default: both x and y
plt.show()

# ---------------------------------------------------
# Example 2: Grid lines only for x-axis
# ---------------------------------------------------
print("[Example 2] Grid lines displayed only for the X-axis.\n")

plt.figure(figsize=(7, 5))
plt.plot(x, y, marker='s', color='m', linestyle='--')
plt.title("Sports Watch Data (X-axis Grid Only)")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(axis='x')  # Show grid lines only on x-axis
plt.show()

# ---------------------------------------------------
# Example 3: Grid lines only for y-axis
# ---------------------------------------------------
print("[Example 3] Grid lines displayed only for the Y-axis.\n")

plt.figure(figsize=(7, 5))
plt.plot(x, y, marker='^', color='g', linestyle='-.')
plt.title("Sports Watch Data (Y-axis Grid Only)")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(axis='y')  # Show grid lines only on y-axis
plt.show()

# ---------------------------------------------------
# Example 4: Customize grid line properties
# ---------------------------------------------------
print("[Example 4] Customized grid lines with color, linestyle, and linewidth.\n")
print("-> Grid lines can be dotted, dashed, or solid and can have any color.\n")

plt.figure(figsize=(7, 5))
plt.plot(x, y, marker='o', color='r', linestyle=':')
plt.title("Sports Watch Data with Customized Grid")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

# Customize grid lines
plt.grid(color='green', linestyle='--', linewidth=0.7)

plt.show()

# ---------------------------------------------------
# Summary
# ---------------------------------------------------
print("\n====================== Summary ======================\n")
print("1. Use plt.grid() to add grid lines to plots.")
print("2. The 'axis' parameter controls which grid lines are shown: 'x', 'y', or 'both'.")
print("3. Grid line properties can be customized using 'color', 'linestyle', and 'linewidth'.")
print("4. Grids improve readability and make data visualization easier to interpret.")
print("\n=====================================================\n")
