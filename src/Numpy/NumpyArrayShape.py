"""
NumPy Array Shape Tutorial
---------------------------
This script demonstrates the concept of array shape in NumPy.
The shape of an array defines the number of elements in each dimension.
We will cover:

1. Getting the shape of 1-D, 2-D, and higher-dimensional arrays
2. Creating arrays with multiple dimensions using ndmin
3. Understanding the shape tuple

Important Note:
- The shape attribute returns a tuple
- Each value in the tuple represents the number of elements in that dimension
"""

import numpy as np

print("\n========== 1. Shape of a 1-D Array ==========\n")

# 1-D array
arr1 = np.array([1, 2, 3, 4, 5])
print("Array:\n", arr1)
print("Shape of 1-D array:", arr1.shape)

print("\nImportant Note: A 1-D array has a single dimension with 5 elements.\n")

print("\n========== 2. Shape of a 2-D Array ==========\n")

# 2-D array
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Array:\n", arr2)
print("Shape of 2-D array:", arr2.shape)

print("\nExplanation: (2, 4) means 2 rows and 4 columns.\n")

print("\n========== 3. Shape of a 3-D Array ==========\n")

# 3-D array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Array:\n", arr3)
print("Shape of 3-D array:", arr3.shape)

print("\nExplanation: (2, 2, 3) means:")
print("- 2 arrays of 2x3 matrices each.\n")

print("\n========== 4. Creating Higher Dimensional Array with ndmin ==========\n")

# 5-D array using ndmin
arr5d = np.array([1, 2, 3, 4], ndmin=5)
print("Array with 5 dimensions:\n", arr5d)
print("Shape of 5-D array:", arr5d.shape)

print("\nExplanation: Shape tuple shows number of elements in each dimension.")
print("For example, shape (1, 1, 1, 1, 4) means 5 dimensions, last dimension has 4 elements.\n")

print("\n========== 5. Important Notes ==========\n")
print("- Shape is a tuple indicating the size of each dimension of the array.")
print("- You can use arr.shape to dynamically get dimensions for any array.")
print("- Combined with ndim attribute, you can get both the number of dimensions and their sizes.\n")

print("========== END OF NUMPY ARRAY SHAPE DEMO ==========\n")
