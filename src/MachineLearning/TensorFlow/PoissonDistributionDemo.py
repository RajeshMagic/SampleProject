"""
poisson_distribution_demo.py
Poisson Distribution — 8 Separate Graph Illustrations
Author: OpenAI ChatGPT

Explains:
 - Models the number of events in a fixed time/space interval
 - Parameter λ (lambda) = expected rate (mean number of events)
 - Important for queueing, reliability, traffic, rare events
"""

import numpy as np
import matplotlib.pyplot as plt

print("\n===== POISSON DISTRIBUTION: 8 ILLUSTRATIONS (SEPARATE GRAPHS) =====\n")
print("Poisson distribution gives probability of k events in fixed interval.")
print("Defined by λ (mean rate of events).")
print("Use: numpy.random.poisson(lam, size)\n")

# 1) Basic Poisson example (λ=3)
x1 = np.random.poisson(3, 10000)
plt.hist(x1, bins=15, edgecolor='black', color='skyblue', align='left')
plt.title("1) Basic Poisson Distribution (λ=3)")
plt.xlabel("Events (k)")
plt.ylabel("Frequency")
plt.show()

# 2) Different λ values
x2a = np.random.poisson(2, 10000)
x2b = np.random.poisson(7, 10000)
plt.hist(x2a, bins=20, alpha=0.6, label="λ=2", align='left')
plt.hist(x2b, bins=20, alpha=0.6, label="λ=7", align='left')
plt.legend()
plt.title("2) Effect of Changing λ (mean events)")
plt.xlabel("Events (k)")
plt.ylabel("Frequency")
plt.show()

# 3) Very small λ (rare events)
x3 = np.random.poisson(0.5, 10000)
plt.hist(x3, bins=10, edgecolor='black', color='lightgreen', align='left')
plt.title("3) Rare Events (λ=0.5)")
plt.xlabel("Events (k)")
plt.ylabel("Frequency")
plt.show()

# 4) Large λ (distribution looks Normal-like)
x4 = np.random.poisson(50, 10000)
plt.hist(x4, bins=60, edgecolor='black', color='salmon')
plt.title("4) Large λ=50 ~ Normal Approximation")
plt.xlabel("Events (k)")
plt.ylabel("Frequency")
plt.show()

# 5) Poisson vs Binomial (approximation)
x5a = np.random.poisson(5, 10000)
x5b = np.random.binomial(1000, 0.005, 10000)  # n large, p small
plt.hist(x5a, bins=20, alpha=0.6, label="Poisson λ=5", align='left')
plt.hist(x5b, bins=20, alpha=0.6, label="Binomial n=1000, p=0.005", align='left')
plt.legend()
plt.title("5) Poisson vs Binomial Approximation")
plt.xlabel("Events (k)")
plt.ylabel("Frequency")
plt.show()

# 6) Multiple λ values compared
x6a = np.random.poisson(2, 10000)
x6b = np.random.poisson(5, 10000)
x6c = np.random.poisson(10, 10000)
plt.hist(x6a, bins=20, alpha=0.5, label="λ=2", align='left')
plt.hist(x6b, bins=20, alpha=0.5, label="λ=5", align='left')
plt.hist(x6c, bins=20, alpha=0.5, label="λ=10", align='left')
plt.legend()
plt.title("6) Comparing Multiple λ Values")
plt.xlabel("Events (k)")
plt.ylabel("Frequency")
plt.show()

# 7) Small vs large sample size
x7a = np.random.poisson(5, 30)
x7b = np.random.poisson(5, 10000)
plt.hist(x7a, bins=15, alpha=0.7, label="n=30 sample", align='left')
plt.hist(x7b, bins=15, alpha=0.7, label="n=10,000 sample", align='left')
plt.legend()
plt.title("7) Sample Size Effect")
plt.xlabel("Events (k)")
plt.ylabel("Frequency")
plt.show()

# 8) Cumulative Distribution (CDF Approximation)
x8 = np.random.poisson(5, 10000)
plt.hist(x8, bins=30, cumulative=True, color='orange', edgecolor='black', align='left')
plt.title("8) Poisson Cumulative Histogram (CDF)")
plt.xlabel("Events (k)")
plt.ylabel("Cumulative Count")
plt.show()

print("\nSummary / Important Notes:")
print(" - Poisson models number of events per interval, with mean λ.")
print(" - λ small => rare events; λ large => curve ~ Normal.")
print(" - Poisson approximates Binomial (large n, small p).")
print(" - Useful in reliability, traffic, call centers, disease spread, etc.\n")
