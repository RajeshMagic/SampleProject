##########################################
# Python Demonstration: Rounding Decimals in NumPy
#
# This script demonstrates:
# - Truncation (trunc, fix)
# - Rounding (around)
# - Floor
# - Ceil
# - Visualization comparing all methods
# - Console outputs with Important Notes
##########################################

import numpy as np
import matplotlib.pyplot as plt

print("\n==============================================")
print("     Demonstration: Rounding Decimals in NumPy")
print("==============================================\n")

# Test array with positive and negative decimals
arr = np.array([-3.1666, -1.5, -0.7, 0.2, 1.49, 2.5, 3.6667])

print("Original Array:", arr, "\n")

##########################################
# Truncation
##########################################
print("--- Example 1: Truncation ---")
print("Using np.trunc():", np.trunc(arr))
print("Using np.fix()  :", np.fix(arr))
print("Important Note: Both trunc() and fix() remove the decimal part.")
print(" - trunc() removes fractional part towards zero.\n")

##########################################
# Rounding (around)
##########################################
print("--- Example 2: Rounding with np.around() ---")
print("Rounded to 0 decimals:", np.around(arr, 0))
print("Rounded to 1 decimal :", np.around(arr, 1))
print("Important Note: around() increments if decimal >= 0.5.\n")

##########################################
# Floor
##########################################
print("--- Example 3: Floor ---")
print("Using np.floor():", np.floor(arr))
print("Important Note: floor() always rounds DOWN to nearest integer.\n")

##########################################
# Ceil
##########################################
print("--- Example 4: Ceil ---")
print("Using np.ceil():", np.ceil(arr))
print("Important Note: ceil() always rounds UP to nearest integer.\n")

##########################################
# Visualization
##########################################
print("--- Example 5: Visualization ---")

methods = {
    "Original": arr,
    "Trunc": np.trunc(arr),
    "Fix": np.fix(arr),
    "Around (0 decimals)": np.around(arr, 0),
    "Floor": np.floor(arr),
    "Ceil": np.ceil(arr)
}

plt.figure(figsize=(10, 6))
x_positions = np.arange(len(arr))

# Plot each method as a scatter for comparison
for i, (label, values) in enumerate(methods.items()):
    plt.scatter(x_positions + i*0.1, values, label=label)

plt.axhline(0, color="black", linestyle="--", linewidth=0.7)
plt.xticks(x_positions, [str(val) for val in arr])
plt.title("Comparison of Rounding Methods in NumPy")
plt.xlabel("Original Values")
plt.ylabel("Transformed Values")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

##########################################
# Summary
##########################################
print("\n==============================================")
print("SUMMARY:")
print("- trunc() and fix() remove decimals (towards zero).")
print("- around() performs conventional rounding.")
print("- floor() always rounds down, ceil() always rounds up.")
print("- Visualization shows how each method handles decimals.")
print("==============================================\n")
