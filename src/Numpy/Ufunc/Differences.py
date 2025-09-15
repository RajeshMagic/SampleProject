############################################
# Python Demonstration: NumPy Differences
#
# This script demonstrates:
# - Discrete differences using np.diff()
# - Higher order differences using parameter n
# - Visualization of differences
# - Console outputs with Important Notes
############################################

import numpy as np
import matplotlib.pyplot as plt

print("\n==============================================")
print("         Demonstration: NumPy Differences")
print("==============================================\n")

############################################
# Example 1: Discrete Difference
############################################
print("--- Example 1: Discrete Difference ---")

arr = np.array([10, 15, 25, 5])
diff1 = np.diff(arr)

print("Original Array:", arr)
print("Discrete Difference (n=1):", diff1)
print("Important Note: Each element is subtracted from the next (arr[i+1] - arr[i]).\n")

############################################
# Example 2: Higher Order Difference
############################################
print("--- Example 2: Higher Order Difference ---")

diff2 = np.diff(arr, n=2)
print("Original Array:", arr)
print("Discrete Difference (n=2):", diff2)
print("Important Note: n=2 performs the difference operation twice successively.\n")

############################################
# Example 3: Visualization
############################################
print("--- Example 3: Visualization ---")

x = np.arange(len(arr))
plt.figure(figsize=(10, 6))
plt.plot(x, arr, marker="o", linestyle="--", label="Original Array", color="blue")

# For n=1, plot diff values at positions 1..len(arr)-1
plt.plot(x[1:], diff1, marker="s", linestyle="-", label="Difference n=1", color="red")

# For n=2, plot diff values at positions 2..len(arr)-1
plt.plot(x[2:], diff2, marker="^", linestyle="-.", label="Difference n=2", color="green")

plt.title("Discrete Differences in NumPy")
plt.xlabel("Index")
plt.ylabel("Value / Difference")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

############################################
# Summary
############################################
print("\n==============================================")
print("SUMMARY:")
print("- np.diff() calculates discrete differences between successive elements.")
print("- The 'n' parameter allows higher-order differences.")
print("- Visualization helps see how differences change relative to the original array.")
print("==============================================\n")
