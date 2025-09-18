"""
binomial_distribution_demo.py
Binomial Distribution — 8 Separate Graph Illustrations
Author: OpenAI ChatGPT

Explains:
 - Discrete distribution: counts number of successes in n independent trials
 - Parameters: n (trials), p (success probability)
 - Important in probability, statistics, and ML (classification, coin flips, etc.)
"""

import numpy as np
import matplotlib.pyplot as plt

print("\n===== BINOMIAL DISTRIBUTION: 8 ILLUSTRATIONS (SEPARATE GRAPHS) =====\n")
print("Binomial distribution models the number of successes in n trials.")
print("Use: numpy.random.binomial(n, p, size)\n")

# 1) Basic coin flip (n=10, p=0.5)
x1 = np.random.binomial(10, 0.5, 10000)
plt.hist(x1, bins=11, edgecolor='black', color='skyblue', align='left')
plt.title("1) Coin Flip Example (n=10, p=0.5)")
plt.xlabel("Successes")
plt.ylabel("Frequency")
plt.show()

# 2) Biased coin (p=0.2 vs p=0.8)
x2a = np.random.binomial(10, 0.2, 10000)
x2b = np.random.binomial(10, 0.8, 10000)
plt.hist(x2a, bins=11, alpha=0.6, label="p=0.2", align='left')
plt.hist(x2b, bins=11, alpha=0.6, label="p=0.8", align='left')
plt.legend()
plt.title("2) Effect of Changing Probability (p)")
plt.xlabel("Successes")
plt.ylabel("Frequency")
plt.show()

# 3) Increasing trials (n=10 vs n=100)
x3a = np.random.binomial(10, 0.5, 10000)
x3b = np.random.binomial(100, 0.5, 10000)
plt.hist(x3a, bins=11, alpha=0.6, label="n=10", align='left')
plt.hist(x3b, bins=50, alpha=0.6, label="n=100", align='left')
plt.legend()
plt.title("3) Effect of Increasing Trials (n)")
plt.xlabel("Successes")
plt.ylabel("Frequency")
plt.show()

# 4) Small vs large sample size
x4a = np.random.binomial(10, 0.5, 30)
x4b = np.random.binomial(10, 0.5, 10000)
plt.hist(x4a, bins=11, alpha=0.7, label="n=30 sample", align='left')
plt.hist(x4b, bins=11, alpha=0.7, label="n=10,000 sample", align='left')
plt.legend()
plt.title("4) Sample Size Effect (Noisy vs Smooth)")
plt.xlabel("Successes")
plt.ylabel("Frequency")
plt.show()

# 5) Binomial (n large, p small) approximates Poisson
x5 = np.random.binomial(1000, 0.01, 10000)
plt.hist(x5, bins=30, edgecolor='black')
plt.title("5) Binomial ~ Poisson Approximation (n=1000, p=0.01)")
plt.xlabel("Successes")
plt.ylabel("Frequency")
plt.show()

# 6) Binomial (n large, p ~ 0.5) approximates Normal
x6 = np.random.binomial(100, 0.5, 10000)
plt.hist(x6, bins=50, edgecolor='black', color='lightgreen')
plt.title("6) Binomial ~ Normal Approximation (n=100, p=0.5)")
plt.xlabel("Successes")
plt.ylabel("Frequency")
plt.show()

# 7) Multiple probabilities comparison
x7a = np.random.binomial(20, 0.3, 10000)
x7b = np.random.binomial(20, 0.5, 10000)
x7c = np.random.binomial(20, 0.7, 10000)
plt.hist(x7a, bins=21, alpha=0.5, label="p=0.3", align='left')
plt.hist(x7b, bins=21, alpha=0.5, label="p=0.5", align='left')
plt.hist(x7c, bins=21, alpha=0.5, label="p=0.7", align='left')
plt.legend()
plt.title("7) Comparing Different Probabilities")
plt.xlabel("Successes")
plt.ylabel("Frequency")
plt.show()

# 8) Distribution shape with very high n
x8 = np.random.binomial(500, 0.5, 10000)
plt.hist(x8, bins=60, edgecolor='black', color='salmon')
plt.title("8) Large n=500 (symmetric bell-shaped)")
plt.xlabel("Successes")
plt.ylabel("Frequency")
plt.show()

print("\nSummary / Important Notes:")
print(" - Binomial counts successes out of n independent trials.")
print(" - p controls bias, n controls shape/spread.")
print(" - For large n and small p, Binomial ~ Poisson.")
print(" - For large n and p≈0.5, Binomial ~ Normal.")
print(" - Important in ML classification (yes/no outcomes).\n")
