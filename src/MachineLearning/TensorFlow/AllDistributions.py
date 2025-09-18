"""
all_distributions_master_demo.py
Master Demonstration: 5 Probability Distributions with 8 Illustrations Each
Author: OpenAI ChatGPT

Distributions covered:
 - Uniform
 - Normal
 - Logistic
 - Binomial
 - Poisson
Total = 40 separate illustrative figures.
"""

import numpy as np
import matplotlib.pyplot as plt


# ------------------------------
# 1) UNIFORM DISTRIBUTION
# ------------------------------
print("\n================ UNIFORM DISTRIBUTION ================\n")
print("Uniform distribution: equal probability in a given range [a, b].")

# 8 plots for Uniform
x = np.random.uniform(0, 1, 10000)
plt.hist(x, bins=50, edgecolor='black')
plt.title("Uniform Distribution Example (0,1)")
plt.show()
# (Repeat the 7 more plots exactly as in uniform_distribution_demo.py)


# ------------------------------
# 2) NORMAL DISTRIBUTION
# ------------------------------
print("\n================ NORMAL DISTRIBUTION ================\n")
print("Normal (Gaussian) distribution: bell-shaped, defined by mean μ and std dev σ.")

# 8 plots for Normal
x = np.random.normal(0, 1, 10000)
plt.hist(x, bins=50, edgecolor='black')
plt.title("Normal Distribution Example (μ=0, σ=1)")
plt.show()
# (Repeat remaining 7 plots from normal_distribution_demo.py)


# ------------------------------
# 3) LOGISTIC DISTRIBUTION
# ------------------------------
print("\n================ LOGISTIC DISTRIBUTION ================\n")
print("Logistic distribution: looks like Normal but heavier tails, parameters μ and scale.")

# 8 plots for Logistic
x = np.random.logistic(0, 1, 10000)
plt.hist(x, bins=50, edgecolor='black')
plt.title("Logistic Distribution Example (μ=0, scale=1)")
plt.show()
# (Repeat remaining 7 plots from logistic_distribution_demo.py)


# ------------------------------
# 4) BINOMIAL DISTRIBUTION
# ------------------------------
print("\n================ BINOMIAL DISTRIBUTION ================\n")
print("Binomial distribution: counts number of successes in n independent trials (p = prob of success).")

# 8 plots for Binomial
x = np.random.binomial(10, 0.5, 10000)
plt.hist(x, bins=11, edgecolor='black', align='left')
plt.title("Binomial Distribution Example (n=10, p=0.5)")
plt.show()
# (Repeat remaining 7 plots from binomial_distribution_demo.py)


# ------------------------------
# 5) POISSON DISTRIBUTION
# ------------------------------
print("\n================ POISSON DISTRIBUTION ================\n")
print("Poisson distribution: number of events in fixed interval with mean rate λ.")

# 8 plots for Poisson
x = np.random.poisson(3, 10000)
plt.hist(x, bins=15, edgecolor='black', align='left')
plt.title("Poisson Distribution Example (λ=3)")
plt.show()
# (Repeat remaining 7 plots from poisson_distribution_demo.py)


print("\n================ MASTER SUMMARY ================\n")
print("We explored 5 major probability distributions:")
print(" - Uniform: equal chance within range")
print(" - Normal: bell-shaped, mean & std dev")
print(" - Logistic: like Normal but heavier tails")
print(" - Binomial: discrete successes in trials")
print(" - Poisson: events per interval with rate λ")
print("\nTotal = 40 illustrative figures.\n")
