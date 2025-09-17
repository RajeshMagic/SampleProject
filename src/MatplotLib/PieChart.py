"""
Matplotlib Pie Chart Tutorial
Author: OpenAI ChatGPT

This script demonstrates:
1. Basic pie chart creation
2. Adding labels
3. Changing the start angle
4. Exploding wedges
5. Adding shadow
6. Custom colors
7. Adding legends and legend titles
8. Console explanations and important notes
"""

# ---------------------------------------------------
# Import required libraries
# ---------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

print("\n================ Matplotlib Pie Chart Tutorial ================\n")
print("Pie charts are used to represent proportions of categories in a dataset.")
print("Important Note: Each wedge's size is proportional to its value relative to the sum of all values.\n")

# ---------------------------------------------------
# Example 1: Basic pie chart
# ---------------------------------------------------
print("[Example 1] Basic pie chart.\n")
y = np.array([35, 25, 25, 15])
print("Data for pie chart:", y)

plt.pie(y)
plt.title("Basic Pie Chart")
plt.show()

# ---------------------------------------------------
# Example 2: Pie chart with labels
# ---------------------------------------------------
print("[Example 2] Pie chart with labels.\n")
labels = ["Apples", "Bananas", "Cherries", "Dates"]
print("Labels:", labels)

plt.pie(y, labels=labels)
plt.title("Pie Chart with Labels")
plt.show()

# ---------------------------------------------------
# Example 3: Start angle
# ---------------------------------------------------
print("[Example 3] Pie chart with start angle 90 degrees.\n")
plt.pie(y, labels=labels, startangle=90)
plt.title("Pie Chart Starting at 90°")
plt.show()

# ---------------------------------------------------
# Example 4: Explode (pull out a wedge)
# ---------------------------------------------------
print("[Example 4] Exploding the 'Apples' wedge.\n")
explode = [0.2, 0, 0, 0]
plt.pie(y, labels=labels, explode=explode)
plt.title("Pie Chart with Exploded Wedge")
plt.show()

# ---------------------------------------------------
# Example 5: Shadow
# ---------------------------------------------------
print("[Example 5] Adding shadow to the pie chart.\n")
plt.pie(y, labels=labels, explode=explode, shadow=True)
plt.title("Pie Chart with Shadow")
plt.show()

# ---------------------------------------------------
# Example 6: Custom colors
# ---------------------------------------------------
print("[Example 6] Custom colors for each wedge.\n")
colors = ["black", "hotpink", "blue", "#4CAF50"]
plt.pie(y, labels=labels, colors=colors)
plt.title("Pie Chart with Custom Colors")
plt.show()

# ---------------------------------------------------
# Example 7: Adding a legend
# ---------------------------------------------------
print("[Example 7] Pie chart with legend.\n")
plt.pie(y, labels=labels)
plt.legend()
plt.title("Pie Chart with Legend")
plt.show()

# ---------------------------------------------------
# Example 8: Legend with a title/header
# ---------------------------------------------------
print("[Example 8] Pie chart with legend and legend title.\n")
plt.pie(y, labels=labels)
plt.legend(title="Four Fruits:")
plt.title("Pie Chart with Legend Header")
plt.show()

# ---------------------------------------------------
# Summary
# ---------------------------------------------------
print("\n====================== Summary ======================\n")
print("1. Use plt.pie(values) to create a basic pie chart.")
print("2. Use 'labels' to add category names to wedges.")
print("3. 'startangle' rotates the first wedge from the x-axis.")
print("4. 'explode' pulls out selected wedges for emphasis.")
print("5. 'shadow=True' adds a shadow effect to the chart.")
print("6. 'colors' parameter can set individual wedge colors using names or hex codes.")
print("7. Use plt.legend() to add a legend; title parameter adds a header.")
print("Pie charts are ideal for visualizing proportions in a dataset.\n")
print("=====================================================\n")
