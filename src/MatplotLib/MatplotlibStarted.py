"""
Matplotlib Getting Started Demonstration
Author: OpenAI ChatGPT

This script demonstrates:
1. How to install Matplotlib
2. How to import Matplotlib
3. How to check the version
4. Examples of visualization methods with explanations
"""

# ---------------------------------------------------
# Installation Instructions (Printed to Console)
# ---------------------------------------------------
print("\n================= Matplotlib Getting Started =================\n")
print("Installation Instructions:")
print("If Python and PIP are installed, use the following command in your terminal:")
print("   C:\\Users\\YourName> pip install matplotlib")
print("\nImportant Note: If this fails, use a distribution like Anaconda or Spyder that includes Matplotlib by default.\n")

# ---------------------------------------------------
# Importing Matplotlib
# ---------------------------------------------------
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print("Matplotlib has been successfully imported.")
print("You can now use it for data visualization.\n")

# ---------------------------------------------------
# Checking Version
# ---------------------------------------------------
print("Checking Matplotlib Version:")
print("Important Note: '__version__' has TWO underscores before and after the word 'version'.")
print(f"Installed Matplotlib Version: {matplotlib.__version__}\n")

# ---------------------------------------------------
# Example 1: Basic Line Plot
# ---------------------------------------------------
print("[Example 1] Basic Line Plot using plt.plot()")
print("-> A simple line graph showing y = 2x for values 0 to 10.\n")

x = np.arange(0, 11)
y = 2 * x

plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', color='blue', label="y = 2x")
plt.title("Basic Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 2: Bar Chart
# ---------------------------------------------------
print("[Example 2] Bar Chart using plt.bar()")
print("-> A bar chart comparing categories with numeric values.\n")

categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
values = [12, 25, 8, 15]

plt.figure(figsize=(6, 4))
plt.bar(categories, values, color=['red', 'yellow', 'pink', 'brown'])
plt.title("Fruit Count - Bar Chart")
plt.xlabel("Fruit Type")
plt.ylabel("Count")
plt.show()

# ---------------------------------------------------
# Example 3: Scatter Plot
# ---------------------------------------------------
print("[Example 3] Scatter Plot using plt.scatter()")
print("-> A scatter plot is useful to show relationship between two variables.\n")

np.random.seed(42)
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

plt.figure(figsize=(6, 4))
plt.scatter(x_scatter, y_scatter, color='green', edgecolors='black')
plt.title("Random Scatter Plot")
plt.xlabel("Random X")
plt.ylabel("Random Y")
plt.show()

# ---------------------------------------------------
# Example 4: Histogram
# ---------------------------------------------------
print("[Example 4] Histogram using plt.hist()")
print("-> A histogram shows the distribution of data values.\n")

data = np.random.randn(500)  # 500 normally distributed values

plt.figure(figsize=(6, 4))
plt.hist(data, bins=20, color='skyblue', edgecolor='black')
plt.title("Histogram - Normal Distribution")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()

# ---------------------------------------------------
# Conclusion
# ---------------------------------------------------
print("\n====================== Summary ======================\n")
print("1. Matplotlib installation is easy via pip, or you can use Anaconda/Spyder.")
print("2. Import it in Python using 'import matplotlib' and 'import matplotlib.pyplot as plt'.")
print("3. Check version with: matplotlib.__version__")
print("4. Demonstrated methods include:")
print("   - plt.plot()  -> Line graphs")
print("   - plt.bar()   -> Bar charts")
print("   - plt.scatter()-> Scatter plots")
print("   - plt.hist()  -> Histograms\n")
print("Important Note: Matplotlib is foundational in Python for data visualization and integrates seamlessly with NumPy and Pandas.\n")
print("=====================================================\n")
