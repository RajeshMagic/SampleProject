##########################################
# Python Demonstration: Zipf Distribution
#
# This script demonstrates:
# - Concept of Zipf Distribution (Zipf's Law)
# - Examples with different distribution parameters `a`
# - Visualization (histograms, filtered plots)
# - Demonstration of Zipf’s Law (rank vs frequency)
# - Console outputs with Important Notes
##########################################

from numpy import random
import numpy as np
import matplotlib.pyplot as plt

print("\n==============================================")
print("         Demonstration: Zipf Distribution")
print("==============================================\n")

##########################################
# Introduction
##########################################
print("Zipf Distribution is based on Zipf's Law:")
print("In a collection, the nth most common term occurs ~1/n times as often as the most common term.")
print("Example: The 5th most common word in English appears ~1/5 as often as the most common word.")
print("\nParameters:")
print("- a    : Distribution parameter (controls steepness of frequencies).")
print("- size : Shape of the returned array.\n")

##########################################
# Example 1: Basic Zipf Sample
##########################################
print("--- Example 1: Zipf Distribution with a=2, size=(2,3) ---")

x = random.zipf(a=2, size=(2, 3))
print("Generated 2x3 samples:\n", x)

# Visualization
samples = random.zipf(a=2, size=1000)

# Filter for smaller values to make plot meaningful
plt.figure(figsize=(8, 5))
plt.hist(samples[samples < 10], bins=np.arange(1, 11)-0.5, rwidth=0.8, color="skyblue", edgecolor="black")
plt.title("Zipf Distribution (a=2), Values < 10")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print("Important Note: Zipf distribution often produces very large values, so plots are usually restricted (e.g. values < 10).")
print("This makes patterns easier to see.\n")

##########################################
# Example 2: Effect of Distribution Parameter
##########################################
print("--- Example 2: Effect of distribution parameter a ---")

params = [1.1, 2, 3]
plt.figure(figsize=(8, 5))
for a in params:
    data = random.zipf(a=a, size=1000)
    plt.hist(data[data < 20], bins=np.arange(1, 21)-0.5, histtype="step", label=f'a={a}')

plt.title("Comparison of Zipf Distributions with Different Parameters")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print("Important Note: Smaller 'a' → heavier tail (more large values). Larger 'a' → distribution becomes more concentrated at small values.\n")

##########################################
# Example 3: Demonstrating Zipf’s Law
##########################################
print("--- Example 3: Demonstrating Zipf's Law ---")

# Generate larger dataset
data = random.zipf(a=2, size=10000)

# Count frequencies
unique, counts = np.unique(data, return_counts=True)
freqs = counts / counts.sum()

# Sort by rank
ranks = np.arange(1, len(freqs)+1)

plt.figure(figsize=(8, 5))
plt.loglog(ranks, np.sort(freqs)[::-1], marker="o", linestyle="None", markersize=5, color="purple")
plt.title("Zipf's Law: Frequency vs Rank (log-log scale)")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.grid(True, which="both", linestyle='--', alpha=0.6)
plt.show()

print("Important Note: On a log-log scale, Zipf's Law produces an approximately straight line,")
print("showing that frequency ~ 1/rank.\n")

##########################################
# Summary
##########################################
print("\n==============================================")
print("SUMMARY:")
print("- Zipf distribution models ranked frequency phenomena (e.g., words in language, city sizes).")
print("- Parameters: a (steepness), size.")
print("- Heavy-tailed: small number of values dominate.")
print("- Demonstrated with rank-frequency plot (Zipf’s Law).")
print("==============================================\n")
