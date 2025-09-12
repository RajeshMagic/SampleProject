"""
NumPy Splitting Arrays Tutorial
-------------------------------
This script demonstrates:
1. Splitting 1D arrays with array_split()
2. Difference between split() and array_split()
3. Accessing split arrays individually
4. Splitting 2D arrays row-wise and column-wise
5. Using hsplit() as an alternative method

Important Notes:
- Splitting is the reverse of joining.
- array_split() adjusts sizes automatically if elements do not divide evenly.
- split() is stricter and fails if sizes do not divide evenly.
- hsplit() is shorthand for splitting along columns (axis=1).
"""

import numpy as np

print("\n========== 1. Splitting 1D Array into Equal Parts ==========\n")

arr = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:", arr)

# Split into 3 parts
split_arr = np.array_split(arr, 3)
print("Split into 3 parts (array_split):", split_arr)
print("Important Note: array_split() always returns a list of arrays.\n")

print("\n========== 2. Splitting 1D Array into Uneven Parts ==========\n")

# Split into 4 parts (not divisible evenly)
split_arr_uneven = np.array_split(arr, 4)
print("Original Array:", arr)
print("Split into 4 parts (array_split):", split_arr_uneven)
print("Important Note: array_split() adjusts sizes when not divisible evenly.\n")

print("\n========== 3. Difference Between split() and array_split() ==========\n")

try:
    np.split(arr, 4)  # This will FAIL because array cannot be divided evenly
except ValueError as e:
    print("Using split(arr, 4) raises an ERROR because array cannot be split evenly.")
    print("Error Message:", e)
print("Important Note: Use array_split() for flexible splitting.\n")

print("\n========== 4. Accessing Splitted Arrays Individually ==========\n")

split_arr = np.array_split(arr, 3)
print("Original Array:", arr)
print("Splitted into 3 arrays:")
print("Part 1:", split_arr[0])
print("Part 2:", split_arr[1])
print("Part 3:", split_arr[2])
print("Important Note: The result of array_split() is a LIST of NumPy arrays.\n")

print("\n========== 5. Splitting 2D Arrays (Row-wise) ==========\n")

arr2d = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print("Original 2D Array:\n", arr2d)

split_2d = np.array_split(arr2d, 3)  # Split into 3 parts row-wise
print("Splitted into 3 parts (row-wise):")
for i, part in enumerate(split_2d, start=1):
    print(f"Part {i}:\n{part}")
print("Important Note: Default split is along axis=0 (rows).\n")

print("\n========== 6. Splitting 2D Arrays (Row-wise with 3 columns per row) ==========\n")

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],
                  [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print("Original 2D Array:\n", arr2d)

split_2d = np.array_split(arr2d, 3)
print("Split into 3 equal row-blocks:\n")
for i, part in enumerate(split_2d, start=1):
    print(f"Part {i}:\n{part}\n")

print("========== 7. Splitting 2D Arrays Along Columns (axis=1) ==========\n")

split_columns = np.array_split(arr2d, 3, axis=1)
print("Split into 3 parts column-wise (axis=1):")
for i, part in enumerate(split_columns, start=1):
    print(f"Part {i}:\n{part}\n")
print("Important Note: axis=1 means split along columns.\n")

print("\n========== 8. Using hsplit() Method ==========\n")

hsplit_arr = np.hsplit(arr2d, 3)
print("Splitting same 2D array into 3 column parts using hsplit():")
for i, part in enumerate(hsplit_arr, start=1):
    print(f"Part {i}:\n{part}\n")
print("Important Note: hsplit() is equivalent to array_split(arr, n, axis=1).\n")

print("\n========== END OF NUMPY ARRAY SPLITTING DEMO ==========\n")
