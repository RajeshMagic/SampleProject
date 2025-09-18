"""
uniform_distribution_demo.py
Uniform Distribution — 8 Separate Graph Illustrations
Author: OpenAI ChatGPT

Explains:
 - uniform(a, b): every value in [a,b) is equally likely
 - Each figure highlights one important property or concept
"""

import numpy as np
import matplotlib.pyplot as plt

print("\n===== UNIFORM DISTRIBUTION: 8 ILLUSTRATIONS (SEPARATE GRAPHS) =====\n")
print("Uniform distribution: every value in a range is equally probable.")
print("Use: numpy.random.uniform(low, high, size)\n")
print("Important: Uniform is ideal when each outcome in an interval should have equal chance.\n")

# 1) Small sample
x1 = np.random.uniform(0, 10, 20)
plt.hist(x1, bins=10, edgecolor='black', color='skyblue')
plt.title("1) Small sample (n=20) — 0..10")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 2) Large sample
x2 = np.random.uniform(0, 10, 10000)
plt.hist(x2, bins=20, edgecolor='black', color='lightgreen')
plt.title("2) Large sample (n=10,000) — 0..10")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 3) Narrow range 0..1
x3 = np.random.uniform(0, 1, 10000)
plt.hist(x3, bins=10, edgecolor='black', color='orange')
plt.title("3) Range 0..1 (n=10,000)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 4) Shifted range 50..100
x4 = np.random.uniform(50, 100, 10000)
plt.hist(x4, bins=25, edgecolor='black', color='plum')
plt.title("4) Range 50..100 (n=10,000)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 5) Effect of bin counts
x5 = np.random.uniform(0, 10, 5000)
plt.hist(x5, bins=5, alpha=0.7, label='5 bins', edgecolor='black')
plt.hist(x5, bins=50, alpha=0.5, label='50 bins', edgecolor='black')
plt.legend()
plt.title("5) Effect of bin count (5 vs 50)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 6) Uniform vs Normal overlay
x_uni = np.random.uniform(0, 10, 10000)
x_norm = np.random.normal(5, 1.5, 10000)
plt.hist(x_uni, bins=40, alpha=0.5, label='Uniform', edgecolor='black')
plt.hist(x_norm, bins=40, alpha=0.5, label='Normal (mean=5,std=1.5)', edgecolor='black')
plt.legend()
plt.title("6) Uniform vs Normal")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 7) Two ranges comparison
x7a = np.random.uniform(-5, 5, 5000)
x7b = np.random.uniform(0, 10, 5000)
plt.hist(x7a, bins=30, alpha=0.6, label='-5..5')
plt.hist(x7b, bins=30, alpha=0.6, label='0..10')
plt.legend()
plt.title("7) Compare different ranges")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 8) Cumulative distribution (CDF approximation)
x8 = np.random.uniform(0, 10, 10000)
plt.hist(x8, bins=100, cumulative=True, color='salmon', edgecolor='black')
plt.title("8) Cumulative Histogram (CDF approximation)")
plt.xlabel("Value")
plt.ylabel("Cumulative Count")
plt.show()

print("\nSummary / Important Notes:")
print(" - Uniform distributions produce roughly flat histograms when sample is large.")
print(" - Range parameters (low, high) shift and stretch the distribution.")
print(" - Small samples look noisy; large samples approach theoretical flatness.")
print(" - Use uniform to model 'every point equally likely' situations.\n")
