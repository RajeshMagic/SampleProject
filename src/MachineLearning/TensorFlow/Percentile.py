"""
Machine Learning: Understanding Percentiles
Author: OpenAI ChatGPT

This script demonstrates:
1. What percentiles are and why they matter in statistics / machine learning
2. How to calculate percentiles using NumPy
3. Examples with real data (ages of people)
4. Visualization using Matplotlib
5. Console outputs with "Important Notes" for clarity
"""

# ---------------------------------------------------
# Import required libraries
# ---------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

print("\n====================== Percentile Demonstration ======================\n")
print("Percentiles give us a way to describe the distribution of data.")
print("For example: the 75th percentile is the value below which 75% of the observations fall.\n")

# ---------------------------------------------------
# Step 1: Example dataset
# ---------------------------------------------------
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39,
        80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

print("[Step 1] Dataset (Ages of people on a street):")
print(ages)

# ---------------------------------------------------
# Step 2: Calculate 75th Percentile
# ---------------------------------------------------
p75 = np.percentile(ages, 75)
print(f"\n[Step 2] 75th Percentile: {p75}")
print("Important: This means that 75% of the people are aged 43 or younger.")

# ---------------------------------------------------
# Step 3: Calculate 90th Percentile
# ---------------------------------------------------
p90 = np.percentile(ages, 90)
print(f"\n[Step 3] 90th Percentile: {p90}")
print("Important: This means that 90% of the people are aged 61 or younger.")

# ---------------------------------------------------
# Step 4: Demonstrating multiple percentiles
# ---------------------------------------------------
percentiles = [25, 50, 75, 90]
values = np.percentile(ages, percentiles)

print("\n[Step 4] Commonly Used Percentiles:")
for perc, val in zip(percentiles, values):
    print(f"  {perc}th Percentile: {val}")

print("\nImportant Points:")
print(" - 25th Percentile is also called Q1 (first quartile)")
print(" - 50th Percentile is the Median (Q2)")
print(" - 75th Percentile is Q3")
print(" - Percentiles help detect spread, skewness, and outliers in data")

# ---------------------------------------------------
# Step 5: Visualizations
# ---------------------------------------------------

# Histogram with percentile lines
plt.hist(ages, bins=10, color='skyblue', edgecolor='black')
plt.axvline(p75, color='red', linestyle='dashed', linewidth=2, label=f'75th Percentile = {p75}')
plt.axvline(p90, color='orange', linestyle='dashed', linewidth=2, label=f'90th Percentile = {p90}')
plt.title("Histogram of Ages with Percentile Markers")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Boxplot (great for showing percentiles and spread)
plt.boxplot(ages, patch_artist=True,
            boxprops=dict(facecolor='lightgreen'))
plt.title("Boxplot of Ages (Shows Percentiles)")
plt.ylabel("Age")
plt.show()

# Cumulative Distribution Plot
sorted_ages = np.sort(ages)
cum_percentiles = np.linspace(0, 100, len(ages))
plt.plot(sorted_ages, cum_percentiles, marker='o', color='purple')
plt.axhline(75, color='red', linestyle='dashed', label='75th Percentile')
plt.axhline(90, color='orange', linestyle='dashed', label='90th Percentile')
plt.title("Cumulative Distribution of Ages")
plt.xlabel("Age")
plt.ylabel("Percentile (%)")
plt.legend()
plt.show()

# ---------------------------------------------------
# Step 6: Summary of insights
# ---------------------------------------------------
print("\n====================== Summary ======================\n")
print("1. Percentiles divide data into 100 equal parts.")
print("2. The 75th percentile = value below which 75% of data lies.")
print("3. The 90th percentile = value below which 90% of data lies.")
print("4. Percentiles are useful for:")
print("   - Detecting outliers")
print("   - Understanding distribution spread")
print("   - Comparing data across groups")
print("5. Visualizations like Histograms, Boxplots, and Cumulative Plots make it easy to interpret percentiles.")
print("\n=======================================================================\n")
