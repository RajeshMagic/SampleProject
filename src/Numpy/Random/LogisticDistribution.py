##########################################
# Python Demonstration: Logistic & Multinomial Distributions
#
# This script demonstrates:
# 1. Logistic Distribution (used in logistic regression, neural networks, etc.)
# 2. Multinomial Distribution (generalization of binomial distribution)
#
# Organized with clear explanations, outputs, and visualizations.
##########################################

from numpy import random
import numpy as np
import matplotlib.pyplot as plt

print("\n==============================================")
print("      Demonstration of Probability Distributions")
print("==============================================\n")

##########################################
# Part 1: Logistic Distribution
##########################################
print("\n--- Logistic Distribution ---")
print("Important Note: Logistic Distribution is used in logistic regression, ML, etc.")
print("It is similar to the normal distribution but has heavier tails.")

# Example 1: Draw 2x3 samples with mean at 1, scale=2
x = random.logistic(loc=1, scale=2, size=(2, 3))
print("\nExample 1: Logistic Distribution with loc=1, scale=2, size=(2,3)")
print("Generated Samples:\n", x)

# Example 2: Compare multiple samples to show spread
x2 = random.logistic(loc=0, scale=1, size=1000)
print("\nExample 2: Logistic Distribution with default loc=0, scale=1")
print("Showing 10 random samples:", x2[:10])

print("\nImportant Point: 'loc' defines the mean (center), 'scale' defines spread.")
print("Heavier tails compared to normal distribution.")

# Visualization: Histogram of logistic distribution
plt.figure(figsize=(8, 5))
plt.hist(x2, bins=30, density=True, alpha=0.7, color='skyblue', edgecolor='black')
plt.title("Histogram of Logistic Distribution (loc=0, scale=1)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

##########################################
# Part 2: Multinomial Distribution
##########################################
print("\n--- Multinomial Distribution ---")
print("Important Note: Multinomial is a generalization of Binomial distribution.")
print("Instead of 2 outcomes, we can have multiple outcomes.")

# Example 1: Simulate rolling a dice 6 times
x = random.multinomial(n=6, pvals=[1/6]*6)
print("\nExample 1: Dice roll simulation (6 rolls)")
print("Outcome counts for each face (1-6):", x)

# Visualization: Bar chart for dice roll
plt.figure(figsize=(7, 4))
plt.bar(range(1, 7), x, color='lightgreen', edgecolor='black')
plt.title("Multinomial Distribution: Dice Roll Simulation (6 rolls)")
plt.xlabel("Dice Face")
plt.ylabel("Count")
plt.show()

# Example 2: Biased dice (probabilities not equal)
pvals_biased = [0.05, 0.1, 0.15, 0.2, 0.25, 0.25]
x2 = random.multinomial(n=100, pvals=pvals_biased)
print("\nExample 2: Biased Dice roll simulation (100 rolls)")
print("Probabilities:", pvals_biased)
print("Outcome counts:", x2)

# Visualization: Bar chart for biased dice
plt.figure(figsize=(7, 4))
plt.bar(range(1, 7), x2, color='salmon', edgecolor='black')
plt.title("Multinomial Distribution: Biased Dice Roll (100 rolls)")
plt.xlabel("Dice Face")
plt.ylabel("Count")
plt.show()

# Example 3: Multiple experiments at once (size parameter)
x3 = random.multinomial(n=10, pvals=[0.2, 0.3, 0.5], size=5)
print("\nExample 3: Multinomial with size=5 (5 experiments, each with 10 trials)")
print("Probabilities: [0.2, 0.3, 0.5]")
print("Results (5 experiments):\n", x3)

# Visualization: Stacked bar chart for multiple experiments
plt.figure(figsize=(7, 5))
labels = ["Cat1", "Cat2", "Cat3"]
for i, exp in enumerate(x3):
    plt.bar(labels, exp, bottom=np.sum(x3[:i], axis=0) if i > 0 else None, alpha=0.6)
plt.title("Multinomial Distribution: 5 Experiments (10 trials each)")
plt.ylabel("Counts")
plt.show()

print("\nImportant Point: Multinomial returns counts for each category, not a single value!")
print("It can simulate categorical experiments (dice rolls, survey results, etc.).")

##########################################
# Summary
##########################################
print("\n==============================================")
print("SUMMARY:")
print("- Logistic Distribution: Continuous distribution, heavy tails, used in ML.")
print("- Multinomial Distribution: Discrete counts across multiple outcomes, generalizes Binomial.")
print("- Visualizations help understand spread (Logistic) and categorical counts (Multinomial).")
print("==============================================\n")
