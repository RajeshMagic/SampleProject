##########################################
# Python Demonstration: Create Your Own ufunc
#
# This script demonstrates:
# - Creating a custom ufunc with np.frompyfunc
# - Checking if functions are ufuncs
# - Comparison with built-in NumPy ufuncs
# - Visualization of results
# - Console outputs with Important Notes
##########################################

import numpy as np
import matplotlib.pyplot as plt

print("\n==============================================")
print("      Demonstration: Create Your Own ufunc")
print("==============================================\n")

##########################################
# Step 1: Define and Create Custom ufunc
##########################################
print("--- Example 1: Creating a custom ufunc ---")

# Define a simple addition function
def myadd(x, y):
    return x + y

# Convert it into a ufunc with frompyfunc
# Arguments: (function, number_of_inputs, number_of_outputs)
myadd_ufunc = np.frompyfunc(myadd, 2, 1)

print("Custom ufunc 'myadd_ufunc' created from Python function.")
print("Testing with arrays:")
print("Result:", myadd_ufunc([1, 2, 3, 4], [5, 6, 7, 8]))
print("Important Note: frompyfunc always returns Python objects, so dtype may differ from built-in ufuncs.\n")

##########################################
# Step 2: Check if Functions are ufuncs
##########################################
print("--- Example 2: Checking if functions are ufuncs ---")

print("Type of np.add:", type(np.add))
print("Type of np.concatenate:", type(np.concatenate))

try:
    print("Type of np.blahblah:", type(np.blahblah))  # this will raise AttributeError
except AttributeError as e:
    print("Error encountered:", e)

if type(np.add) == np.ufunc:
    print("✅ np.add is a ufunc")
else:
    print("❌ np.add is not a ufunc")

if type(np.concatenate) == np.ufunc:
    print("✅ np.concatenate is a ufunc")
else:
    print("❌ np.concatenate is NOT a ufunc")
print("\nImportant Note: Only functions of type 'numpy.ufunc' are universal functions.\n")

##########################################
# Step 3: Visualization – Built-in vs Custom ufunc
##########################################
print("--- Example 3: Visualization ---")

x = np.linspace(-10, 10, 100)

# Using built-in add ufunc
y_builtin = np.add(x, 5)

# Using custom myadd ufunc
y_custom = myadd_ufunc(x, 5)

plt.figure(figsize=(8, 5))
plt.plot(x, y_builtin, label="Built-in np.add", color="blue")
plt.plot(x, y_custom, "r--", label="Custom myadd_ufunc")
plt.title("Comparison: Built-in vs Custom ufunc")
plt.xlabel("Input x")
plt.ylabel("Output (x + 5)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

print("Important Note: Both built-in and custom ufuncs produce the same result,")
print("but built-in ufuncs are optimized (faster, support vectorization with C-level speed).\n")

##########################################
# Summary
##########################################
print("\n==============================================")
print("SUMMARY:")
print("- You can create custom ufuncs with np.frompyfunc.")
print("- Built-in ufuncs (like np.add, np.multiply) are highly optimized.")
print("- Checked if functions are ufuncs using type() and np.ufunc.")
print("- Demonstrated results via console and visualization.")
print("==============================================\n")
