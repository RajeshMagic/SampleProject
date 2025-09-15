##########################################
# Python Demonstration: Pareto Distribution
#
# This script demonstrates:
# - Concept of Pareto Distribution (80-20 rule)
# - Examples with different shape parameters `a`
# - Visualization (histograms, KDE)
# - Illustration of Pareto's law (80-20 principle)
# - Console outputs with Important Notes
##########################################

from numpy import random
import numpy as np
import matplotlib.pyplot as plt

print("\n==============================================")
print("         Demonstration: Pareto Distribution")
print("==============================================\n")

##########################################
# Introduction
##########################################
print("Pareto Distribution is also known as the 80-20 distribution.")
print("It models phenomena where a small number of factors account for most of the effect.")
print("\nParameters:")
print("- a    : Shape parameter (controls heaviness of the tail).")
print("- size : Shape of the returned array.\n")

##########################################
# Example 1: Basic Pareto Sample
##########################################
print("--- Example 1: Pareto Distribution with a=2, size=(2,3) ---")

x = random.pareto(a=2, size=(2, 3))
print("Generated 2x3 samples:\n", x)

# Visualization
samples = random.pareto(a=2, size=1000)
plt.figure(figsize=(8, 5))
plt.hist(samples, bins=30, density=True, alpha=0.7, color='lightgreen', edgecolor='black')
plt.title("Pareto Distribution (a=2)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print("Important Note: Pareto distribution produces only positive values and is heavy-tailed.\n")

##########################################
# Example 2: Effect of Shape Parameter
##########################################
print("--- Example 2: Effect of shape parameter a ---")

shapes = [1, 2, 5]
plt.figure(figsize=(8, 5))
for a in shapes:
    sns = random.pareto(a=a, size=1000)
    plt.hist(sns, bins=100, density=True, histtype='step', label=f'a={a}')

plt.title("Comparison of Pareto Distributions with Different Shape Parameters")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print("Important Note: Smaller 'a' → heavier tail (more extreme large values). Larger 'a' → distribution is more concentrated.\n")

##########################################
# Example 3: Demonstrating 80-20 Rule
##########################################
print("--- Example 3: Illustrating Pareto's Law (80-20 Rule) ---")

# Generate income-like data using Pareto
data = (random.pareto(a=2, size=10000) + 1) * 100  # scale for interpretation

# Sort data descending
sorted_data = np.sort(data)[::-1]

# Compute cumulative share of wealth
cumulative_share = np.cumsum(sorted_data) / sorted_data.sum()

# Find proportion at 20%
n_people = len(sorted_data)
top_20pct_index = int(0.2 * n_people)
share_top20 = cumulative_share[top_20pct_index]

plt.figure(figsize=(8, 5))
plt.plot(np.linspace(0, 100, n_people), cumulative_share * 100, label="Cumulative Share of Wealth")
plt.axvline(x=20, color='red', linestyle='--', label="Top 20%")
plt.axhline(y=share_top20 * 100, color='blue', linestyle='--', label=f"≈ {share_top20*100:.1f}% Wealth")
plt.title("Pareto Principle: 80-20 Rule")
plt.xlabel("Population % (sorted by wealth)")
plt.ylabel("Cumulative Wealth Share (%)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print(f"Important Note: In this simulation, the top 20% of population holds ≈ {share_top20*100:.1f}% of the wealth.")
print("This illustrates the Pareto principle in action.\n")

##########################################
# Summary
##########################################
print("\n==============================================")
print("SUMMARY:")
print("- Pareto distribution models the 80-20 rule.")
print("- Parameters: a (shape), size.")
print("- Heavy-tailed: few large values dominate.")
print("- Demonstrated with income/wealth example.")
print("==============================================\n")
