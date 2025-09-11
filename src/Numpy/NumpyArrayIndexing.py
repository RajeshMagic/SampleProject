"""
NumPy Array Indexing
--------------------
This script demonstrates how to access elements from NumPy arrays
using indexing for 1D, 2D, and 3D arrays, including negative indexing.

Important notes are printed for clarity.
"""

import numpy as np

print("\n========== 1-D Array Indexing ==========\n")

# Create a 1-D array
arr_1d = np.array([1, 2, 3, 4])
print("1-D Array:", arr_1d)

# Access the first element
print("First element (index 0):", arr_1d[0])

# Access the second element
print("Second element (index 1):", arr_1d[1])

# Access third and fourth elements and add them
sum_3_4 = arr_1d[2] + arr_1d[3]
print("Sum of third and fourth elements:", sum_3_4)
print("Important Note: Indexing starts from 0 in NumPy arrays.\n")

print("\n========== 2-D Array Indexing ==========\n")

# Create a 2-D array
arr_2d = np.array([[1, 2, 3, 4, 5], 
                   [6, 7, 8, 9, 10]])
print("2-D Array:\n", arr_2d)

# Access 2nd element on 1st row
print("2nd element on 1st row:", arr_2d[0, 1])

# Access 5th element on 2nd row
print("5th element on 2nd row:", arr_2d[1, 4])

# Negative indexing: access last element from 2nd row
print("Last element from 2nd row (negative indexing):", arr_2d[1, -1])
print("Important Note: In 2-D arrays, arr[row_index, column_index] is used.\n")

print("\n========== 3-D Array Indexing ==========\n")

# Create a 3-D array
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]],
                   [[7, 8, 9], [10, 11, 12]]])
print("3-D Array:\n", arr_3d)

# Access third element of second array of first array
element = arr_3d[0, 1, 2]
print("Element arr_3d[0, 1, 2]:", element)
print("""
Explanation:
- First index 0: selects the first array [[1,2,3],[4,5,6]]
- Second index 1: selects the second sub-array [4,5,6]
- Third index 2: selects the third element of that sub-array -> 6
""")

# Negative indexing in 3-D array
neg_index_element = arr_3d[1, -1, -2]
print("Element using negative indexing arr_3d[1, -1, -2]:", neg_index_element)
print("Explanation: Access last row of second array, then second last element -> 11")

print("\n========== Important Notes ==========\n")
print("1. Indexing starts from 0 in all dimensions.")
print("2. For multi-dimensional arrays, use comma-separated indices: arr[x, y, z,...]")
print("3. Negative indexing allows accessing elements from the end of the array.")
print("4. NumPy arrays support slicing and advanced indexing, which can be explored further.\n")

print("========== END OF DEMO ==========\n")
