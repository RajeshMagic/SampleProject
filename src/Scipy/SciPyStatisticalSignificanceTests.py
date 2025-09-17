"""
SciPy Statistical Significance Tests Demo
-----------------------------------------
This script demonstrates:
1. Hypothesis Testing Basics (Null vs Alternate)
2. T-Test using ttest_ind()
3. KS-Test using kstest()
4. Statistical Description using describe()
5. Normality Tests (skew, kurtosis, normaltest)

Each section includes:
- Clear explanations
- Console outputs with "Important Notes"
- Visualizations for intuitive understanding
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, kstest, describe, skew, kurtosis, normaltest

print("="*90)
print("             SciPy Statistical Significance Tests Demonstration")
print("="*90, "\n")

# -------------------------------------------------------------------
# Step 1: Hypothesis Basics
# -------------------------------------------------------------------
print("Step 1: Hypothesis Basics")
print("Null Hypothesis (H0): The observation is due to chance / not significant.")
print("Alternate Hypothesis (H1): The observation is due to a real effect.\n")
print("Example: Student performance")
print(" - H0: Student is worse than average")
print(" - H1: Student is better than average")
print("Important Note: Tests can be one-tailed or two-tailed depending on directionality.\n")
print("-"*90 + "\n")

# -------------------------------------------------------------------
# Step 2: T-Test
# -------------------------------------------------------------------
print("Step 2: T-Test using ttest_ind()\n")

v1 = np.random.normal(size=100)  # sample from normal distribution
v2 = np.random.normal(size=100)

res_ttest = ttest_ind(v1, v2)
print("T-Test Result (statistic, pvalue):", res_ttest)
print("Extracted p-value only:", res_ttest.pvalue)
print("Important Note: If p-value <= alpha (e.g. 0.05), reject H0 and accept H1.\n")

# Visualization of distributions
plt.figure(figsize=(7, 5))
plt.hist(v1, bins=15, alpha=0.6, label="Sample v1")
plt.hist(v2, bins=15, alpha=0.6, label="Sample v2")
plt.title("T-Test Example: Comparing Two Distributions")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()
print("-"*90 + "\n")

# -------------------------------------------------------------------
# Step 3: KS-Test
# -------------------------------------------------------------------
print("Step 3: KS-Test using kstest()\n")

v = np.random.normal(size=100)
res_ks = kstest(v, "norm")
print("KS-Test Result:", res_ks)
print("Important Note: KS-Test checks if data follows a distribution (default 2-sided).")
print("If p-value > 0.05, we usually accept null hypothesis (data fits normal distribution).\n")

# Visualization
plt.figure(figsize=(7, 5))
plt.hist(v, bins=20, density=True, alpha=0.6, label="Sample Data")
xs = np.linspace(min(v), max(v), 100)
plt.plot(xs, 1/np.sqrt(2*np.pi) * np.exp(-xs**2/2), 'r-', label="Normal PDF")
plt.title("KS-Test: Checking Normality of Data")
plt.legend()
plt.show()
print("-"*90 + "\n")

# -------------------------------------------------------------------
# Step 4: Statistical Description
# -------------------------------------------------------------------
print("Step 4: Statistical Description using describe()\n")

v_desc = np.random.normal(size=100)
res_desc = describe(v_desc)

print("Description of dataset:")
print(res_desc)
print("Important Note: Provides summary -> nobs, min/max, mean, variance, skewness, kurtosis.\n")

# Visualization: boxplot for summary
plt.figure(figsize=(6, 5))
plt.boxplot(v_desc)
plt.title("Boxplot: Statistical Summary Visualization")
plt.show()
print("-"*90 + "\n")

# -------------------------------------------------------------------
# Step 5: Normality Tests
# -------------------------------------------------------------------
print("Step 5: Normality Tests (Skewness, Kurtosis, Normaltest)\n")

v_norm = np.random.normal(size=100)

print("Skewness of data:", skew(v_norm))
print("Kurtosis of data:", kurtosis(v_norm))
print("Normality Test Result:", normaltest(v_norm))
print("Important Note:")
print(" - Skewness ~ 0 means symmetric distribution.")
print(" - Kurtosis < 0 means light tails, > 0 means heavy tails.")
print(" - normaltest() checks if data comes from a normal distribution.\n")

# Visualization: histogram of data
plt.figure(figsize=(7, 5))
plt.hist(v_norm, bins=20, alpha=0.7, color="green", edgecolor="black")
plt.title("Normality Check: Histogram of Data")
plt.show()

print("="*90)
print(" 🎉 End of SciPy Statistical Significance Tests Demo 🎉 ")
print("="*90)
