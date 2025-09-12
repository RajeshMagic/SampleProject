"""
Uniform Distribution Demonstration with NumPy, Matplotlib, and Seaborn
----------------------------------------------------------------------

Concept Recap:
--------------
1. Uniform Distribution:
   - All outcomes in the given interval are equally likely.
   - Example: Rolling a fair die (1–6, each has equal probability).

2. Parameters:
   - low   -> lower bound (default = 0.0).
   - high  -> upper bound (default = 1.0).
   - size  -> shape of returned array.

3. Continuous Distribution:
   - Uniform distribution is continuous between [low, high).
   - Contrast with discrete uniform (like dice rolls).
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# ------------------------------
# Example 1: Basic Uniform Distribution (default low=0, high=1)
# ------------------------------
print("\n" + "="*70)
print("EXAMPLE 1: Generate a 2x3 Uniform Distribution sample (default [0,1))")
print("="*70)

x1 = random.uniform(size=(2, 3))
print("Generated 2x3 random uniform values in [0,1):")
print(x1)
print("Important Note: By default, values lie between 0.0 and 1.0.\n")


# ------------------------------
# Example 2: Uniform Distribution with Custom Range
# ------------------------------
print("="*70)
print("EXAMPLE 2: Generate Uniform Distribution with low=5, high=10, size=5")
print("="*70)

x2 = random.uniform(low=5, high=10, size=5)
print("Generated 5 random uniform values between [5,10):")
print(x2)
print("Important Note: Every value between 5 and 10 is equally likely.\n")


# ------------------------------
# Example 3: Visualization of Uniform Distribution
# ------------------------------
print("="*70)
print("EXAMPLE 3: Visualizing Uniform Distribution (1000 samples, default range [0,1))")
print("="*70)

x3 = random.uniform(size=1000)
sns.displot(x3, kind="kde")
plt.title("Uniform Distribution (1000 samples, range [0,1))")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()

print("Observation:")
print("- The density plot is flat, meaning every value has equal probability.")
print("- Unlike Normal distribution (bell-shaped), Uniform is constant across the interval.\n")


# ------------------------------
# Example 4: Visualization of Custom Uniform Range
# ------------------------------
print("="*70)
print("EXAMPLE 4: Visualizing Uniform Distribution with Range [10, 20)")
print("="*70)

x4 = random.uniform(low=10, high=20, size=1000)
sns.displot(x4, kind="kde")
plt.title("Uniform Distribution (1000 samples, range [10,20))")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()

print("Observation:")
print("- Distribution is still flat (constant probability).")
print("- Only the interval has shifted to [10,20).\n")

print("✅ All Uniform Distribution demonstrations completed successfully!")
