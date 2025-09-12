"""
Binomial Distribution Demonstration with NumPy, Matplotlib, and Seaborn
------------------------------------------------------------------------

Concept Recap:
--------------
1. Binomial Distribution is a DISCRETE distribution.
   - Example: Coin toss (Head or Tail).
   - Possible outcomes are COUNTABLE (0, 1, 2…n).
2. Parameters:
   - n     -> number of trials
   - p     -> probability of success in each trial
   - size  -> number of samples (shape of returned array)

Key Difference from Normal:
---------------------------
- Normal Distribution is CONTINUOUS (values like 1.1, 1.11, etc.)
- Binomial Distribution is DISCRETE (whole numbers, e.g. 0,1,2…)
- With large n and p≈0.5, binomial looks like a normal distribution.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# Example 1: Basic Binomial Distribution
# ------------------------------
print("\n" + "="*60)
print("EXAMPLE 1: Generate a Binomial Distribution with n=10, p=0.5, size=10")
print("="*60)

x1 = random.binomial(n=10, p=0.5, size=10)
print("Generated 10 samples of binomial distribution (10 coin tosses each):")
print(x1)
print("Important Note: Each value represents number of successes (e.g. heads) in 10 tosses.\n")


# ------------------------------
# Example 2: Visualization of Binomial Distribution
# ------------------------------
print("="*60)
print("EXAMPLE 2: Visualizing Binomial Distribution with Seaborn")
print("="*60)

x2 = random.binomial(n=10, p=0.5, size=1000)
print("Generated 1000 samples of binomial distribution (10 tosses, p=0.5).")
print("Plotting distribution curve...")

sns.displot(x2, kde=False)  # Histogram without KDE, since Binomial is discrete
plt.title("Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Number of Successes (out of 10)")
plt.ylabel("Frequency")
plt.show()


# ------------------------------
# Example 3: Binomial vs Normal Distribution
# ------------------------------
print("="*60)
print("EXAMPLE 3: Comparing Binomial Distribution with Normal Distribution")
print("="*60)

data = {
    "normal": random.normal(loc=50, scale=5, size=1000),     # continuous
    "binomial": random.binomial(n=100, p=0.5, size=1000)     # discrete
}

print("Generated 1000 samples each of Normal(loc=50, scale=5) and Binomial(n=100, p=0.5).")
print("Now comparing their distribution curves...")

sns.displot(data, kind="kde")
plt.title("Comparison: Normal vs Binomial Distributions")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()

print("\nKey Observation:")
print("- Normal is continuous → smooth bell curve.")
print("- Binomial is discrete → steps at integer values.")
print("- For large n and p≈0.5, binomial curve approximates normal.\n")

print("✅ All Binomial Distribution demonstrations completed successfully!")
