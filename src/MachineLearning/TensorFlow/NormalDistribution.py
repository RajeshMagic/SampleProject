"""
normal_distribution_demo.py
Normal (Gaussian) Distribution — 8 Separate Graph Illustrations
Author: OpenAI ChatGPT

Explains:
 - The famous "bell curve" distribution
 - Controlled by mean (μ) and standard deviation (σ)
 - Many natural and human-related phenomena follow this distribution
"""

import numpy as np
import matplotlib.pyplot as plt

print("\n===== NORMAL DISTRIBUTION: 8 ILLUSTRATIONS (SEPARATE GRAPHS) =====\n")
print("Normal distribution is symmetric and bell-shaped.")
print("Defined by parameters: mean (center) and std dev (spread).")
print("Use: numpy.random.normal(mean, std, size)\n")

# 1) Standard Normal Distribution (mean=0, std=1)
x1 = np.random.normal(0, 1, 10000)
plt.hist(x1, bins=50, edgecolor='black', color='skyblue')
plt.title("1) Standard Normal Distribution (μ=0, σ=1)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 2) Different mean values
x2a = np.random.normal(0, 1, 10000)
x2b = np.random.normal(5, 1, 10000)
plt.hist(x2a, bins=50, alpha=0.6, label="μ=0, σ=1")
plt.hist(x2b, bins=50, alpha=0.6, label="μ=5, σ=1")
plt.legend()
plt.title("2) Effect of Changing Mean (Shift Left/Right)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 3) Different standard deviations
x3a = np.random.normal(0, 1, 10000)
x3b = np.random.normal(0, 3, 10000)
plt.hist(x3a, bins=50, alpha=0.6, label="σ=1")
plt.hist(x3b, bins=50, alpha=0.6, label="σ=3")
plt.legend()
plt.title("3) Effect of Changing Std Dev (Spread)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 4) Small sample vs large sample
x4a = np.random.normal(0, 1, 30)
x4b = np.random.normal(0, 1, 10000)
plt.hist(x4a, bins=10, alpha=0.7, label="n=30")
plt.hist(x4b, bins=50, alpha=0.7, label="n=10,000")
plt.legend()
plt.title("4) Sample Size Effect (Noisy vs Smooth)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 5) Overlay 3 different normals
x5a = np.random.normal(-2, 1, 10000)
x5b = np.random.normal(0, 2, 10000)
x5c = np.random.normal(3, 0.5, 10000)
plt.hist(x5a, bins=50, alpha=0.5, label="μ=-2, σ=1")
plt.hist(x5b, bins=50, alpha=0.5, label="μ=0, σ=2")
plt.hist(x5c, bins=50, alpha=0.5, label="μ=3, σ=0.5")
plt.legend()
plt.title("5) Comparing Multiple Normals")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 6) Normal vs Logistic distribution
x6a = np.random.normal(0, 1, 10000)
x6b = np.random.logistic(0, 1, 10000)
plt.hist(x6a, bins=50, alpha=0.6, label="Normal")
plt.hist(x6b, bins=50, alpha=0.6, label="Logistic")
plt.legend()
plt.title("6) Normal vs Logistic (Logistic has heavier tails)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 7) Normal Distribution with Outliers
x7 = np.append(np.random.normal(0, 1, 1000), [8, 9, -7, -8])
plt.hist(x7, bins=50, edgecolor='black')
plt.title("7) Normal Distribution with Outliers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 8) Cumulative Distribution (CDF Approximation)
x8 = np.random.normal(0, 1, 10000)
plt.hist(x8, bins=100, cumulative=True, color='salmon', edgecolor='black')
plt.title("8) Normal Cumulative Histogram (CDF)")
plt.xlabel("Value")
plt.ylabel("Cumulative Count")
plt.show()

print("\nSummary / Important Notes:")
print(" - Normal distribution is symmetric and defined by mean and std dev.")
print(" - Mean shifts the curve left/right, std dev controls spread.")
print(" - Larger samples approximate the bell curve better.")
print(" - Many ML algorithms assume normality for features/errors.\n")
