############################################
# Python Demonstration: NumPy LCM (Lowest Common Multiple)
#
# This script demonstrates:
# - LCM of two numbers
# - LCM of multiple numbers in an array
# - LCM of a range of integers
# - Visualization to understand LCM growth
# - Console outputs with Important Notes
############################################

import numpy as np
import matplotlib.pyplot as plt

print("\n==============================================")
print("         Demonstration: NumPy LCM")
print("==============================================\n")

############################################
# Example 1: LCM of two numbers
############################################
print("--- Example 1: LCM of two numbers ---")

num1 = 4
num2 = 6
lcm_two = np.lcm(num1, num2)

print(f"Numbers: {num1} and {num2}")
print("LCM:", lcm_two)
print("Important Note: LCM is the smallest number divisible by both numbers.\n")

############################################
# Example 2: LCM of an array of numbers
############################################
print("--- Example 2: LCM of an array of numbers ---")

arr = np.array([3, 6, 9])
lcm_array = np.lcm.reduce(arr)

print("Array:", arr)
print("LCM of array elements:", lcm_array)
print("Important Note: np.lcm.reduce() applies LCM successively across the array.\n")

############################################
# Example 3: LCM of range 1 to 10
############################################
print("--- Example 3: LCM of integers from 1 to 10 ---")

arr_range = np.arange(1, 11)
lcm_range = np.lcm.reduce(arr_range)

print("Array:", arr_range)
print("LCM of 1 to 10:", lcm_range)
print("Important Note: LCM grows quickly as range increases, due to prime factors.\n")

############################################
# Example 4: Visualization
############################################
print("--- Example 4: Visualization of LCM Growth ---")

arr_values = np.arange(1, 21)
lcm_values = [np.lcm.reduce(arr_values[:i+1]) for i in range(len(arr_values))]

plt.figure(figsize=(10, 6))
plt.plot(arr_values, lcm_values, marker="o", linestyle="-", color="purple")
plt.title("LCM of First N Integers")
plt.xlabel("N (First N integers)")
plt.ylabel("LCM Value")
plt.yscale("log")  # use logarithmic scale due to rapid growth
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

############################################
# Summary
############################################
print("\n==============================================")
print("SUMMARY:")
print("- np.lcm(x, y) calculates LCM of two numbers.")
print("- np.lcm.reduce(array) calculates LCM across multiple numbers.")
print("- LCM can grow rapidly with increasing numbers due to primes.")
print("- Visualization (log scale) helps see growth trend clearly.")
print("==============================================\n")
