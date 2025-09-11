"""
NumPy Array Copy vs View Tutorial
---------------------------------
This script demonstrates the difference between a copy and a view of a NumPy array.
It covers the following concepts:
1. Creating a copy of an array
2. Creating a view of an array
3. Observing changes in original vs copy/view
4. Changing data in the view and observing effects
5. Checking ownership of data using the .base attribute
"""

import numpy as np

print("\n========== 1. Copy of an Array ==========\n")

# Original array
arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)

# Create a copy of the array
arr_copy = arr.copy()
print("Copy of array:", arr_copy)

# Change the original array
arr[0] = 42
print("\nAfter changing original array (arr[0] = 42):")
print("Original array:", arr)
print("Copy array (should NOT change):", arr_copy)

print("\nImportant Note: A copy owns its data. Changes to the original array do not affect the copy.\n")

print("\n========== 2. View of an Array ==========\n")

# Create a view of the array
arr_view = arr.view()
print("Original array:", arr)
print("View of array:", arr_view)

# Change the original array
arr[1] = 99
print("\nAfter changing original array (arr[1] = 99):")
print("Original array:", arr)
print("View array (should reflect changes):", arr_view)

print("\nImportant Note: A view shares the same data as the original array. Changes in one affect the other.\n")

print("\n========== 3. Change Data in the View ==========\n")

# Change the view
arr_view[2] = 77
print("After changing view (arr_view[2] = 77):")
print("Original array (should reflect changes):", arr)
print("View array:", arr_view)

print("\nImportant Note: Since view shares the same data, changes in the view affect the original array.\n")

print("\n========== 4. Check if Array Owns its Data ==========\n")

# Using .base attribute
copy_base = arr_copy.base
view_base = arr_view.base

print("Original array:", arr)
print("Copy array base attribute:", copy_base)   # Should be None
print("View array base attribute:", view_base)   # Should refer to original array

print("\nImportant Note:")
print("- Copy: .base is None, meaning it owns its data.")
print("- View: .base refers to the original array, meaning it does NOT own its data.\n")

print("========== END OF NUMPY COPY VS VIEW DEMO ==========\n")
