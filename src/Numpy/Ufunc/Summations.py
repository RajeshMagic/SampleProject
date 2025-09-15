############################################
# Python Demonstration: NumPy Summations
#
# This script demonstrates:
# - Difference between addition and summation
# - Summation over an axis
# - Cumulative summation
# - Visualization of summation vs cumulative sum
# - Console outputs with Important Notes
############################################

import numpy as np
import matplotlib.pyplot as plt

print("\n==============================================")
print("         Demonstration: NumPy Summations")
print("==============================================\n")

############################################
# Example 1: Addition vs Summation
############################################
print("--- Example 1: Addition vs Summation ---")

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

# Addition
addition_result = np.add(arr1, arr2)
print("Addition of arr1 and arr2 (element-wise):", addition_result)
print("Important Note: Addition is performed element by element.\n")

# Summation
summation_result = np.sum([arr1, arr2])
print("Summation of arr1 and arr2 (all elements together):", summation_result)
print("Important Note: Summation is over all elements combined.\n")

############################################
# Example 2: Summation Over an Axis
############################################
print("--- Example 2: Summation Over an Axis ---")

axis_sum = np.sum([arr1, arr2], axis=1)
print("Summation over axis=1 (row-wise):", axis_sum)
print("Important Note: With axis=1, each row/array is summed individually.\n")

############################################
# Example 3: Cumulative Summation
############################################
print("--- Example 3: Cumulative Summation ---")

arr3 = np.array([1, 2, 3, 4])
cumulative_sum = np.cumsum(arr3)

print("Original Array:", arr3)
print("Cumulative Sum :", cumulative_sum)
print("Important Note: cumsum() shows running total (partial sums).\n")

############################################
# Example 4: Visualization
############################################
print("--- Example 4: Visualization of Summation and Cumulative Sum ---")

x = np.arange(1, len(arr3) + 1)

plt.figure(figsize=(10, 6))
plt.plot(x, arr3, marker="o", label="Original Values", linestyle="--", color="blue")
plt.plot(x, cumulative_sum, marker="s", label="Cumulative Sum", linestyle="-", color="red")

plt.title("Cumulative Summation Demonstration")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

############################################
# Summary
############################################
print("\n==============================================")
print("SUMMARY:")
print("- Addition (np.add) is element-wise between two arrays.")
print("- Summation (np.sum) combines all elements into a single total.")
print("- Summation with axis parameter allows row/column-wise aggregation.")
print("- Cumulative Sum (np.cumsum) gives running totals of array elements.")
print("Visualization clearly shows cumulative growth over original values.")
print("==============================================\n")
