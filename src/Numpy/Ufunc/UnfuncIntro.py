##########################################
# Python Demonstration: NumPy ufuncs
#
# This script demonstrates:
# - What are ufuncs?
# - Why ufuncs are useful (speed, vectorization, broadcasting)
# - Difference between Python loops and ufuncs
# - Example with add()
# - Using ufunc methods: reduce, accumulate
# - Using arguments: where, dtype, out
# - Simple visualization of performance
# - Console outputs with Important Notes
##########################################

import numpy as np
import matplotlib.pyplot as plt
import time

print("\n==============================================")
print("         Demonstration: NumPy ufuncs")
print("==============================================\n")

##########################################
# Introduction
##########################################
print("What are ufuncs?")
print("-> ufuncs = Universal Functions in NumPy.")
print("-> They operate elementwise on ndarrays.")
print("-> They enable fast vectorized operations (no Python loops).")
print("\nWhy use ufuncs?")
print("- They are MUCH faster than Python loops.")
print("- Support broadcasting, reduce, accumulate, etc.")
print("- Accept extra arguments (where, dtype, out).\n")

##########################################
# Example 1: Adding two lists (loop vs ufunc)
##########################################
print("--- Example 1: Adding two lists ---")

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]

# Without ufuncs (Python loop)
z_loop = []
for i, j in zip(x, y):
    z_loop.append(i + j)

print("Result using loop:", z_loop)

# With ufunc (np.add)
z_ufunc = np.add(x, y)
print("Result using np.add:", z_ufunc)

print("Important Note: np.add is vectorized and works faster than explicit loops.\n")

##########################################
# Example 2: Vectorization Speed Comparison
##########################################
print("--- Example 2: Speed comparison: Loop vs np.add ---")

arr1 = np.arange(1, 1_000_01)
arr2 = np.arange(1, 1_000_01)

# Loop addition
start = time.time()
z_loop = [i + j for i, j in zip(arr1, arr2)]
end = time.time()
time_loop = end - start

# NumPy addition
start = time.time()
z_np = np.add(arr1, arr2)
end = time.time()
time_np = end - start

print(f"Time taken with loop: {time_loop:.5f} seconds")
print(f"Time taken with np.add: {time_np:.5f} seconds")
print("Important Note: NumPy ufuncs are highly optimized in C and vectorized.\n")

# Visualization of performance
plt.bar(["Python Loop", "NumPy ufunc"], [time_loop, time_np], color=["orange", "green"])
plt.title("Performance Comparison: Loop vs ufunc (Addition of 1M elements)")
plt.ylabel("Time (seconds)")
plt.show()

##########################################
# Example 3: Ufunc methods (reduce, accumulate)
##########################################
print("--- Example 3: Ufunc methods ---")

arr = np.array([1, 2, 3, 4])

# Using reduce (sum of array)
sum_reduce = np.add.reduce(arr)
print("np.add.reduce(arr):", sum_reduce)

# Using accumulate (cumulative sum)
sum_accumulate = np.add.accumulate(arr)
print("np.add.accumulate(arr):", sum_accumulate)

print("Important Note: reduce() collapses into a single value, accumulate() keeps partial results.\n")

##########################################
# Example 4: Extra arguments (where, dtype, out)
##########################################
print("--- Example 4: Extra arguments ---")

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])

# where: only apply addition at certain positions
result_where = np.add(arr1, arr2, where=[True, False, True, False])
print("Using 'where' mask:", result_where)

# dtype: force result into float
result_dtype = np.add(arr1, arr2, dtype=float)
print("Using 'dtype=float':", result_dtype)

# out: store result into pre-allocated array
out_arr = np.zeros(4, dtype=int)
np.add(arr1, arr2, out=out_arr)
print("Using 'out' array:", out_arr)

print("Important Note: 'where', 'dtype', and 'out' give fine control over operations.\n")

##########################################
# Summary
##########################################
print("\n==============================================")
print("SUMMARY:")
print("- ufuncs = Universal Functions in NumPy.")
print("- They provide fast, vectorized, elementwise operations.")
print("- Much faster than Python loops.")
print("- Provide methods like reduce, accumulate.")
print("- Support arguments: where, dtype, out.")
print("==============================================\n")
