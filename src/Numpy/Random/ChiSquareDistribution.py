##########################################
# Python Demonstration: Chi-Square Distribution
#
# This script demonstrates:
# - Concept of Chi-Square Distribution (basis for hypothesis testing)
# - Examples with different degrees of freedom (df) and sizes
# - Visualization (histograms, KDE)
# - Console outputs with Important Notes
##########################################

from numpy import random
import numpy as np
import matplotlib.pyplot as plt

print("\n==============================================")
print("         Demonstration: Chi-Square Distribution")
print("==============================================\n")

##########################################
# Introduction
##########################################
print("Chi-Square Distribution is widely used in hypothesis testing.")
print("It arises as the distribution of the sum of squares of normal variables.")
print("\nParameters:")
print("- df   : Degrees of freedom (must be > 0).")
print("- size : Shape of the returned array.\n")

##########################################
# Example 1: Basic Chi-Square Sample
##########################################
print("--- Example 1: Chi-Square Distribution with df=2, size=(2,3) ---")

x = random.chisquare(df=2, size=(2, 3))
print("Generated 2x3 samples:\n", x)

# Visualization
samples = random.chisquare(df=2, size=1000)
plt.figure(figsize=(8, 5))
plt.hist(samples, bins=30, density=True, alpha=0.7, color='lightblue', edgecolor='black')
plt.title("Chi-Square Distribution (df=2)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print("Important Note: Chi-Square values are always positive since they are sums of squares.\n")

##########################################
# Example 2: Effect of Degrees of Freedom
##########################################
print("--- Example 2: Effect of df on Chi-Square Distribution ---")

dfs = [1, 2, 5, 10]
plt.figure(figsize=(8, 5))
for d in dfs:
    sns = random.chisquare(df=d, size=1000)
    plt.hist(sns, bins=50, density=True, histtype='step', label=f'df={d}')

plt.title("Comparison of Chi-Square Distributions with Different df")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print("Important Note: Smaller df → distribution is more skewed. Larger df → shape approaches Normal distribution.\n")

##########################################
# Example 3: Chi-Square in Hypothesis Testing Context
##########################################
print("--- Example 3: Chi-Square in Hypothesis Testing ---")
print("In practice, Chi-Square is used to test categorical independence.")
print("Here, we only simulate data, but in real problems you compare observed vs expected counts.")

observed = [50, 30, 20]
expected = [40, 40, 20]

chi_square_stat = sum(((o - e) ** 2) / e for o, e in zip(observed, expected))
print("Observed counts:", observed)
print("Expected counts:", expected)
print("Chi-Square Statistic:", chi_square_stat)

print("Important Note: The test statistic is compared against Chi-Square distribution with (k-1) df.")
print("This determines whether to reject the null hypothesis.\n")

##########################################
# Summary
##########################################
print("\n==============================================")
print("SUMMARY:")
print("- Chi-Square Distribution is based on squared standard normal variables.")
print("- Parameters: df (degrees of freedom), size.")
print("- Always positive, skew depends on df.")
print("- Widely used in hypothesis testing (e.g., goodness-of-fit, independence tests).")
print("==============================================\n")