############################################
# Python Demonstration: NumPy Products
#
# This script demonstrates:
# - Total product using np.prod()
# - Product of multiple arrays
# - Product over an axis
# - Cumulative product using np.cumprod()
# - Visualization of cumulative product
# - Console outputs with Important Notes
############################################

import numpy as np
import matplotlib.pyplot as plt

print("\n==============================================")
print("         Demonstration: NumPy Products")
print("==============================================\n")

############################################
# Example 1: Product of a single array
############################################
print("--- Example 1: Product of a single array ---")

arr = np.array([1, 2, 3, 4])
product = np.prod(arr)
print("Array:", arr)
print("Product of all elements:", product)
print("Important Note: np.prod() multiplies all elements together.\n")

############################################
# Example 2: Product of multiple arrays
############################################
print("--- Example 2: Product of multiple arrays ---")

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

product_all = np.prod([arr1, arr2])
print("Arrays:", arr1, "and", arr2)
print("Product of all elements:", product_all)
print("Important Note: np.prod([arr1, arr2]) multiplies all elements across arrays.\n")

############################################
# Example 3: Product over an axis
############################################
print("--- Example 3: Product over an axis ---")

product_axis = np.prod([arr1, arr2], axis=1)
print("Arrays:", arr1, "and", arr2)
print("Product along axis=1:", product_axis)
print("Important Note: axis=1 calculates product row-wise.\n")

############################################
# Example 4: Cumulative Product
############################################
print("--- Example 4: Cumulative Product ---")

arr3 = np.array([5, 6, 7, 8])
cum_product = np.cumprod(arr3)
print("Array:", arr3)
print("Cumulative Product:", cum_product)
print("Important Note: np.cumprod() shows running product (partial multiplication).\n")

############################################
# Example 5: Visualization
############################################
print("--- Example 5: Visualization of Cumulative Product ---")

x = np.arange(1, len(arr3)+1)

plt.figure(figsize=(10, 6))
plt.plot(x, arr3, marker="o", linestyle="--", label="Original Values", color="blue")
plt.plot(x, cum_product, marker="s", linestyle="-", label="Cumulative Product", color="red")

plt.title("Cumulative Product Demonstration")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

############################################
# Summary
############################################
print("\n==============================================")
print("SUMMARY:")
print("- np.prod() multiplies all elements in an array.")
print("- np.prod() can handle multiple arrays.")
print("- axis parameter controls row/column-wise product.")
print("- np.cumprod() shows cumulative multiplication (partial products).")
print("- Visualization illustrates growth of cumulative product over array indices.")
print("==============================================\n")
