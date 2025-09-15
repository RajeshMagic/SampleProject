##########################################
# Python Demonstration: Rayleigh Distribution
#
# This script demonstrates:
# - Concept of Rayleigh Distribution (used in signal processing)
# - Examples with different scale and size parameters
# - Visualization (histograms, KDE)
# - Similarity to Chi-Square Distribution (df=2)
# - Console outputs with Important Notes
##########################################

from numpy import random
import numpy as np
import matplotlib.pyplot as plt

print("\n==============================================")
print("         Demonstration: Rayleigh Distribution")
print("==============================================\n")

##########################################
# Introduction
##########################################
print("Rayleigh Distribution is widely used in signal processing (e.g. modeling noise).")
print("It is a continuous distribution related to Chi-Square.")
print("\nParameters:")
print("- scale : Standard deviation (controls spread of distribution). Default=1.0")
print("- size  : Shape of the returned array.\n")

##########################################
# Example 1: Basic Rayleigh Sample
##########################################
print("--- Example 1: Rayleigh Distribution with scale=2, size=(2,3) ---")

x = random.rayleigh(scale=2, size=(2, 3))
print("Generated 2x3 samples:\n", x)

# Visualization
samples = random.rayleigh(scale=2, size=1000)
plt.figure(figsize=(8, 5))
plt.hist(samples, bins=30, density=True, alpha=0.7, color='lightblue', edgecolor='black')
plt.title("Rayleigh Distribution (scale=2)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print("Important Note: Rayleigh distribution only produces positive values (like Chi-Square).\n")

##########################################
# Example 2: Compare Different Scales
##########################################
print("--- Example 2: Effect of scale parameter ---")

scales = [1, 2, 5]
plt.figure(figsize=(8, 5))
for s in scales:
    sns = random.rayleigh(scale=s, size=1000)
    plt.hist(sns, bins=50, density=True, histtype='step', label=f'scale={s}')

plt.title("Comparison of Rayleigh Distributions with Different Scales")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print("Important Note: Larger scale → distribution spreads out more. Smaller scale → sharper peak.\n")

##########################################
# Example 3: Relation to Chi-Square
##########################################
print("--- Example 3: Relation Between Rayleigh and Chi-Square ---")
print("At unit stddev and df=2, Rayleigh and Chi-Square are related.")

rayleigh_samples = random.rayleigh(scale=1, size=1000)
chisq_samples = random.chisquare(df=2, size=1000)

plt.figure(figsize=(8, 5))
plt.hist(rayleigh_samples, bins=50, density=True, histtype='step', label="Rayleigh (scale=1)")
plt.hist(chisq_samples, bins=50, density=True, histtype='step', label="Chi-Square (df=2)")

plt.title("Rayleigh vs Chi-Square Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print("Important Note: Chi-Square with df=2 is mathematically equivalent to Rayleigh squared.")
print("This explains their similarity in shape.\n")

##########################################
# Summary
##########################################
print("\n==============================================")
print("SUMMARY:")
print("- Rayleigh Distribution is widely used in signal processing.")
print("- Parameters: scale (stddev), size.")
print("- Produces positive values only.")
print("- Related to Chi-Square: Rayleigh (scale=1) ↔ Chi-Square(df=2).")
print("==============================================\n")