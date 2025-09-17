"""
Machine Learning: Mean, Median, Mode Demonstration
Author: OpenAI ChatGPT

This script demonstrates:
1. How to calculate Mean, Median, and Mode using Python
2. Using NumPy and SciPy modules for calculations
3. Visualization using Matplotlib
4. Understanding the importance of these measures in Machine Learning
"""

# ---------------------------------------------------
# Import required libraries
# ---------------------------------------------------
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

print("\n================ Mean, Median, Mode Demo =================\n")
print("Important Note: Mean, Median, and Mode are fundamental statistics used in Machine Learning.")
print("They help us summarize numerical data and understand its distribution.\n")

# ---------------------------------------------------
# Step 1: Example dataset
# ---------------------------------------------------
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
print("[Step 1] Dataset (Car Speeds):")
print(speed)

# ---------------------------------------------------
# Step 2: Calculate Mean
# ---------------------------------------------------
mean_speed = np.mean(speed)
print(f"\n[Step 2] Mean (Average Speed): {mean_speed:.2f}")
print("Important: Mean is sensitive to outliers (extremely high or low values can skew it).")

# ---------------------------------------------------
# Step 3: Calculate Median
# ---------------------------------------------------
median_speed = np.median(speed)
print(f"\n[Step 3] Median (Middle Value): {median_speed}")
print("Important: Median is robust to outliers and represents the central value.")

# ---------------------------------------------------
# Step 4: Calculate Mode (Updated for SciPy >= 1.11)
# ---------------------------------------------------
mode_result = stats.mode(speed, keepdims=True)  # keepdims=True ensures .mode and .count are arrays
mode_value = mode_result.mode[0]
mode_count = mode_result.count[0]
print(f"\n[Step 4] Mode (Most Frequent Value): {mode_value} (Appears {mode_count} times)")
print("Important: Mode tells us the most common observation in the dataset.")

# ---------------------------------------------------
# Step 5: Visualizations
# ---------------------------------------------------

# 5a: Histogram
plt.hist(speed, bins=6, color='skyblue', edgecolor='black')
plt.axvline(mean_speed, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_speed:.2f}')
plt.axvline(median_speed, color='green', linestyle='dashed', linewidth=2, label=f'Median: {median_speed}')
plt.axvline(mode_value, color='orange', linestyle='dashed', linewidth=2, label=f'Mode: {mode_value}')
plt.title("Histogram of Car Speeds")
plt.xlabel("Speed")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# 5b: Boxplot
plt.boxplot(speed, patch_artist=True, boxprops=dict(facecolor='lightgreen'))
plt.title("Boxplot of Car Speeds")
plt.ylabel("Speed")
plt.show()

# 5c: Scatter Plot for distribution
plt.scatter(range(len(speed)), speed, color='purple', s=100)
plt.axhline(mean_speed, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_speed:.2f}')
plt.axhline(median_speed, color='green', linestyle='dashed', linewidth=2, label=f'Median: {median_speed}')
plt.axhline(mode_value, color='orange', linestyle='dashed', linewidth=2, label=f'Mode: {mode_value}')
plt.title("Scatter Plot of Car Speeds")
plt.xlabel("Observation Index")
plt.ylabel("Speed")
plt.legend()
plt.show()

# ---------------------------------------------------
# Step 6: Summary of insights
# ---------------------------------------------------
print("\n====================== Summary ======================\n")
print("1. Mean: Represents the average value; useful for symmetric distributions.")
print("2. Median: Middle value after sorting; robust to outliers.")
print("3. Mode: Most frequent value; useful for understanding repeated observations.")
print("4. Visualizations (Histogram, Boxplot, Scatter) help to quickly understand data distribution.")
print("\n=====================================================\n")
