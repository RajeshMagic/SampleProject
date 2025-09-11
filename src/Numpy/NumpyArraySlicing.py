"""
NumPy Array Slicing
-------------------
This script demonstrates how to slice NumPy arrays in 1D and 2D.
It includes examples for start:end slices, step slicing, negative slicing,
and multidimensional slicing.
"""

import numpy as np

print("\n========== 1-D Array Slicing ==========\n")

# Create a 1-D array
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7])
print("Original 1-D Array:", arr_1d)

# Slice elements from index 1 to index 5
slice1 = arr_1d[1:5]
print("Elements from index 1 to 5 (exclusive):", slice1)

# Slice elements from index 4 to the end
slice2 = arr_1d[4:]
print("Elements from index 4 to end:", slice2)

# Slice elements from beginning to index 4 (not included)
slice3 = arr_1d[:4]
print("Elements from beginning to index 4 (exclusive):", slice3)

# Negative slicing: slice from 3rd from end to 1st from end
slice4 = arr_1d[-3:-1]
print("Elements from -3 to -1 (exclusive):", slice4)

# Step slicing: return every other element from index 1 to index 5
slice5 = arr_1d[1:5:2]
print("Every other element from index 1 to 5:", slice5)

# Step slicing on entire array: every other element
slice6 = arr_1d[::2]
print("Every other element from entire array:", slice6)

print("Important Note: Slicing includes start index but excludes end index.\n")

print("\n========== 2-D Array Slicing ==========\n")

# Create a 2-D array
arr_2d = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10]])
print("Original 2-D Array:\n", arr_2d)

# From the second row, slice elements from index 1 to index 4
slice2d_1 = arr_2d[1, 1:4]
print("Second row, elements index 1 to 4:", slice2d_1)

# From both rows, return index 2 (third column)
slice2d_2 = arr_2d[0:2, 2]
print("All rows, index 2 (third column):", slice2d_2)

# From both rows, slice index 1 to index 4 (columns 2-4), return 2-D array
slice2d_3 = arr_2d[0:2, 1:4]
print("All rows, columns index 1 to 4:\n", slice2d_3)

print("\n========== Important Notes ==========\n")
print("1. For 1-D arrays: arr[start:end:step] selects elements from start to end-1.")
print("2. Omitting start defaults to 0, omitting end defaults to array length, omitting step defaults to 1.")
print("3. Negative indices allow slicing from the end of the array.")
print("4. For 2-D arrays: arr[row_start:row_end, col_start:col_end] selects subarrays.")
print("5. Slicing in 2-D can return 1-D or 2-D arrays depending on how many dimensions are sliced.\n")

print("========== END OF NUMPY ARRAY SLICING DEMO ==========\n")
