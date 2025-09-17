"""
Matplotlib Histogram Tutorial
Author: OpenAI ChatGPT

This script demonstrates:
1. Basic histogram creation
2. Setting the number of bins
3. Changing colors of the histogram
4. Adjusting transparency with alpha
5. Console explanations and important notes
"""

# ---------------------------------------------------
# Import required libraries
# ---------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

print("\n================ Matplotlib Histogram Tutorial ================\n")
print("Histograms are used to visualize frequency distributions.")
print("Important Note: Each bar represents the frequency of data points in a given range (bin).\n")

# ---------------------------------------------------
# Example 1: Basic histogram
# ---------------------------------------------------
print("[Example 1] Basic histogram.\n")
# Generate a normal distribution: mean=170, std=10, n=250
data = np.random.normal(170, 10, 250)
print("Generated 250 random heights (mean=170, std=10):")
print(data[:10], "...")  # Show first 10 values for brevity

plt.hist(data)
plt.title("Basic Histogram")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.show()

# ---------------------------------------------------
# Example 2: Histogram with specified bins
# ---------------------------------------------------
print("[Example 2] Histogram with 10 bins.\n")
plt.hist(data, bins=10)
plt.title("Histogram with 10 Bins")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.show()

# ---------------------------------------------------
# Example 3: Histogram with color and transparency
# ---------------------------------------------------
print("[Example 3] Histogram with color and alpha (transparency).\n")
plt.hist(data, bins=15, color='hotpink', alpha=0.7)
plt.title("Histogram with Color and Transparency")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.show()

# ---------------------------------------------------
# Example 4: Histogram with edge color for bars
# ---------------------------------------------------
print("[Example 4] Histogram with bar edge color.\n")
plt.hist(data, bins=12, color='#4CAF50', edgecolor='black')
plt.title("Histogram with Edge Color")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.show()

# ---------------------------------------------------
# Example 5: Multiple histograms for comparison
# ---------------------------------------------------
print("[Example 5] Compare two datasets in one figure.\n")
data_day1 = np.random.normal(170, 10, 250)
data_day2 = np.random.normal(175, 12, 250)

plt.hist(data_day1, bins=15, alpha=0.5, label='Day 1')
plt.hist(data_day2, bins=15, alpha=0.5, label='Day 2')
plt.title("Comparison of Two Datasets")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# ---------------------------------------------------
# Summary
# ---------------------------------------------------
print("\n====================== Summary ======================\n")
print("1. Use plt.hist(data) to create a histogram.")
print("2. The 'bins' parameter controls the number of intervals for data.")
print("3. Use 'color' to set bar colors and 'alpha' for transparency.")
print("4. Use 'edgecolor' to outline bars for better visibility.")
print("5. Multiple histograms can be overlaid using transparency (alpha) and legend.")
print("6. Histograms are ideal to visualize data distribution and frequency.\n")
print("=====================================================\n")
