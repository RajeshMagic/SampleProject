"""
=============================================================
 NumPy Tutorial Demo
=============================================================
 NumPy (Numerical Python) is a Python library used for:
   - Efficient numerical computing
   - Working with n-dimensional arrays
   - Vectorized operations (without loops)
   - Basis of pandas, TensorFlow, scikit-learn, etc.
=============================================================
"""

import numpy as np

print("\n🔹 WHAT IS NUMPY?")
print("NumPy is a library for numerical computing in Python.")
print("It provides ndarray (n-dimensional array) for fast operations.\n")

# -----------------------------------------------------------
# Normal Python List vs NumPy Array
# -----------------------------------------------------------
print("🔹 LIST vs NUMPY ARRAY DEMO\n")

# Python Lists
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

print("Python Lists:")
print("list1 =", list1)
print("list2 =", list2)
print("list1 + list2 =", list1 + list2)
print("👉 Important Note: '+' concatenates lists, does NOT add element-wise!\n")

# NumPy Arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("NumPy Arrays:")
print("arr1 =", arr1)
print("arr2 =", arr2)
print("arr1 + arr2 =", arr1 + arr2)
print("👉 Important Note: '+' performs ELEMENT-WISE addition with arrays!\n")

# -----------------------------------------------------------
# Key Features of NumPy Arrays
# -----------------------------------------------------------
print("🔹 KEY FEATURES OF NUMPY ARRAYS\n")

# 1. n-dimensional array (1D, 2D, 3D...)
a = np.array([1, 2, 3, 4])
matrix = np.array([[1, 2], [3, 4]])
tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("1D Array:", a)
print("2D Array (Matrix):\n", matrix)
print("3D Array (Tensor):\n", tensor, "\n")

# 2. Fast Element-wise Operations
print("2. Fast Element-wise Operations:")
print("a =", a)
print("Square of a:", a ** 2)
print("Sqrt of a:", np.sqrt(a), "\n")

# 3. Broadcasting
print("3. Broadcasting:")
arr3 = np.array([1, 2, 3])
print("arr3 =", arr3)
print("arr3 + 10 =", arr3 + 10)
print("👉 Broadcasting automatically expands scalar operations across the array!\n")

# 4. Built-in Functions
print("4. Built-in Functions:")
print("Sum of a:", np.sum(a))
print("Mean of a:", np.mean(a))
print("Min of a:", np.min(a))
print("Max of a:", np.max(a), "\n")

# 5. Integration with Linear Algebra
print("5. Linear Algebra Example with 2D Matrix:\n", matrix)
print("Transpose:\n", matrix.T)
print("Matrix Multiplication:\n", np.dot(matrix, matrix))
print("Determinant:", np.linalg.det(matrix))
print("Inverse:\n", np.linalg.inv(matrix), "\n")

# -----------------------------------------------------------
# Extra Notes for Understanding
# -----------------------------------------------------------
print("=============================================================")
print("✅ IMPORTANT NOTES")
print(" - Lists are flexible but slow for numerical operations.")
print(" - NumPy arrays are FAST, MEMORY-EFFICIENT, and support VECTORIZED operations.")
print(" - Broadcasting allows operations between different-shaped arrays.")
print(" - NumPy integrates tightly with data science & ML libraries.")
print("=============================================================\n")
