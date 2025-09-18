"""
logistic_distribution_demo.py
Logistic Distribution — 8 Separate Graph Illustrations
Author: OpenAI ChatGPT

Explains:
 - Logistic distribution looks like Normal but with heavier tails
 - Controlled by mean (μ = loc) and scale (σ ~ std dev)
 - Widely used in logistic regression, neural networks, and ML
"""

import numpy as np
import matplotlib.pyplot as plt

print("\n===== LOGISTIC DISTRIBUTION: 8 ILLUSTRATIONS (SEPARATE GRAPHS) =====\n")
print("Logistic distribution is symmetric and bell-shaped like Normal,")
print("but with heavier tails (more probability of extreme values).")
print("Use: numpy.random.logistic(loc, scale, size)\n")

# 1) Standard Logistic Distribution
x1 = np.random.logistic(0, 1, 10000)
plt.hist(x1, bins=50, edgecolor='black', color='skyblue')
plt.title("1) Standard Logistic (μ=0, scale=1)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 2) Different mean (loc) values
x2a = np.random.logistic(0, 1, 10000)
x2b = np.random.logistic(5, 1, 10000)
plt.hist(x2a, bins=50, alpha=0.6, label="μ=0")
plt.hist(x2b, bins=50, alpha=0.6, label="μ=5")
plt.legend()
plt.title("2) Effect of Mean (Shift)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 3) Different scale values
x3a = np.random.logistic(0, 1, 10000)
x3b = np.random.logistic(0, 3, 10000)
plt.hist(x3a, bins=50, alpha=0.6, label="scale=1")
plt.hist(x3b, bins=50, alpha=0.6, label="scale=3")
plt.legend()
plt.title("3) Effect of Scale (Spread)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 4) Small vs large sample
x4a = np.random.logistic(0, 1, 30)
x4b = np.random.logistic(0, 1, 10000)
plt.hist(x4a, bins=10, alpha=0.7, label="n=30")
plt.hist(x4b, bins=50, alpha=0.7, label="n=10,000")
plt.legend()
plt.title("4) Sample Size Effect (Noisy vs Smooth)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 5) Logistic vs Normal
x5a = np.random.logistic(0, 1, 10000)
x5b = np.random.normal(0, 1, 10000)
plt.hist(x5a, bins=50, alpha=0.6, label="Logistic")
plt.hist(x5b, bins=50, alpha=0.6, label="Normal")
plt.legend()
plt.title("5) Logistic vs Normal (Heavier tails for Logistic)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 6) Multiple Logistic Distributions
x6a = np.random.logistic(-3, 1, 10000)
x6b = np.random.logistic(0, 0.5, 10000)
x6c = np.random.logistic(3, 2, 10000)
plt.hist(x6a, bins=50, alpha=0.5, label="μ=-3, scale=1")
plt.hist(x6b, bins=50, alpha=0.5, label="μ=0, scale=0.5")
plt.hist(x6c, bins=50, alpha=0.5, label="μ=3, scale=2")
plt.legend()
plt.title("6) Comparing Multiple Logistic Distributions")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 7) Logistic with Outliers
x7 = np.append(np.random.logistic(0, 1, 1000), [10, -9, -11, 12])
plt.hist(x7, bins=50, edgecolor='black')
plt.title("7) Logistic with Outliers (still fits heavy tails)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 8) Cumulative Distribution (CDF)
x8 = np.random.logistic(0, 1, 10000)
plt.hist(x8, bins=100, cumulative=True, color='salmon', edgecolor='black')
plt.title("8) Logistic Cumulative Histogram (CDF)")
plt.xlabel("Value")
plt.ylabel("Cumulative Count")
plt.show()

print("\nSummary / Important Notes:")
print(" - Logistic resembles Normal but with heavier tails (more extremes).")
print(" - Mean (loc) shifts the curve; scale stretches it.")
print(" - Important in logistic regression & neural networks (sigmoid link).")
print(" - Useful for classification tasks in ML.\n")
