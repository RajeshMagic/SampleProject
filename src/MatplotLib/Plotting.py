"""
Matplotlib Plotting Demonstration
Author: OpenAI ChatGPT

This script demonstrates:
1. Plotting x and y points using plt.plot()
2. Plotting with only markers
3. Plotting multiple points
4. Using default x-points if not specified
5. Console explanations with 'Important Notes'
"""

# ---------------------------------------------------
# Import required modules
# ---------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

print("\n================= Matplotlib Plotting Tutorial =================\n")
print("The plot() function is used to draw points (markers) in a diagram.")
print("By default, it draws a line from one point to the next.")
print("Important Note: The first parameter is x-axis values, the second is y-axis values.\n")

# ---------------------------------------------------
# Example 1: Basic Line Plot (single line between 2 points)
# ---------------------------------------------------
print("[Example 1] Basic Line Plot")
print("-> Drawing a line between points (1,3) and (8,10).\n")

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.figure(figsize=(6, 4))
plt.plot(xpoints, ypoints, color="blue", marker="o")
plt.title("Basic Line Plot (1,3) → (8,10)")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 2: Plotting Without Line (markers only)
# ---------------------------------------------------
print("[Example 2] Plotting with only markers")
print("-> Using 'o' notation to show only the points without connecting lines.\n")

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.figure(figsize=(6, 4))
plt.plot(xpoints, ypoints, 'o', color="red")
plt.title("Markers Only Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 3: Multiple Points
# ---------------------------------------------------
print("[Example 3] Plotting Multiple Points")
print("-> Drawing a line through points (1,3), (2,8), (6,1), (8,10).\n")

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.figure(figsize=(6, 4))
plt.plot(xpoints, ypoints, marker="o", color="green")
plt.title("Multiple Points Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 4: Default X-Points
# ---------------------------------------------------
print("[Example 4] Default X-Points")
print("-> If only y-values are given, x-values are automatically assigned as [0,1,2,...].")
print("-> Here y = [3, 8, 1, 10, 5, 7]. So x will default to [0, 1, 2, 3, 4, 5].\n")

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.figure(figsize=(6, 4))
plt.plot(ypoints, marker="o", color="purple")
plt.title("Default X-Points Example")
plt.xlabel("Default X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Conclusion
# ---------------------------------------------------
print("\n====================== Summary ======================\n")
print("1. plot(x, y) is the fundamental function for drawing lines in Matplotlib.")
print("2. Passing only y-values makes x default to [0, 1, 2, ...].")
print("3. Shortcut strings like 'o' can be used for markers-only plots.")
print("4. You can connect multiple points with a single line by passing arrays of x and y values.")
print("5. The x-axis is always horizontal, and the y-axis is vertical.\n")
print("Important Note: These are the foundational plotting concepts you need before exploring markers, colors, and line styles in detail.\n")
print("=====================================================\n")
