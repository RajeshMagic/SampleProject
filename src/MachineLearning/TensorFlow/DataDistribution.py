"""
Machine Learning: Data Distribution Demonstration
Author: OpenAI ChatGPT

This script demonstrates:
1. How to generate random datasets using NumPy
2. How to visualize data distributions using Histograms in Matplotlib
3. Understanding histogram bins and frequency counts
4. Small dataset example (250 samples)
5. Big dataset example (100,000 samples)
"""

# ---------------------------------------------------
# Import required libraries
# ---------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

print("\n====================== Data Distribution Demo ======================\n")
print("In real-world Machine Learning projects, datasets can be very large.")
print("NumPy helps us simulate random data for practice and testing.")
print("Matplotlib lets us visualize distributions using Histograms.\n")

# ---------------------------------------------------
# Step 1: Create a small dataset (250 random floats between 0 and 5)
# ---------------------------------------------------
print("[Step 1] Generating a SMALL dataset of 250 random floats between 0 and 5 ...")
x_small = np.random.uniform(0.0, 5.0, 250)
print("Sample of dataset:", x_small[:10], "...\n")  # Print first 10 values

# ---------------------------------------------------
# Step 2: Visualize the small dataset with a Histogram
# ---------------------------------------------------
print("[Step 2] Drawing Histogram for SMALL dataset with 5 bins ...")
print("Each bin represents the count of values in a range:")
print("  Bin 1 → values between 0 and 1")
print("  Bin 2 → values between 1 and 2")
print("  Bin 3 → values between 2 and 3")
print("  Bin 4 → values between 3 and 4")
print("  Bin 5 → values between 4 and 5\n")

plt.hist(x_small, bins=5, color='skyblue', edgecolor='black')
plt.title("Histogram (250 samples, 5 bins)")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()

# ---------------------------------------------------
# Step 3: Count frequencies in each bin manually
# ---------------------------------------------------
print("[Step 3] Frequency counts for each bin (using NumPy histogram):")
counts, bin_edges = np.histogram(x_small, bins=5, range=(0.0, 5.0))
for i in range(len(counts)):
    print(f"  Bin {i+1} ({bin_edges[i]:.1f} - {bin_edges[i+1]:.1f}): {counts[i]} values")

print("\nImportant Note: The counts may differ on each run because the dataset is random.\n")

# ---------------------------------------------------
# Step 4: Create a BIG dataset (100,000 random floats between 0 and 5)
# ---------------------------------------------------
print("[Step 4] Generating a BIG dataset of 100,000 random floats between 0 and 5 ...")
x_big = np.random.uniform(0.0, 5.0, 100000)
print("First 10 values from big dataset:", x_big[:10], "...\n")

# ---------------------------------------------------
# Step 5: Visualize the big dataset with a Histogram (100 bins)
# ---------------------------------------------------
print("[Step 5] Drawing Histogram for BIG dataset with 100 bins ...")
print("This allows us to see the distribution much more clearly.\n")

plt.hist(x_big, bins=100, color='orange', edgecolor='black')
plt.title("Histogram (100,000 samples, 100 bins)")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()

# ---------------------------------------------------
# Step 6: Summary of insights
# ---------------------------------------------------
print("\n====================== Summary ======================\n")
print("1. NumPy 'random.uniform(low, high, size)' generates datasets of any size.")
print("2. Histograms show how data is distributed across ranges (bins).")
print("3. Smaller datasets (250 values) may look irregular, due to randomness.")
print("4. Larger datasets (100,000 values) show smoother, uniform distribution.")
print("5. Bin counts (like 0-1, 1-2, etc.) tell us how many values fall in each interval.")
print("6. Data distribution is a critical first step in data analysis & ML projects.")
print("\n======================================================================\n")
