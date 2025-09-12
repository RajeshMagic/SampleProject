"""
NumPy Sorting Arrays Tutorial
------------------------------
This script demonstrates:
1. Sorting numeric arrays
2. Sorting string arrays (alphabetical order)
3. Sorting boolean arrays
4. Sorting 2D arrays (row-wise sorting)

Important Notes:
- np.sort() always returns a **sorted copy** (original array is unchanged).
- Works on numbers, strings, and booleans.
- For 2D arrays, sorting happens row-wise by default.
"""

import numpy as np

print("\n========== 1. Sorting Numeric Arrays ==========\n")

arr = np.array([3, 2, 0, 1])
print("Original Array:", arr)

sorted_arr = np.sort(arr)
print("Sorted Array:", sorted_arr)

print("Important Note: np.sort() returns a new sorted copy.\n"
      "The original array remains unchanged.\n")

print("\n========== 2. Sorting String Arrays ==========\n")

arr = np.array(['banana', 'cherry', 'apple'])
print("Original String Array:", arr)

sorted_arr = np.sort(arr)
print("Sorted Alphabetically:", sorted_arr)

print("Important Note: Strings are sorted alphabetically (ASCII order).\n")

print("\n========== 3. Sorting Boolean Arrays ==========\n")

arr = np.array([True, False, True])
print("Original Boolean Array:", arr)

sorted_arr = np.sort(arr)
print("Sorted Boolean Array:", sorted_arr)

print("Important Note: False < True (so False comes first).\n")

print("\n========== 4. Sorting a 2D Array ==========\n")

arr = np.array([[3, 2, 4], [5, 0, 1]])
print("Original 2D Array:\n", arr)

sorted_arr = np.sort(arr)
print("Sorted 2D Array (row-wise):\n", sorted_arr)

print("Important Note: np.sort() sorts each row individually by default.\n")

print("\n========== END OF NUMPY SORTING ARRAYS DEMO ==========\n")
