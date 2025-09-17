"""
SciPy Interpolation Demo
------------------------
This script demonstrates:
1. 1D Interpolation using interp1d()
2. Spline Interpolation using UnivariateSpline()
3. Radial Basis Function Interpolation using Rbf()

Each section explains:
- Purpose
- Example usage
- Console outputs with "Important Notes"
- Visualizations comparing original vs interpolated data
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, UnivariateSpline, Rbf

print("="*80)
print("                  SciPy Interpolation Demonstration")
print("="*80, "\n")

# -------------------------------------------------------------------
# Step 1: 1D Interpolation (Linear Example with interp1d)
# -------------------------------------------------------------------
print("Step 1: 1D Interpolation using interp1d()\n")

xs = np.arange(10)
ys = 2*xs + 1  # simple linear relation: y = 2x + 1

# Create interpolation function
interp_func_1d = interp1d(xs, ys)

# Interpolating between 2.1 and 2.9
new_xs = np.arange(2.1, 3, 0.1)
new_ys = interp_func_1d(new_xs)

print("Original xs:", xs)
print("Original ys:", ys)
print("Interpolated values between 2.1 and 2.9:", new_ys)
print("Important Note: interp1d only works within the range of given xs.")
print("Extrapolation outside the given range will throw an error.\n")
print("-"*80 + "\n")

# -------------------------------------------------------------------
# Step 2: Spline Interpolation (UnivariateSpline Example)
# -------------------------------------------------------------------
print("Step 2: Spline Interpolation using UnivariateSpline()\n")

xs2 = np.arange(10)
ys2 = xs2**2 + np.sin(xs2) + 1  # nonlinear relation

# Create spline interpolation
interp_func_spline = UnivariateSpline(xs2, ys2)

# Interpolating between 2.1 and 2.9
new_xs2 = np.arange(2.1, 3, 0.1)
new_ys2 = interp_func_spline(new_xs2)

print("Original xs2:", xs2)
print("Original ys2:", ys2)
print("Spline Interpolated values between 2.1 and 2.9:\n", new_ys2)
print("Important Note: Splines fit piecewise polynomials for smoother curves.")
print("They are especially useful when data is nonlinear.\n")
print("-"*80 + "\n")

# -------------------------------------------------------------------
# Step 3: Radial Basis Function Interpolation (Rbf Example)
# -------------------------------------------------------------------
print("Step 3: Radial Basis Function Interpolation using Rbf()\n")

xs3 = np.arange(10)
ys3 = xs3**2 + np.sin(xs3) + 1  # same nonlinear data

# Create RBF interpolation
interp_func_rbf = Rbf(xs3, ys3)

# Interpolating between 2.1 and 2.9
new_xs3 = np.arange(2.1, 3, 0.1)
new_ys3 = interp_func_rbf(new_xs3)

print("Original xs3:", xs3)
print("Original ys3:", ys3)
print("RBF Interpolated values between 2.1 and 2.9:\n", new_ys3)
print("Important Note: RBF uses radial basis functions for interpolation.")
print("It is flexible and works well with scattered/multidimensional data.\n")
print("-"*80 + "\n")

# -------------------------------------------------------------------
# Step 4: Visualization of All Interpolations
# -------------------------------------------------------------------
print("Step 4: Visualization\n")
print("Plotting original data vs interpolated curves for all methods...")

fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# 1D Interpolation plot
axs[0].plot(xs, ys, "o", label="Original Data")
axs[0].plot(new_xs, new_ys, "r-", label="Interpolated (interp1d)")
axs[0].set_title("1D Interpolation (interp1d)")
axs[0].legend()
axs[0].grid(True)

# Spline Interpolation plot
axs[1].plot(xs2, ys2, "o", label="Original Data")
axs[1].plot(new_xs2, new_ys2, "g-", label="Spline Interpolation")
axs[1].set_title("Spline Interpolation (UnivariateSpline)")
axs[1].legend()
axs[1].grid(True)

# RBF Interpolation plot
axs[2].plot(xs3, ys3, "o", label="Original Data")
axs[2].plot(new_xs3, new_ys3, "m-", label="RBF Interpolation")
axs[2].set_title("Radial Basis Function Interpolation (Rbf)")
axs[2].legend()
axs[2].grid(True)

plt.suptitle("SciPy Interpolation Methods", fontsize=16)
plt.show()

print("="*80)
print(" 🎉 End of SciPy Interpolation Demo 🎉 ")
print("="*80)
