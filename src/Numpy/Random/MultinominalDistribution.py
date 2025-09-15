##########################################
# Python Demonstration: Multinomial Distribution
#
# This script demonstrates:
# - Concept of Multinomial Distribution (generalization of Binomial)
# - Different parameter settings (n, pvals, size)
# - Visualizations (bar charts, stacked experiments)
# - Console outputs with Important Notes
##########################################

from numpy import random
import numpy as np
import matplotlib.pyplot as plt

print("\n==============================================")
print("         Demonstration: Multinomial Distribution")
print("==============================================\n")

##########################################
# Introduction
##########################################
print("Multinomial Distribution is a generalization of the Binomial distribution.")
print("Binomial: Two outcomes (success/failure).")
print("Multinomial: Multiple outcomes (e.g. dice rolls, survey responses, blood types).\n")

print("Parameters:")
print("- n     : Number of trials (how many times experiment is repeated).")
print("- pvals : Probabilities of each category (must sum to 1).")
print("- size  : Shape/number of experiments to run.\n")

##########################################
# Example 1: Fair Dice Roll
##########################################
print("--- Example 1: Fair Dice Roll (6 rolls) ---")
print("We roll a fair dice 6 times. Probabilities are equal: [1/6,...,1/6].")

x = random.multinomial(n=6, pvals=[1/6]*6)
print("Outcome counts for each face (1-6):", x)

# Visualization
plt.figure(figsize=(7, 4))
plt.bar(range(1, 7), x, color='lightblue', edgecolor='black')
plt.title("Multinomial Distribution: Fair Dice Roll (6 trials)")
plt.xlabel("Dice Face")
plt.ylabel("Counts")
plt.show()

print("Important Note: Multinomial returns an array with counts for EACH category, not a single value!\n")

##########################################
# Example 2: Biased Dice Roll
##########################################
print("--- Example 2: Biased Dice Roll (20 rolls) ---")
pvals_biased = [0.05, 0.1, 0.15, 0.2, 0.25, 0.25]
print("Probabilities:", pvals_biased)

x2 = random.multinomial(n=20, pvals=pvals_biased)
print("Outcome counts for 20 rolls:", x2)

# Visualization
plt.figure(figsize=(7, 4))
plt.bar(range(1, 7), x2, color='salmon', edgecolor='black')
plt.title("Multinomial Distribution: Biased Dice Roll (20 trials)")
plt.xlabel("Dice Face")
plt.ylabel("Counts")
plt.show()

print("Important Note: Probabilities (pvals) don’t have to be equal, but they must sum to 1.\n")

##########################################
# Example 3: Multiple Experiments (size parameter)
##########################################
print("--- Example 3: Multiple Experiments (size=5) ---")
print("We run 5 experiments. Each experiment has 10 trials with 3 categories.")

pvals_multi = [0.2, 0.3, 0.5]
x3 = random.multinomial(n=10, pvals=pvals_multi, size=5)
print("Probabilities:", pvals_multi)
print("Results of 5 experiments:\n", x3)

# Visualization: Stacked bar chart
plt.figure(figsize=(7, 5))
labels = ["Category 1", "Category 2", "Category 3"]
for i, exp in enumerate(x3):
    plt.bar(labels, exp, bottom=np.sum(x3[:i], axis=0) if i > 0 else None, alpha=0.6)
plt.title("Multinomial Distribution: 5 Experiments (10 trials each)")
plt.ylabel("Counts")
plt.show()

print("Important Note: Using 'size' allows running multiple experiments at once.\n")

##########################################
# Summary
##########################################
print("\n==============================================")
print("SUMMARY:")
print("- Multinomial Distribution extends Binomial to more than 2 outcomes.")
print("- Returns counts for each category, not a single outcome.")
print("- Parameters: n (trials), pvals (probabilities), size (experiments).")
print("- Useful for modeling categorical outcomes (dice, polls, genetics, etc.).")
print("==============================================\n")