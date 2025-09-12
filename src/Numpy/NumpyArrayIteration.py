"""
NumPy Array Iteration Tutorial
-------------------------------
This script demonstrates how to iterate over NumPy arrays in different ways.

Concepts Covered:
1. Iterating 1-D arrays
2. Iterating 2-D arrays
3. Iterating down to scalars in multi-dimensional arrays
4. Iterating 3-D arrays
5. Iterating with np.nditer()
6. Iterating with dtype conversion and buffer
7. Iterating with step sizes
8. Enumerated iteration using ndenumerate()

Important Notes:
- Iterating a NumPy array depends on its dimensions.
- For higher-dimensional arrays, we need nested loops unless we use np.nditer().
- np.nditer() makes iteration simpler and more powerful.
- ndenumerate() allows us to get both element and index.
"""

import numpy as np

print("\n========== 1. Iterating 1-D Array ==========\n")

arr1d = np.array([1, 2, 3])
print("Original 1-D Array:", arr1d)
print("Iterating through each element:")
for x in arr1d:
    print("Value:", x)

print("\n========== 2. Iterating 2-D Array ==========\n")

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Original 2-D Array:\n", arr2d)
print("Iterating row by row:")
for row in arr2d:
    print("Row:", row)

print("\nIterating down to each scalar:")
for row in arr2d:
    for val in row:
        print("Value:", val)

print("\nImportant Note: For multi-dimensional arrays, basic iteration goes one dimension at a time.\n")

print("\n========== 3. Iterating 3-D Array ==========\n")

arr3d = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[7, 8, 9], [10, 11, 12]]])

print("Original 3-D Array:\n", arr3d)
print("Iterating 2-D blocks of the 3-D array:")
for block in arr3d:
    print("2-D Block:\n", block)

print("\nIterating down to scalars in 3-D array:")
for block in arr3d:
    for row in block:
        for val in row:
            print("Value:", val)

print("\n========== 4. Iterating Using np.nditer() ==========\n")

arr_nditer = np.array([[[1, 2], [3, 4]],
                       [[5, 6], [7, 8]]])
print("Original Array:\n", arr_nditer)
print("Iterating through all scalars using np.nditer():")
for x in np.nditer(arr_nditer):
    print("Value:", x)

print("\nImportant Note: np.nditer() flattens iteration for any dimension.\n")

print("\n========== 5. Iterating With Different Data Types ==========\n")

arr_dtype = np.array([1, 2, 3])
print("Original Array:", arr_dtype)
print("Iterating as strings using nditer with buffer:")
for x in np.nditer(arr_dtype, flags=['buffered'], op_dtypes=['S']):
    print("Value as string:", x)

print("\nImportant Note: Buffered iteration allows temporary conversion without changing original array.\n")

print("\n========== 6. Iterating With Step Size ==========\n")

arr_step = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8]])
print("Original Array:\n", arr_step)
print("Iterating every other column (step=2):")
for x in np.nditer(arr_step[:, ::2]):
    print("Value:", x)

print("\n========== 7. Enumerated Iteration Using ndenumerate() ==========\n")

arr_enum1d = np.array([1, 2, 3])
print("Enumerating elements of 1-D array:")
for idx, val in np.ndenumerate(arr_enum1d):
    print(f"Index {idx} -> Value {val}")

arr_enum2d = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8]])
print("\nEnumerating elements of 2-D array:")
for idx, val in np.ndenumerate(arr_enum2d):
    print(f"Index {idx} -> Value {val}")

print("\n========== END OF NUMPY ARRAY ITERATION DEMO ==========\n")
