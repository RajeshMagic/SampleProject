import scipy
from scipy import constants
import matplotlib.pyplot as plt

print("============================")
print("   SciPy Getting Started    ")
print("============================\n")

# ---------------------------------------------------------------
# 1. Installation Note (for learners)
# ---------------------------------------------------------------
print("[INFO] To install SciPy, use the following command in terminal:")
print("       pip install scipy")
print("If this fails, consider using a Python distribution like Anaconda (which comes with SciPy pre-installed).\n")

# ---------------------------------------------------------------
# 2. Importing SciPy and Constants
# ---------------------------------------------------------------
print("[STEP] Importing constants module from SciPy.")
print("[IMPORTANT NOTE] SciPy provides many physical and mathematical constants (e.g., speed of light, gravity, liter, etc.).\n")

# Example: How many cubic meters are in one liter
print("Example: 1 liter in cubic meters:")
print("constants.liter =", constants.liter, "cubic meters\n")

# ---------------------------------------------------------------
# 3. Exploring a few more SciPy constants
# ---------------------------------------------------------------
print("[STEP] Exploring some commonly used SciPy constants:")
print("Speed of Light (m/s):", constants.c)
print("Standard Gravity (m/s^2):", constants.g)
print("Planck Constant (Joule second):", constants.h)
print("Pi (mathematical constant):", constants.pi)

# ---------------------------------------------------------------
# 4. Visualization of some constants
# ---------------------------------------------------------------
print("\n[VISUALIZATION] Comparing magnitudes of selected SciPy constants.")

# Prepare data for visualization
constant_names = ["Speed of Light (c)", "Gravity (g)", "Planck Const (h)"]
constant_values = [constants.c, constants.g, constants.h]

plt.figure(figsize=(8, 5))
plt.bar(constant_names, constant_values, color=['blue', 'green', 'purple'])
plt.yscale('log')  # log scale because values differ greatly
plt.title("Comparison of SciPy Constants (log scale)")
plt.ylabel("Value (log scale)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# ---------------------------------------------------------------
# 5. Checking SciPy Version
# ---------------------------------------------------------------
print("\n[STEP] Checking SciPy Version:")
print("SciPy Version:", scipy.__version__)
print("\n[IMPORTANT NOTE] Use double underscores for __version__.\n")

print("============================")
print(" End of Getting Started Demo ")
print("============================")