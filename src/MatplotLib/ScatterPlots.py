"""
Matplotlib Scatter Plot Tutorial
Author: OpenAI ChatGPT

This script demonstrates:
1. Basic scatter plots
2. Multiple scatter plots in the same figure
3. Setting colors (single, array, colormap)
4. Setting marker sizes
5. Using alpha transparency
6. Combining color, size, alpha, and colormap
7. Console explanations and important notes
"""

# ---------------------------------------------------
# Import required libraries
# ---------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

print("\n================ Matplotlib Scatter Plot Tutorial ================\n")
print("Scatter plots are useful to visualize the relationship between two variables.")
print("Important Note: x and y arrays must be of the same length.\n")

# ---------------------------------------------------
# Example 1: Basic scatter plot
# ---------------------------------------------------
print("[Example 1] Basic scatter plot.\n")
x1 = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y1 = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x1, y1)
plt.title("Basic Scatter Plot")
plt.xlabel("Car Age")
plt.ylabel("Speed")
plt.show()

# ---------------------------------------------------
# Example 2: Multiple scatter plots on the same figure
# ---------------------------------------------------
print("[Example 2] Two scatter plots on the same figure.\n")
x2 = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y2 = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

plt.scatter(x1, y1, color='hotpink', label='Day 1')
plt.scatter(x2, y2, color='#88c999', label='Day 2')
plt.title("Scatter Plot Comparison")
plt.xlabel("Car Age")
plt.ylabel("Speed")
plt.legend()
plt.show()

# ---------------------------------------------------
# Example 3: Scatter plot with individual colors
# ---------------------------------------------------
print("[Example 3] Color each point differently.\n")
colors = np.array(["red","green","blue","yellow","pink","black","orange",
                   "purple","beige","brown","gray","cyan","magenta"])
plt.scatter(x1, y1, c=colors)
plt.title("Scatter Plot with Individual Colors")
plt.show()

# ---------------------------------------------------
# Example 4: Scatter plot with colormap
# ---------------------------------------------------
print("[Example 4] Using a colormap.\n")
color_values = np.array([0,10,20,30,40,45,50,55,60,70,80,90,100])
plt.scatter(x1, y1, c=color_values, cmap='viridis')
plt.colorbar()  # Show the color scale
plt.title("Scatter Plot with Colormap")
plt.show()

# ---------------------------------------------------
# Example 5: Scatter plot with varying sizes
# ---------------------------------------------------
print("[Example 5] Scatter plot with different sizes.\n")
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
plt.scatter(x1, y1, s=sizes)
plt.title("Scatter Plot with Sizes")
plt.show()

# ---------------------------------------------------
# Example 6: Scatter plot with alpha transparency
# ---------------------------------------------------
print("[Example 6] Scatter plot with alpha transparency.\n")
plt.scatter(x1, y1, s=sizes, alpha=0.5)
plt.title("Scatter Plot with Alpha Transparency")
plt.show()

# ---------------------------------------------------
# Example 7: Combine color, size, alpha, and colormap
# ---------------------------------------------------
print("[Example 7] Combine color, size, alpha, and colormap.\n")
x_random = np.random.randint(100, size=100)
y_random = np.random.randint(100, size=100)
colors_random = np.random.randint(100, size=100)
sizes_random = 10 * np.random.randint(100, size=100)

plt.scatter(x_random, y_random, c=colors_random, s=sizes_random, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()  # Show the color scale
plt.title("Advanced Scatter Plot with ColorMap, Size, and Alpha")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# ---------------------------------------------------
# Summary
# ---------------------------------------------------
print("\n====================== Summary ======================\n")
print("1. plt.scatter(x, y) creates a basic scatter plot.")
print("2. Use color='name' for single color or c=array for multiple colors.")
print("3. Use cmap='colormap_name' to apply a colormap.")
print("4. Use s=array to vary the size of each marker.")
print("5. Use alpha to set transparency.")
print("6. Combine color, size, alpha, and colormap for advanced visualization.")
print("\n=====================================================\n")
