"""
NumPy Joining Arrays Tutorial
------------------------------
This script demonstrates how to join arrays in NumPy using:
1. concatenate()
2. stack()
3. hstack()
4. vstack()
5. dstack()

Important Notes:
- concatenate() joins along an existing axis.
- stack() joins along a NEW axis.
- hstack() stacks horizontally (rows).
- vstack() stacks vertically (columns).
- dstack() stacks along depth (3rd dimension).
"""

import numpy as np

print("\n========== 1. Joining Using concatenate() ==========\n")

# Example 1: Concatenate 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

joined_1d = np.concatenate((arr1, arr2))
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Joined 1-D Array (using concatenate):", joined_1d)
print("Important Note: concatenate() joins along an existing axis.\n")

# Example 2: Concatenate 2D arrays along columns (axis=1)
arr1_2d = np.array([[1, 2], [3, 4]])
arr2_2d = np.array([[5, 6], [7, 8]])

joined_2d = np.concatenate((arr1_2d, arr2_2d), axis=1)
print("Array 1 (2D):\n", arr1_2d)
print("Array 2 (2D):\n", arr2_2d)
print("Joined 2-D Array along axis=1:\n", joined_2d)

print("\n========== 2. Joining Using stack() ==========\n")

# Example: Stack 1D arrays along a new axis
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

stacked = np.stack((arr1, arr2), axis=1)
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Stacked (new axis, axis=1):\n", stacked)
print("Important Note: stack() creates a new axis unlike concatenate().\n")

print("\n========== 3. Stacking Along Rows (hstack) ==========\n")

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

h_stacked = np.hstack((arr1, arr2))
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Horizontally Stacked Array (hstack):", h_stacked)
print("Important Note: hstack() joins arrays along rows (like axis=1 for 2D arrays).\n")

print("\n========== 4. Stacking Along Columns (vstack) ==========\n")

v_stacked = np.vstack((arr1, arr2))
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Vertically Stacked Array (vstack):\n", v_stacked)
print("Important Note: vstack() joins arrays along columns (like axis=0 for 2D arrays).\n")

print("\n========== 5. Stacking Along Depth (dstack) ==========\n")

d_stacked = np.dstack((arr1, arr2))
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Depth Stacked Array (dstack):\n", d_stacked)
print("Shape of result:", d_stacked.shape)
print("Important Note: dstack() joins arrays along depth (3rd axis).\n")

print("\n========== END OF NUMPY ARRAY JOINING DEMO ==========\n")
