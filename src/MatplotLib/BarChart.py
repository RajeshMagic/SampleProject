"""
Matplotlib Bar Chart Tutorial
Author: OpenAI ChatGPT

This script demonstrates:
1. Basic vertical bar chart
2. Horizontal bar chart
3. Setting colors using names and hex values
4. Adjusting bar width and height
5. Console explanations and important notes
"""

# ---------------------------------------------------
# Import required libraries
# ---------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

print("\n================ Matplotlib Bar Chart Tutorial ================\n")
print("Bar charts are useful to visualize categorical data.")
print("Important Note: x values can be categories (strings) and y values are numeric.\n")

# ---------------------------------------------------
# Example 1: Basic vertical bar chart
# ---------------------------------------------------
print("[Example 1] Basic vertical bar chart.\n")
categories = np.array(["A", "B", "C", "D"])
values = np.array([3, 8, 1, 10])

plt.bar(categories, values)
plt.title("Basic Vertical Bar Chart")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()

# ---------------------------------------------------
# Example 2: Horizontal bar chart
# ---------------------------------------------------
print("[Example 2] Horizontal bar chart.\n")
plt.barh(categories, values)
plt.title("Basic Horizontal Bar Chart")
plt.xlabel("Values")
plt.ylabel("Category")
plt.show()

# ---------------------------------------------------
# Example 3: Bar colors using color names
# ---------------------------------------------------
print("[Example 3] Bar colors using names.\n")
plt.bar(categories, values, color="red")
plt.title("Vertical Bars with Red Color")
plt.show()

# Bar with "hotpink"
plt.bar(categories, values, color="hotpink")
plt.title("Vertical Bars with Hot Pink Color")
plt.show()

# ---------------------------------------------------
# Example 4: Bar colors using Hexadecimal
# ---------------------------------------------------
print("[Example 4] Bar colors using Hex values.\n")
plt.bar(categories, values, color="#4CAF50")  # Beautiful green color
plt.title("Vertical Bars with Hex Color")
plt.show()

# ---------------------------------------------------
# Example 5: Adjusting bar width
# ---------------------------------------------------
print("[Example 5] Adjust bar width (vertical bars).\n")
plt.bar(categories, values, width=0.1)  # Very thin bars
plt.title("Vertical Bars with Width=0.1")
plt.show()

# ---------------------------------------------------
# Example 6: Adjusting bar height (horizontal bars)
# ---------------------------------------------------
print("[Example 6] Adjust bar height (horizontal bars).\n")
plt.barh(categories, values, height=0.1)  # Very thin horizontal bars
plt.title("Horizontal Bars with Height=0.1")
plt.show()

# ---------------------------------------------------
# Summary
# ---------------------------------------------------
print("\n====================== Summary ======================\n")
print("1. plt.bar(x, y) creates vertical bar charts.")
print("2. plt.barh(x, y) creates horizontal bar charts.")
print("3. Use color='name' or color='#hexvalue' to set bar colors.")
print("4. Adjust vertical bars width using width parameter (default=0.8).")
print("5. Adjust horizontal bars height using height parameter (default=0.8).")
print("6. Category labels (x-axis) can be strings.\n")
print("=====================================================\n")
