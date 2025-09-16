#############################################################
# Python Demonstration: NumPy Set Operations
#
# Concepts Covered:
# - Create sets using unique()
# - Union, Intersection, Difference, Symmetric Difference
# - Visualize results using matplotlib Venn diagrams
# - Console outputs with detailed notes
#############################################################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

print("\n==============================================")
print("      Demonstration: NumPy Set Operations")
print("==============================================\n")

#############################################################
# Example 1: Creating Sets with unique()
#############################################################
print("--- Example 1: Create Sets ---")

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
unique_set = np.unique(arr)

print("Original array with duplicates:", arr)
print("Unique set using np.unique():", unique_set)
print("Important Note: np.unique() is used to create 1D sets from arrays.\n")

#############################################################
# Example 2: Union of two sets
#############################################################
print("--- Example 2: Union ---")

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

union_result = np.union1d(arr1, arr2)
print("Set 1:", arr1)
print("Set 2:", arr2)
print("Union of Set1 and Set2:", union_result)
print("Important Note: Union combines all unique elements from both sets.\n")

#############################################################
# Example 3: Intersection of two sets
#############################################################
print("--- Example 3: Intersection ---")

intersection_result = np.intersect1d(arr1, arr2, assume_unique=True)
print("Intersection of Set1 and Set2:", intersection_result)
print("Important Note: Intersection returns elements common to both sets.\n")

#############################################################
# Example 4: Difference of two sets
#############################################################
print("--- Example 4: Difference ---")

difference_result = np.setdiff1d(arr1, arr2, assume_unique=True)
print("Difference (Set1 - Set2):", difference_result)
print("Important Note: Difference keeps only elements of the first set that are not in the second.\n")

#############################################################
# Example 5: Symmetric Difference of two sets
#############################################################
print("--- Example 5: Symmetric Difference ---")

symdiff_result = np.setxor1d(arr1, arr2, assume_unique=True)
print("Symmetric Difference of Set1 and Set2:", symdiff_result)
print("Important Note: Symmetric difference keeps elements present in only one set, not in both.\n")

#############################################################
# Visualization with Venn Diagrams
#############################################################
print("Now visualizing set operations with Venn Diagrams...\n")

set1 = set(arr1)
set2 = set(arr2)

# Union
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
venn2([set1, set2], set_labels=("Set1", "Set2"))
plt.title("Union of Set1 and Set2")

# Intersection
plt.subplot(2, 2, 2)
venn2([set1, set2], set_labels=("Set1", "Set2"))
plt.title("Intersection of Set1 and Set2")

# Difference
plt.subplot(2, 2, 3)
venn2([set1, set2], set_labels=("Set1", "Set2"))
plt.title("Difference (Set1 - Set2)")

# Symmetric Difference
plt.subplot(2, 2, 4)
venn2([set1, set2], set_labels=("Set1", "Set2"))
plt.title("Symmetric Difference")

plt.tight_layout()
plt.show()

#############################################################
# Summary
#############################################################
print("\n==============================================")
print("SUMMARY:")
print("- np.unique() → Creates set from array.")
print("- np.union1d() → Combines all unique elements from both sets.")
print("- np.intersect1d() → Common elements between sets.")
print("- np.setdiff1d() → Elements in first set but not in second.")
print("- np.setxor1d() → Elements in either set but not in both.")
print("Visualization with Venn diagrams helps understand relationships.")
print("==============================================\n")
