"""
NumPy Searching Arrays Tutorial
-------------------------------
This script demonstrates:
1. Searching with np.where()
   - Finding indexes of a value
   - Finding indexes of even/odd values
2. Searching in sorted arrays with np.searchsorted()
   - Default (left insertion)
   - Right insertion (side='right')
   - Searching multiple values at once

Important Notes:
- np.where() returns indexes that satisfy a condition.
- np.searchsorted() is for sorted arrays and tells where a value
  should be inserted to maintain order.
"""

import numpy as np

print("\n========== 1. Searching with np.where() ==========\n")

arr = np.array([1, 2, 3, 4, 5, 4, 4])
print("Original Array:", arr)

# Find indexes where value == 4
indexes = np.where(arr == 4)
print("Indexes where arr == 4:", indexes)
print("Important Note: np.where() returns a tuple with index arrays.\n")

print("\n========== 2. Searching for Even Numbers ==========\n")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("Original Array:", arr)

even_indexes = np.where(arr % 2 == 0)
print("Indexes of even numbers:", even_indexes)
print("Even values are:", arr[even_indexes])
print("Important Note: Condition arr%2==0 selects even elements.\n")

print("\n========== 3. Searching for Odd Numbers ==========\n")

odd_indexes = np.where(arr % 2 == 1)
print("Indexes of odd numbers:", odd_indexes)
print("Odd values are:", arr[odd_indexes])
print("Important Note: Condition arr%2==1 selects odd elements.\n")

print("\n========== 4. Searching in Sorted Arrays with searchsorted() ==========\n")

arr = np.array([6, 7, 8, 9])
print("Sorted Array:", arr)

pos = np.searchsorted(arr, 7)
print("Index where 7 should be inserted (default/left):", pos)
print("Important Note: searchsorted() gives the leftmost valid insertion point.\n")

print("\n========== 5. Searching with side='right' ==========\n")

pos_right = np.searchsorted(arr, 7, side='right')
print("Index where 7 should be inserted (right side):", pos_right)
print("Important Note: side='right' returns the rightmost insertion point.\n")

print("\n========== 6. Searching Multiple Values ==========\n")

arr = np.array([1, 3, 5, 7])
print("Sorted Array:", arr)

positions = np.searchsorted(arr, [2, 4, 6])
print("Indexes where [2, 4, 6] should be inserted:", positions)
print("Important Note: np.searchsorted() can handle multiple values at once.\n")

print("\n========== END OF NUMPY SEARCHING ARRAYS DEMO ==========\n")
