"""
Poisson Distribution Demonstration with NumPy, Matplotlib, and Seaborn
------------------------------------------------------------------------

Concept Recap:
--------------
1. Poisson Distribution is a DISCRETE probability distribution.
   - Example: Number of emails received per hour.
   - Possible outcomes: 0, 1, 2, 3, ... (unlimited).

2. Parameters:
   - lam   -> (λ) rate of occurrences (average events in a given time interval).
   - size  -> shape of the returned array (number of samples).

3. Relationship:
   - Normal vs Poisson:
        Normal is continuous, Poisson is discrete.
        For large λ, Poisson starts resembling Normal distribution.
   - Binomial vs Poisson:
        Binomial has only 2 outcomes (success/failure).
        Poisson can have unlimited outcomes.
        For large n and very small p, Binomial ≈ Poisson when n*p ≈ λ.
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# ------------------------------
# Example 1: Basic Poisson Distribution
# ------------------------------
print("\n" + "="*70)
print("EXAMPLE 1: Generate a Poisson Distribution with λ=2, size=10")
print("="*70)

x1 = random.poisson(lam=2, size=10)
print("Generated 10 random samples from Poisson distribution (λ=2):")
print(x1)
print("Important Note: Each value represents number of events occurring in a given time period.\n")


# ------------------------------
# Example 2: Visualization of Poisson Distribution
# ------------------------------
print("="*70)
print("EXAMPLE 2: Visualizing Poisson Distribution (λ=2, 1000 samples)")
print("="*70)

x2 = random.poisson(lam=2, size=1000)
sns.displot(x2, kde=False)  # histogram without KDE since Poisson is discrete
plt.title("Poisson Distribution (λ=2, 1000 samples)")
plt.xlabel("Number of Events")
plt.ylabel("Frequency")
plt.show()


# ------------------------------
# Example 3: Difference Between Normal and Poisson
# ------------------------------
print("="*70)
print("EXAMPLE 3: Comparing Normal vs Poisson Distribution")
print("="*70)

data1 = {
    "normal": random.normal(loc=50, scale=7, size=1000),  # continuous
    "poisson": random.poisson(lam=50, size=1000)          # discrete
}

sns.displot(data1, kind="kde")
plt.title("Comparison: Normal vs Poisson Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()

print("Observation:")
print("- Normal distribution is continuous → smooth curve.")
print("- Poisson distribution is discrete → step-like values.")
print("- For large λ, Poisson curve becomes similar to Normal.\n")


# ------------------------------
# Example 4: Difference Between Binomial and Poisson
# ------------------------------
print("="*70)
print("EXAMPLE 4: Comparing Binomial vs Poisson Distribution")
print("="*70)

data2 = {
    "binomial": random.binomial(n=1000, p=0.01, size=1000),  # large n, small p
    "poisson": random.poisson(lam=10, size=1000)             # λ ≈ n * p
}

sns.displot(data2, kind="kde")
plt.title("Comparison: Binomial vs Poisson Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()

print("Observation:")
print("- Binomial has only two outcomes (success/failure per trial).")
print("- Poisson counts number of events (can be unlimited).")
print("- For large n and small p (with n*p ≈ λ), Binomial ≈ Poisson.\n")

print("✅ All Poisson Distribution demonstrations completed successfully!")
