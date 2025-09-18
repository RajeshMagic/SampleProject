"""
Machine Learning: Normal Data Distribution
Author: OpenAI ChatGPT

This script demonstrates:
1. What a Normal (Gaussian) Distribution is
2. How to generate data with numpy.random.normal()
3. How mean and standard deviation affect the distribution
4. Visualizing with histograms (bell curve)
5. Step-by-step console explanations
"""

# ---------------------------------------------------
# Import required libraries
# ---------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

print("\n====================== Normal Data Distribution Demo ======================\n")
print("In statistics, the NORMAL distribution (Gaussian distribution) is the most")
print("common probability distribution. It is also called the 'Bell Curve'.\n")

# ---------------------------------------------------
# Step 1: Generate normally distributed data
# ---------------------------------------------------
print("[Step 1] Generating data with numpy.random.normal() ...")
print("Syntax: numpy.random.normal(loc, scale, size)")
print("  loc   = mean (center of distribution)")
print("  scale = standard deviation (spread of distribution)")
print("  size  = number of samples\n")

mean = 5.0
std_dev = 1.0
size = 100000

x = np.random.normal(mean, std_dev, size)

print(f"Generated {size} samples with mean={mean} and std_dev={std_dev}.")
print("Important Note: Most values are around 5.0, and rarely farther than ±1.0.\n")

# ---------------------------------------------------
# Step 2: Visualize with Histogram
# ---------------------------------------------------
print("[Step 2] Drawing histogram with 100 bins ...")
plt.hist(x, bins=100, color='skyblue', edgecolor='black')
plt.title("Normal Distribution (mean=5.0, std=1.0)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# ---------------------------------------------------
# Step 3: Compare different standard deviations
# ---------------------------------------------------
print("[Step 3] Effect of Standard Deviation on Distribution ...")
print(" - Smaller std_dev → values are tightly packed around the mean")
print(" - Larger std_dev  → values are more spread out\n")

x1 = np.random.normal(5.0, 0.5, 100000)  # narrower curve
x2 = np.random.normal(5.0, 2.0, 100000)  # wider curve

plt.hist(x1, bins=100, alpha=0.6, label='std_dev=0.5')
plt.hist(x2, bins=100, alpha=0.6, label='std_dev=2.0')
plt.legend()
plt.title("Effect of Standard Deviation on Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# ---------------------------------------------------
# Step 4: Compare different means
# ---------------------------------------------------
print("[Step 4] Effect of Mean on Distribution ...")
print(" - Mean shifts the curve left or right.")
print(" - Standard deviation remains the same.\n")

x3 = np.random.normal(2.0, 1.0, 100000)
x4 = np.random.normal(8.0, 1.0, 100000)

plt.hist(x3, bins=100, alpha=0.6, label='mean=2.0')
plt.hist(x4, bins=100, alpha=0.6, label='mean=8.0')
plt.legend()
plt.title("Effect of Mean on Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# ---------------------------------------------------
# Step 5: Summary of insights
# ---------------------------------------------------
print("\n====================== Summary ======================\n")
print("1. Normal Distribution is also called Gaussian or Bell Curve.")
print("2. Generated using numpy.random.normal(loc=mean, scale=std_dev, size=n).")
print("3. Mean (loc): shifts the curve left or right.")
print("4. Standard Deviation (scale): controls spread of data.")
print("   - Smaller std_dev → narrow, tall curve (values close to mean).")
print("   - Larger std_dev → wider, flatter curve (values spread out).")
print("5. Many real-world phenomena follow Normal Distribution (heights, exam scores, etc.).")
print("\n======================================================================\n")




"""
normal_distribution_demo.py
Normal (Gaussian) Distribution — 8 Graph Illustrations
Author: OpenAI ChatGPT

Demonstrates:
 - effect of mean and std, overlays, QQ-ish check via histogram+pdf, cumulative, sampling variability
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

print("\n===== NORMAL DISTRIBUTION: 8 ILLUSTRATIONS =====\n")
print("Normal distribution: bell curve (Gaussian).")
print("Use: numpy.random.normal(loc=mean, scale=stddev, size)\n")

fig, axs = plt.subplots(4, 2, figsize=(14, 12))
fig.suptitle("Normal Distribution — 8 Illustrations", fontsize=16)

# 1) N(0,1) small sample
x1 = np.random.normal(0, 1, 200)
axs[0,0].hist(x1, bins=20, edgecolor='black', color='lightblue')
axs[0,0].set_title("1) N(0,1) small sample (n=200)")

# 2) N(0,1) large sample
x2 = np.random.normal(0, 1, 100000)
axs[0,1].hist(x2, bins=100, edgecolor='black', color='lightgreen')
axs[0,1].set_title("2) N(0,1) large sample (n=100000)")

# 3) Changing stddev: narrow vs wide
x3a = np.random.normal(0, 0.5, 50000)
x3b = np.random.normal(0, 2.0, 50000)
axs[1,0].hist(x3a, bins=80, alpha=0.6, label='std=0.5')
axs[1,0].hist(x3b, bins=80, alpha=0.6, label='std=2.0')
axs[1,0].legend()
axs[1,0].set_title("3) Effect of Std Dev (0.5 vs 2.0)")

# 4) Changing mean: shift left/right
x4a = np.random.normal(-3, 1, 50000)
x4b = np.random.normal(3, 1, 50000)
axs[1,1].hist(x4a, bins=80, alpha=0.6, label='mean=-3')
axs[1,1].hist(x4b, bins=80, alpha=0.6, label='mean=3')
axs[1,1].legend()
axs[1,1].set_title("4) Effect of Mean (-3 vs 3)")

# 5) Overlay theoretical PDF on histogram
x5 = np.random.normal(5, 1, 20000)
axs[2,0].hist(x5, bins=70, density=True, alpha=0.6, edgecolor='black', label='Empirical')
xs = np.linspace(5-4, 5+4, 300)
axs[2,0].plot(xs, norm.pdf(xs, 5, 1), 'r-', lw=2, label='Theoretical PDF')
axs[2,0].legend()
axs[2,0].set_title("5) Empirical Histogram + Theoretical PDF (mean=5,std=1)")

# 6) Many small histograms (sampling variability)
for i in range(6):
    sample = np.random.normal(0,1,200)
    axs[2,1].plot(np.sort(sample), np.linspace(0,1,len(sample)), alpha=0.6)
axs[2,1].set_title("6) Empirical CDFs for several small samples")

# 7) QQ-like visual: sorted sample vs theoretical quantiles (approx)
sample7 = np.random.normal(0,1,1000)
theo_q = norm.ppf(np.linspace(0.001,0.999,len(sample7)))
axs[3,0].scatter(np.sort(sample7), theo_q, s=10)
axs[3,0].plot([-4,4], [-4,4], 'r--')
axs[3,0].set_title("7) QQ-ish plot (sample quantiles vs normal quantiles)")

# 8) Central Limit Theorem demo: means of small samples
means = [np.mean(np.random.normal(2,3,10)) for _ in range(20000)]
axs[3,1].hist(means, bins=80, color='salmon', edgecolor='black')
axs[3,1].set_title("8) CLT: Distribution of sample means (n=10)")

plt.tight_layout(rect=[0,0,1,0.96])
plt.show()

print("\nImportant Notes:")
print(" - Normal distribution is symmetric around the mean.")
print(" - PDF overlay in (5) shows empirical data matches theory for large n.")
print(" - CLT: averages of independent samples approach normality even if underlying variance is large.\n")
