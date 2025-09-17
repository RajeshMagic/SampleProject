"""
Matplotlib Demonstration Script
Author: OpenAI ChatGPT

This script demonstrates:
1. What Matplotlib is
2. Who created it
3. Open source nature and languages involved
4. Where the codebase is located
5. Examples of methods & visualization using Matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------
# Console Introduction
# ---------------------------------------------------
print("\n====================== Matplotlib Tutorial ======================\n")

print("What is Matplotlib?")
print("-> Matplotlib is a low-level graph plotting library in Python that serves as a visualization utility.\n")

print("Who created Matplotlib?")
print("-> It was created by John D. Hunter.\n")

print("Is Matplotlib free to use?")
print("-> Yes! Matplotlib is open-source and freely available under a permissive license.\n")

print("What languages are used in Matplotlib?")
print("-> It is mostly written in Python, with some parts in C, Objective-C, and JavaScript for platform compatibility.\n")

print("Where is the Matplotlib codebase?")
print("-> You can find it on GitHub at: https://github.com/matplotlib/matplotlib\n")

print("==============================================================\n")
print("Important Note: Let's now explore Matplotlib in action with examples!\n")

# ---------------------------------------------------
# Example 1: Basic Line Plot
# ---------------------------------------------------
x = np.linspace(0, 10, 100)
y = np.sin(x)

print("\n[Example 1] Basic Line Plot using plt.plot()")
print("-> We will plot a simple sine wave using Matplotlib.")
plt.figure(figsize=(6, 4))
plt.plot(x, y, label="Sine Wave", color="blue")
plt.title("Basic Line Plot - Sine Wave")
plt.xlabel("X values")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 2: Multiple Plots with different styles
# ---------------------------------------------------
y_cos = np.cos(x)

print("\n[Example 2] Multiple Plots with Different Styles")
print("-> Plotting both sine and cosine curves on the same figure with legends.")
plt.figure(figsize=(6, 4))
plt.plot(x, y, 'r-', label="Sine")  # red solid line
plt.plot(x, y_cos, 'g--', label="Cosine")  # green dashed line
plt.title("Sine vs Cosine")
plt.xlabel("X values")
plt.ylabel("Function values")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 3: Bar Chart
# ---------------------------------------------------
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 40]

print("\n[Example 3] Bar Chart using plt.bar()")
print("-> Bar charts are used to compare categories.")
plt.figure(figsize=(6, 4))
plt.bar(categories, values, color=['red', 'green', 'blue', 'purple'])
plt.title("Category Comparison - Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# ---------------------------------------------------
# Example 4: Scatter Plot
# ---------------------------------------------------
np.random.seed(42)
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

print("\n[Example 4] Scatter Plot using plt.scatter()")
print("-> Scatter plots are useful for showing relationships between variables.")
plt.figure(figsize=(6, 4))
plt.scatter(x_scatter, y_scatter, color='orange', marker='o', edgecolors='black')
plt.title("Random Scatter Plot")
plt.xlabel("Random X")
plt.ylabel("Random Y")
plt.show()

# ---------------------------------------------------
# Example 5: Histogram
# ---------------------------------------------------
data = np.random.randn(1000)  # 1000 normally distributed points

print("\n[Example 5] Histogram using plt.hist()")
print("-> Histograms show distribution of data.")
plt.figure(figsize=(6, 4))
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title("Histogram - Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# ---------------------------------------------------
# Conclusion
# ---------------------------------------------------
print("\n====================== Summary ======================\n")
print("1. Matplotlib is a versatile, open-source plotting library created by John D. Hunter.")
print("2. It is widely used for 2D and 3D plotting in Python.")
print("3. Source code available at: https://github.com/matplotlib/matplotlib")
print("4. We demonstrated several methods:")
print("   - plt.plot() for line graphs")
print("   - plt.bar() for bar charts")
print("   - plt.scatter() for scatter plots")
print("   - plt.hist() for histograms\n")
print("Important Note: Matplotlib is foundational in Python data science and is often used together with libraries like NumPy and Pandas for rich data visualizations.\n")
print("=====================================================\n")
