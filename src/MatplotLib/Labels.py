"""
Matplotlib Labels and Title Demonstration
Author: OpenAI ChatGPT

This script demonstrates:
1. Adding x-axis and y-axis labels
2. Adding a title to the plot
3. Setting font properties for labels and title using fontdict
4. Positioning the title (left, center, right)
"""

# ---------------------------------------------------
# Importing required libraries
# ---------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# Sample data
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

print("\n================= Matplotlib Labels and Title Tutorial =================\n")
print("We can use xlabel(), ylabel(), and title() to add descriptive text to plots.\n")
print("Important Note: Labels and titles make plots easier to understand and interpret.\n")

# ---------------------------------------------------
# Example 1: Adding basic labels
# ---------------------------------------------------
print("[Example 1] Adding basic labels to X and Y axes.\n")

plt.figure(figsize=(6, 4))
plt.plot(x, y)
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.title("Basic Label Example")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 2: Adding a title along with labels
# ---------------------------------------------------
print("[Example 2] Adding a TITLE along with X and Y axis labels.\n")

plt.figure(figsize=(6, 4))
plt.plot(x, y)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 3: Custom font properties using fontdict
# ---------------------------------------------------
print("[Example 3] Customizing fonts using the fontdict parameter.\n")
print("-> You can change font family, color, and size.\n")

# Define font styles
font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

plt.figure(figsize=(7, 5))
plt.plot(x, y)
plt.title("Sports Watch Data", fontdict=font1)
plt.xlabel("Average Pulse", fontdict=font2)
plt.ylabel("Calorie Burnage", fontdict=font2)
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 4: Positioning the title
# ---------------------------------------------------
print("[Example 4] Positioning the TITLE using loc parameter.\n")
print("-> Options are 'left', 'center' (default), and 'right'.\n")

# Title positioned to the left
plt.figure(figsize=(7, 5))
plt.plot(x, y)
plt.title("Sports Watch Data (Left Title)", loc='left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(True)
plt.show()

# Title positioned to the right
plt.figure(figsize=(7, 5))
plt.plot(x, y)
plt.title("Sports Watch Data (Right Title)", loc='right')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Conclusion
# ---------------------------------------------------
print("\n====================== Summary ======================\n")
print("1. xlabel() and ylabel() add text to the X and Y axes.")
print("2. title() adds a main title to the plot.")
print("3. fontdict can be used to customize fonts (family, color, size).")
print("4. loc parameter positions the title (left, center, right).")
print("\nImportant Note: Proper labeling improves the readability of your data visualization.\n")
print("=====================================================\n")
