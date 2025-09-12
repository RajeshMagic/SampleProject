"""
Seaborn Tutorial Example
========================
Topic: Visualizing Distributions with Seaborn
Libraries Used: seaborn (built on top of matplotlib), matplotlib
--------------------------------------------------------------

Concepts Demonstrated:
1. Installing and importing seaborn
2. Creating a simple distribution plot (histogram style)
3. Creating a KDE (Kernel Density Estimation) distribution plot
4. Showing differences between histogram-based and KDE-based visualizations

IMPORTANT NOTE:
- sns.displot() is a powerful function for visualizing distributions.
- By default, it shows a histogram of data.
- With kind="kde", it shows a smooth curve (density function).
"""

# Step 1: Import required libraries
import matplotlib.pyplot as plt
import seaborn as sns

print("===== Seaborn Distribution Plot Tutorial =====\n")

# Step 2: Example 1 - Basic Distribution Plot (Histogram)
print("Example 1: Basic Distribution Plot (Histogram Style)")
print("----------------------------------------------------")
print("We are plotting values [0, 1, 2, 3, 4, 5] using sns.displot().")
print("This will show how frequently each value occurs.")
print("Important Note: By default, displot creates a histogram.\n")

# Create histogram
sns.displot([0, 1, 2, 3, 4, 5])
plt.title("Histogram of [0, 1, 2, 3, 4, 5]")
plt.show()


# Step 3: Example 2 - KDE (Kernel Density Estimation) Distribution Plot
print("Example 2: KDE (Kernel Density Estimation) Plot")
print("------------------------------------------------")
print("Here we use the same values [0, 1, 2, 3, 4, 5] but with kind='kde'.")
print("This shows a smooth probability density curve instead of bars.")
print("Important Note: KDE plots are useful when you want to visualize the 'shape' of data distribution.\n")

# Create KDE plot
sns.displot([0, 1, 2, 3, 4, 5], kind="kde")
plt.title("KDE Plot of [0, 1, 2, 3, 4, 5]")
plt.show()


# Step 4: Random Distribution Example (Optional Expansion)
import numpy as np

print("Example 3: Random Distribution with KDE")
print("---------------------------------------")
print("Now let's generate a random distribution using numpy (1000 random numbers).")
print("We use sns.displot(arr, kind='kde') to visualize its probability density curve.\n")

# Generate random numbers from normal distribution
arr = np.random.randn(1000)   # 1000 random numbers from a normal distribution

sns.displot(arr, kind="kde")
plt.title("KDE Plot of 1000 Random Numbers (Normal Distribution)")
plt.show()

print("===== End of Tutorial =====")
print("Important Point Recap:")
print("1. sns.displot() by default shows histogram.")
print("2. sns.displot(..., kind='kde') shows a smooth density curve.")
print("3. KDE is better for understanding the overall distribution shape,")
print("   while histogram shows frequency counts.")
