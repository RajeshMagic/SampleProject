"""
NumPy Array Reshaping Tutorial
-------------------------------
This script demonstrates how to reshape NumPy arrays.
Reshaping means changing the number of dimensions or shape of an array.

Concepts Covered:
1. Reshape 1-D array to 2-D array
2. Reshape 1-D array to 3-D array
3. Reshape constraints (elements must match)
4. Check if reshaped array is a view or copy
5. Using unknown dimension (-1)
6. Flattening arrays

Important Notes:
- The total number of elements must remain the same while reshaping.
- You can use -1 for one dimension, and NumPy calculates it automatically.
- Reshape usually returns a view, not a copy.
"""

import numpy as np

print("\n========== 1. Reshape 1-D to 2-D ==========\n")

# 1-D array with 12 elements
arr1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Original 1-D Array:\n", arr1d)

# Reshape to 2-D array: 4 rows, 3 columns
arr2d = arr1d.reshape(4, 3)
print("\nReshaped to 2-D Array (4x3):\n", arr2d)

print("\nImportant Note: Total elements must match. 1-D array of 12 elements becomes 4x3 = 12 elements in 2-D.\n")

print("\n========== 2. Reshape 1-D to 3-D ==========\n")

# Reshape to 3-D array: 2 arrays, each containing 3 arrays of 2 elements
arr3d = arr1d.reshape(2, 3, 2)
print("Reshaped to 3-D Array (2x3x2):\n", arr3d)

print("\nExplanation: Outermost dimension has 2 arrays, each containing 3 arrays with 2 elements.\n")

print("\n========== 3. Reshape Constraints ==========\n")

try:
    arr_invalid = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    arr_invalid.reshape(3, 3)
except ValueError as e:
    print("Error Example: Cannot reshape 8 elements to 3x3 array")
    print("Error Message:", e, "\n")

print("\n========== 4. Check if Reshape Returns View or Copy ==========\n")

arr_check = np.array([1, 2, 3, 4, 5, 6, 7, 8])
reshaped_arr = arr_check.reshape(2, 4)
print("Original Array:\n", arr_check)
print("Reshaped Array:\n", reshaped_arr)
print("Base of reshaped array (None = copy, else view):", reshaped_arr.base)

print("\nImportant Note: Reshaping usually returns a view, not a copy.\n")

print("\n========== 5. Using Unknown Dimension (-1) ==========\n")

arr_unknown = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# Automatically calculate last dimension
reshaped_unknown = arr_unknown.reshape(2, 2, -1)
print("Original Array:\n", arr_unknown)
print("Reshaped Array with -1:\n", reshaped_unknown)
print("Explanation: NumPy calculated the last dimension automatically.\n")

print("\n========== 6. Flattening Arrays ==========\n")

arr_to_flatten = np.array([[1, 2, 3], [4, 5, 6]])
print("Original 2-D Array:\n", arr_to_flatten)

# Flatten to 1-D array
flattened_arr = arr_to_flatten.reshape(-1)
print("Flattened 1-D Array:\n", flattened_arr)

print("\nImportant Note: reshape(-1) converts any multi-dimensional array into 1-D.\n")

print("========== END OF NUMPY ARRAY RESHAPING DEMO ==========\n")
