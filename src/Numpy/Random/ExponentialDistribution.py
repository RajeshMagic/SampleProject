##########################################
# Python Demonstration: Exponential Distribution
#
# This script demonstrates:
# - Concept of Exponential Distribution (time until next event)
# - Examples with different parameters (scale, size)
# - Visualization using Matplotlib (histograms, KDE)
# - Relation to Poisson Distribution
# - Console explanations with Important Notes
##########################################

from numpy import random
import numpy as np
import matplotlib.pyplot as plt

print("\n==============================================")
print("         Demonstration: Exponential Distribution")
print("==============================================\n")

##########################################
# Introduction
##########################################
print("Exponential Distribution is used to model the time between events.")
print("Examples: Time until machine failure, time until next customer arrival.")
print("\nParameters:")
print("- scale : Inverse of rate (λ). Larger scale = longer average wait.")
print("- size  : Shape of the output array.\n")

##########################################
# Example 1: Basic Exponential Distribution
##########################################
print("--- Example 1: Exponential Distribution with scale=2, size=(2,3) ---")

x = random.exponential(scale=2, size=(2, 3))
print("Generated 2x3 samples:\n", x)

# Visualization
samples = random.exponential(scale=2, size=1000)
plt.figure(figsize=(8, 5))
plt.hist(samples, bins=30, density=True, alpha=0.7, color='lightblue', edgecolor='black')
plt.title("Histogram of Exponential Distribution (scale=2)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print("Important Note: Exponential distribution is always positive (time cannot be negative).\n")

##########################################
# Example 2: Compare Different Scales
##########################################
print("--- Example 2: Effect of scale parameter ---")

scales = [1, 2, 5]
plt.figure(figsize=(8, 5))
for s in scales:
    sns = random.exponential(scale=s, size=1000)
    plt.hist(sns, bins=50, density=True, histtype='step', label=f'scale={s}')

plt.title("Comparison of Exponential Distributions with Different Scales")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print("Important Note: Smaller scale → faster decay (events occur more frequently).\n")

##########################################
# Relation Between Poisson and Exponential
##########################################
print("--- Relation Between Poisson and Exponential ---")
print("- Poisson: Counts number of events in fixed time interval.")
print("- Exponential: Models waiting time BETWEEN events.")

# Example: Simulate Poisson arrivals and Exponential waiting times
lam = 2  # average rate (events per unit time)
poisson_counts = random.poisson(lam=lam, size=1000)
exp_wait_times = random.exponential(scale=1/lam, size=1000)

print("Example: λ=2 (on average 2 events per unit time)")
print("Sample Poisson counts (first 10):", poisson_counts[:10])
print("Sample Exponential waiting times (first 10):", exp_wait_times[:10])

# Visualization side-by-side
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(poisson_counts, bins=range(0, max(poisson_counts)+1), color='salmon', edgecolor='black', alpha=0.7)
plt.title("Poisson Distribution (Counts per Interval, λ=2)")
plt.xlabel("Number of Events")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.hist(exp_wait_times, bins=30, density=True, color='lightgreen', edgecolor='black', alpha=0.7)
plt.title("Exponential Distribution (Waiting Times, scale=1/λ=0.5)")
plt.xlabel("Waiting Time")
plt.ylabel("Density")

plt.tight_layout()
plt.show()

print("Important Note: Poisson & Exponential are mathematically linked.")
print("If events follow a Poisson process with rate λ, waiting times follow an Exponential distribution with scale=1/λ.\n")

##########################################
# Summary
##########################################
print("\n==============================================")
print("SUMMARY:")
print("- Exponential Distribution models waiting time between events.")
print("- Parameters: scale (1/λ), size.")
print("- Always positive values.")
print("- Relation: Poisson counts vs Exponential waiting times (both describe Poisson processes).")
print("==============================================\n")