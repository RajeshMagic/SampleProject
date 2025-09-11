"""
NumPy Arrays - Creating and Understanding Dimensions
----------------------------------------------------
This program demonstrates how to create arrays in NumPy,
what dimensions mean, and how to check them using the `ndim` attribute.

Important notes are printed to the console for clarity.
"""

# Import NumPy
import numpy as np

print("\n========== NumPy Array Creation ==========\n")

# 1. Creating a NumPy array from a Python list
arr_list = np.array([1, 2, 3, 4, 5])
print("Array created from a Python list:", arr_list)
print("Type of arr_list:", type(arr_list))
print("Important Note: NumPy arrays are of type numpy.ndarray, not normal Python list.\n")

# 2. Creating a NumPy array from a Python tuple
arr_tuple = np.array((1, 2, 3, 4, 5))
print("Array created from a Python tuple:", arr_tuple, "\n")


print("\n========== Understanding Dimensions ==========\n")

# 0-D Array (Scalar)
arr_0d = np.array(42)
print("0-D Array (scalar value):", arr_0d)
print("Dimensions:", arr_0d.ndim)
print("Important Note: A single number is considered as 0-D array.\n")

# 1-D Array
arr_1d = np.array([1, 2, 3, 4, 5])
print("1-D Array:", arr_1d)
print("Dimensions:", arr_1d.ndim)
print("Important Note: This is the most common type of array, like a Python list but optimized.\n")

# 2-D Array (Matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2-D Array (Matrix):\n", arr_2d)
print("Dimensions:", arr_2d.ndim)
print("Important Note: Each row is a 1-D array, forming a 2-D matrix.\n")

# 3-D Array (Tensor)
arr_3d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]]
])
print("3-D Array (Tensor):\n", arr_3d)
print("Dimensions:", arr_3d.ndim)
print("Important Note: 3-D arrays are made of multiple 2-D arrays (matrices).\n")

# Checking number of dimensions with different arrays
print("\n========== Checking Dimensions with .ndim ==========\n")
a = np.array(42)  # 0-D
b = np.array([1, 2, 3, 4, 5])  # 1-D
c = np.array([[1, 2, 3], [4, 5, 6]])  # 2-D
d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]]
])  # 3-D

print("a (0-D):", a, "-> ndim =", a.ndim)
print("b (1-D):", b, "-> ndim =", b.ndim)
print("c (2-D):\n", c, "\n-> ndim =", c.ndim)
print("d (3-D):\n", d, "\n-> ndim =", d.ndim, "\n")

# Higher Dimensional Arrays using ndmin
print("\n========== Higher Dimensional Arrays (ndmin) ==========\n")
arr_highdim = np.array([1, 2, 3, 4], ndmin=5)
print("Array with ndmin=5:\n", arr_highdim)
print("Number of dimensions:", arr_highdim.ndim)
print("Important Note: ndmin lets you force an array into higher dimensions.\n")

print("\n========== END OF DEMO ==========\n")
