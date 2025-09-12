"""
NumPy Filtering Arrays Tutorial
-------------------------------
This script demonstrates:
1. Basic filtering using a hardcoded boolean index list.
2. Creating filter arrays manually using conditions.
3. Filtering even numbers using custom filter array.
4. Using NumPy's direct conditional filtering (more efficient).
"""

import numpy as np

print("\n========== 1. Filtering with Hardcoded Boolean List ==========\n")

arr = np.array([41, 42, 43, 44])
print("Original Array:", arr)

# Boolean mask: True means keep the element, False means discard it
x = [True, False, True, False]
newarr = arr[x]

print("Boolean Mask:", x)
print("Filtered Array:", newarr)

print("Important Note: Only elements at positions where mask=True are selected.\n")


print("\n========== 2. Creating Filter Array Manually (Condition-based) ==========\n")

arr = np.array([41, 42, 43, 44])
print("Original Array:", arr)

# Create filter array manually: Keep only values > 42
filter_arr = []
for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print("Manual Filter Mask (Values > 42):", filter_arr)
print("Filtered Array (Values > 42):", newarr)

print("Important Note: Manual creation works, but it's not efficient.\n")


print("\n========== 3. Filtering Even Numbers Manually ==========\n")

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("Original Array:", arr)

filter_arr = []
for element in arr:
    if element % 2 == 0:   # Check if even
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]

print("Manual Filter Mask (Even Numbers):", filter_arr)
print("Filtered Array (Even Numbers):", newarr)

print("Important Note: Same logic but more typing. NumPy has a better way.\n")


print("\n========== 4. Filtering Using NumPy Direct Conditions ==========\n")

arr = np.array([41, 42, 43, 44])
print("Original Array:", arr)

# Direct filtering: No need for manual loops
filter_arr = arr > 42
newarr = arr[filter_arr]

print("Filter Mask (arr > 42):", filter_arr)
print("Filtered Array:", newarr)

print("\nAnother Example: Filtering Even Numbers\n")

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("Original Array:", arr)

filter_arr = arr % 2 == 0
newarr = arr[filter_arr]

print("Filter Mask (arr % 2 == 0):", filter_arr)
print("Filtered Array (Even Numbers):", newarr)

print("\n========== END OF NUMPY FILTER ARRAY DEMO ==========\n")
