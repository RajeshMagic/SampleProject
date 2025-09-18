"""
Probability Distribution Demo: Uniform Distribution
Author: OpenAI ChatGPT
"""

import numpy as np
import matplotlib.pyplot as plt

print("\n================ Uniform Distribution =================\n")
print("Uniform distribution: All values in a given range are equally likely.")
print("Example: Rolling a fair dice (1–6 each has equal probability).\n")

# Small dataset
x_small = np.random.uniform(0.0, 10.0, 20)
print("[Small Dataset] 20 random numbers between 0 and 10:")
print(x_small, "\n")

# Large dataset for visualization
x_large = np.random.uniform(0.0, 10.0, 100000)

print("[Large Dataset] Generated 100,000 values between 0 and 10.")
print("Important: All ranges are equally probable.\n")

plt.hist(x_large, bins=20, color='skyblue', edgecolor='black')
plt.title("Uniform Distribution (0 to 10)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

print("Summary: Uniform distribution creates flat histograms, since all values are equally likely.\n")



"""
Uniform Distribution Demo (8 Graph Illustrations)
Author: OpenAI ChatGPT
"""

import numpy as np
import matplotlib.pyplot as plt

print("\n================ Uniform Distribution Demo =================\n")
print("Uniform distribution: all values in a given range are equally likely.")
print("Example: rolling a fair dice → 1–6 equally probable.\n")

# Create figure grid (4x2 = 8 plots)
fig, axs = plt.subplots(4, 2, figsize=(12, 12))
fig.suptitle("Uniform Distribution - 8 Illustrations", fontsize=16)

# --- 1: Small dataset
x = np.random.uniform(0, 10, 20)
axs[0,0].hist(x, bins=10, color='skyblue', edgecolor='black')
axs[0,0].set_title("Small Sample (20 values)")

# --- 2: Large dataset
x = np.random.uniform(0, 10, 10000)
axs[0,1].hist(x, bins=20, color='lightgreen', edgecolor='black')
axs[0,1].set_title("Large Sample (10,000 values)")

# --- 3: Different range (0–1)
x = np.random.uniform(0, 1, 10000)
axs[1,0].hist(x, bins=10, color='orange', edgecolor='black')
axs[1,0].set_title("Range 0–1")

# --- 4: Range (50–100)
x = np.random.uniform(50, 100, 10000)
axs[1,1].hist(x, bins=20, color='purple', edgecolor='black')
axs[1,1].set_title("Range 50–100")

# --- 5: Compare 2 ranges (0–1 vs 0–10)
axs[2,0].hist(np.random.uniform(0,1,10000), bins=10, alpha=0.5, label="0–1")
axs[2,0].hist(np.random.uniform(0,10,10000), bins=10, alpha=0.5, label="0–10")
axs[2,0].set_title("Comparison of Ranges")
axs[2,0].legend()

# --- 6: Few bins vs many bins
x = np.random.uniform(0, 10, 10000)
axs[2,1].hist(x, bins=5, alpha=0.6, label="5 bins")
axs[2,1].hist(x, bins=50, alpha=0.6, label="50 bins")
axs[2,1].set_title("Effect of Bins")
axs[2,1].legend()

# --- 7: Uniform vs Normal comparison
x1 = np.random.uniform(0,10,10000)
x2 = np.random.normal(5,2,10000)
axs[3,0].hist(x1, bins=30, alpha=0.5, label="Uniform")
axs[3,0].hist(x2, bins=30, alpha=0.5, label="Normal")
axs[3,0].set_title("Uniform vs Normal")
axs[3,0].legend()

# --- 8: Cumulative Distribution
x = np.random.uniform(0,10,10000)
axs[3,1].hist(x, bins=50, cumulative=True, color='red', edgecolor='black')
axs[3,1].set_title("Cumulative Distribution")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

print("Important Notes:")
print(" - Uniform distribution produces flat histograms.")
print(" - Range changes the spread of values.")
print(" - All values inside the range are equally probable.\n")
