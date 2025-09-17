"""
Matplotlib Subplot Tutorial
Author: OpenAI ChatGPT

This script demonstrates:
1. Displaying multiple plots in a single figure using subplot()
2. Creating different layouts: side-by-side, top-bottom, and grid
3. Adding individual titles to each subplot
4. Adding a super title to the entire figure
5. Console explanations and important notes
"""

# ---------------------------------------------------
# Import required libraries
# ---------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

print("\n================ Matplotlib Subplot Tutorial ================\n")
print("Subplots allow you to display multiple plots in a single figure.")
print("Important Note: subplot(rows, columns, index) defines layout and position.\n")

# ---------------------------------------------------
# Example 1: Two plots side by side
# ---------------------------------------------------
print("[Example 1] Two plots side by side (1 row, 2 columns).\n")

# Plot 1
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st plot
plt.plot(x1, y1, marker='o', color='b')
plt.title("SALES")

# Plot 2
x2 = np.array([0, 1, 2, 3])
y2 = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd plot
plt.plot(x2, y2, marker='s', color='r')
plt.title("INCOME")

# Super title for entire figure
plt.suptitle("MY SHOP DATA")
plt.show()

# ---------------------------------------------------
# Example 2: Two plots stacked vertically
# ---------------------------------------------------
print("[Example 2] Two plots stacked vertically (2 rows, 1 column).\n")

# Plot 1
plt.subplot(2, 1, 1)
plt.plot(x1, y1, marker='^', color='g')
plt.title("SALES")

# Plot 2
plt.subplot(2, 1, 2)
plt.plot(x2, y2, marker='*', color='m')
plt.title("INCOME")

plt.suptitle("MY SHOP DATA")
plt.show()

# ---------------------------------------------------
# Example 3: Grid layout with 6 plots
# ---------------------------------------------------
print("[Example 3] Grid layout with 2 rows and 3 columns.\n")

# Loop to create 6 plots
for i in range(6):
    plt.subplot(2, 3, i+1)  # 2 rows, 3 columns, index i+1
    y = y1 if i % 2 == 0 else y2  # Alternate y1 and y2
    plt.plot(x1, y, marker='o' if i%2==0 else 's', color='b' if i%2==0 else 'r')
    plt.title(f"Plot {i+1}")

plt.suptitle("Multiple Subplots Example")
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust layout to prevent overlap with suptitle
plt.show()

# ---------------------------------------------------
# Summary
# ---------------------------------------------------
print("\n====================== Summary ======================\n")
print("1. plt.subplot(rows, cols, index) creates multiple plots in one figure.")
print("2. Indexing starts from 1 and goes row-wise.")
print("3. Use plt.title() to add individual plot titles.")
print("4. Use plt.suptitle() to add a title for the entire figure.")
print("5. Use plt.tight_layout() to prevent overlaps between subplots and titles.")
print("\n=====================================================\n")
