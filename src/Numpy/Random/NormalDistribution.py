"""
Normal (Gaussian) Distribution Demonstration with NumPy, Matplotlib, and Seaborn
-------------------------------------------------------------------------------

Concept Recap:
--------------
1. Normal Distribution is also called Gaussian Distribution.
2. It is one of the most important probability distributions.
3. Examples: IQ scores, heights, heartbeat rates, etc.
4. Formula controlled by:
   - loc   -> Mean (center of the bell curve)
   - scale -> Standard Deviation (spread/width of the curve)
   - size  -> Shape of array to generate

We will demonstrate:
- Generating normal distribution arrays with default and custom parameters
- Understanding effect of mean & standard deviation
- Visualization with Seaborn
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# Example 1: Basic Normal Distribution
# ------------------------------
print("\n" + "="*60)
print("EXAMPLE 1: Generate a random Normal Distribution with default parameters")
print("="*60)

x1 = random.normal(size=(2, 3))  # mean=0, std=1 by default
print("Generated Array (2x3) with default mean=0 and std=1:\n", x1)
print("Important Note: By default -> loc=0 (mean), scale=1 (std deviation).")


# ------------------------------
# Example 2: Normal Distribution with Custom Mean and Std
# ------------------------------
print("\n" + "="*60)
print("EXAMPLE 2: Normal Distribution with loc=1 (mean=1), scale=2 (std=2)")
print("="*60)

x2 = random.normal(loc=1, scale=2, size=(2, 3))
print("Generated Array (2x3) with mean=1 and std=2:\n", x2)
print("Important Note: loc shifts the curve center, scale controls spread.")


# ------------------------------
# Example 3: Large Sample for Visualization
# ------------------------------
print("\n" + "="*60)
print("EXAMPLE 3: Visualizing Normal Distribution using Seaborn")
print("="*60)

# Generate 1000 random numbers from a Normal distribution
x3 = random.normal(loc=0, scale=1, size=1000)

print("Generated 1000 random samples from N(0,1).")
print("Now plotting distribution curve...")

# Visualization
sns.displot(x3, kind="kde")  # KDE plot (smooth curve)
plt.title("Normal Distribution (mean=0, std=1, 1000 samples)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()

# ------------------------------
# Example 4: Comparing Different Distributions
# ------------------------------
print("\n" + "="*60)
print("EXAMPLE 4: Comparing Normal Distributions with Different Parameters")
print("="*60)

x4 = random.normal(loc=0, scale=1, size=1000)   # standard normal
x5 = random.normal(loc=5, scale=1, size=1000)   # shifted mean
x6 = random.normal(loc=0, scale=2, size=1000)   # larger spread

print("Plotted 3 different normal distributions:\n"
      "- Standard Normal: mean=0, std=1\n"
      "- Shifted Mean: mean=5, std=1\n"
      "- Wide Spread: mean=0, std=2")

# Visualization
sns.kdeplot(x4, label="N(0,1)", fill=True)
sns.kdeplot(x5, label="N(5,1)", fill=True)
sns.kdeplot(x6, label="N(0,2)", fill=True)

plt.title("Comparison of Normal Distributions")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.show()

print("\nAll demonstrations completed successfully ✅")
