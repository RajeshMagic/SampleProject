"""
Matplotlib Pyplot Demonstration
Author: OpenAI ChatGPT

This script demonstrates:
1. What Pyplot is and why it is commonly imported as 'plt'
2. A simple line plot example (from (0,0) to (6,250))
3. Additional method examples (multiple lines, styles, labels, grid)
4. Clear console outputs with 'Important Notes'
"""

# ---------------------------------------------------
# Importing Required Modules
# ---------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

print("\n================= Matplotlib Pyplot Tutorial =================\n")
print("What is Pyplot?")
print("-> Pyplot is a submodule of Matplotlib that provides a simple interface for plotting.")
print("-> It is usually imported as 'plt': import matplotlib.pyplot as plt\n")
print("Important Note: 'plt' is a commonly used alias, making the syntax concise.\n")

# ---------------------------------------------------
# Example 1: Basic Line Plot (from problem statement)
# ---------------------------------------------------
print("[Example 1] Basic Line Plot using plt.plot()")
print("-> Drawing a line from (0,0) to (6,250).\n")

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.figure(figsize=(6, 4))
plt.plot(xpoints, ypoints, color="blue", marker="o")
plt.title("Basic Line Plot (0,0) → (6,250)")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 2: Plotting Multiple Lines
# ---------------------------------------------------
print("[Example 2] Plotting Multiple Lines")
print("-> Here we plot y = x and y = x^2 on the same graph for comparison.\n")

x = np.linspace(0, 10, 100)
y1 = x
y2 = x**2

plt.figure(figsize=(6, 4))
plt.plot(x, y1, label="y = x", color="green")
plt.plot(x, y2, label="y = x^2", color="red")
plt.title("Multiple Line Plot")
plt.xlabel("X Values")
plt.ylabel("Function Values")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 3: Customizing Line Style
# ---------------------------------------------------
print("[Example 3] Customizing Line Style")
print("-> Different line styles (solid, dashed, dotted) can be used with Pyplot.\n")

plt.figure(figsize=(6, 4))
plt.plot(x, np.sin(x), 'b-', label="Solid Line")
plt.plot(x, np.cos(x), 'g--', label="Dashed Line")
plt.plot(x, np.tan(x), 'r:', label="Dotted Line")
plt.ylim(-5, 5)  # Limit y-axis for tangent
plt.title("Line Styles in Pyplot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 4: Markers and Colors
# ---------------------------------------------------
print("[Example 4] Using Markers and Colors")
print("-> Markers help highlight data points on a line.\n")

x_markers = np.array([1, 2, 3, 4, 5])
y_markers = np.array([2, 4, 6, 8, 10])

plt.figure(figsize=(6, 4))
plt.plot(x_markers, y_markers, 'o--m', label="Points with markers")
plt.title("Markers and Colors Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Conclusion
# ---------------------------------------------------
print("\n====================== Summary ======================\n")
print("1. Pyplot is the main Matplotlib submodule for easy plotting, imported as 'plt'.")
print("2. Basic line plots can be created using plt.plot(x, y).")
print("3. You can add multiple lines, customize styles, markers, and add grids & legends.")
print("4. Pyplot makes it easy to create clear, professional visualizations with minimal code.\n")
print("Important Note: Most Matplotlib tutorials and real-world examples rely heavily on Pyplot.\n")
print("=====================================================\n")
