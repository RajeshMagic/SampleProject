"""
NumPy Data Types Tutorial
-------------------------
This script demonstrates the following concepts in NumPy:
1. Checking data types of arrays
2. Creating arrays with a defined data type (dtype)
3. Converting data types of existing arrays
4. Handling errors during data type conversion
"""

import numpy as np

print("\n========== 1. Checking the Data Type of an Array ==========\n")

# Array of integers
arr_int = np.array([1, 2, 3, 4])
print("Array of integers:", arr_int)
print("Data type:", arr_int.dtype)

# Array of strings
arr_str = np.array(['apple', 'banana', 'cherry'])
print("\nArray of strings:", arr_str)
print("Data type:", arr_str.dtype)

# Array of floats
arr_float = np.array([1.1, 2.2, 3.3])
print("\nArray of floats:", arr_float)
print("Data type:", arr_float.dtype)

print("\nImportant Note: The dtype property tells the type of elements in the array.\n")

print("\n========== 2. Creating Arrays With a Defined Data Type ==========\n")

# Create array with string data type
arr_s = np.array([1, 2, 3, 4], dtype='S')  # 'S' means string
print("Array with dtype='S':", arr_s)
print("Data type:", arr_s.dtype)

# Create array with 4-byte integers
arr_i4 = np.array([1, 2, 3, 4], dtype='i4')  # 'i4' means 4-byte integer
print("\nArray with dtype='i4':", arr_i4)
print("Data type:", arr_i4.dtype)

print("\nImportant Note: NumPy allows specifying the data type while creating arrays using dtype argument.\n")

print("\n========== 3. Handling Conversion Errors ==========\n")

# Example: Cannot convert non-integer string to integer
try:
    arr_invalid = np.array(['a', '2', '3'], dtype='i')
except ValueError as e:
    print("Error while converting ['a','2','3'] to integer:", e)

print("\nImportant Note: If a value cannot be converted to the specified dtype, NumPy raises ValueError.\n")

print("\n========== 4. Converting Data Type of Existing Arrays ==========\n")

# Converting float array to integer using 'i'
arr_float2 = np.array([1.1, 2.1, 3.1])
arr_int2 = arr_float2.astype('i')  # Convert using string dtype
print("Original float array:", arr_float2)
print("Converted to integer using 'i':", arr_int2)
print("Data type after conversion:", arr_int2.dtype)

# Convert using Python int type
arr_int3 = arr_float2.astype(int)
print("\nConverted to integer using int type:", arr_int3)
print("Data type after conversion:", arr_int3.dtype)

# Convert integer array to boolean
arr_bool = np.array([1, 0, 3])
arr_bool2 = arr_bool.astype(bool)
print("\nOriginal integer array:", arr_bool)
print("Converted to boolean:", arr_bool2)
print("Data type after conversion:", arr_bool2.dtype)

print("\nImportant Note: astype() creates a new array with the desired data type without modifying the original array.\n")

print("\n========== 5. Summary of NumPy Data Types ==========\n")
print("i - integer")
print("b - boolean")
print("u - unsigned integer")
print("f - float")
print("c - complex float")
print("m - timedelta")
print("M - datetime")
print("O - object")
print("S - string")
print("U - unicode string")
print("V - fixed chunk of memory for other type (void)\n")

print("========== END OF NUMPY DATA TYPES DEMO ==========\n")
