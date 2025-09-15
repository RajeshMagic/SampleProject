##########################################
# Python Demonstration: NumPy Log Functions
#
# This script demonstrates:
# - Log base 2 (np.log2)
# - Log base 10 (np.log10)
# - Natural log (np.log)
# - Custom log for any base (np.frompyfunc + math.log)
# - Visualization comparing different log bases
# - Console outputs with Important Notes
##########################################

import numpy as np
import matplotlib.pyplot as plt
from math import log

print("\n==============================================")
print("         Demonstration: NumPy Logs")
print("==============================================\n")

##########################################
# Base array for demonstration
##########################################
arr = np.arange(1, 10)  # numbers from 1 to 9
print("Array for demonstration:", arr, "\n")

##########################################
# Example 1: Log base 2
##########################################
print("--- Example 1: Log base 2 ---")
print("np.log2(arr):")
print(np.log2(arr))
print("Important Note: log2() is useful in computer science (binary systems).\n")

##########################################
# Example 2: Log base 10
##########################################
print("--- Example 2: Log base 10 ---")
print("np.log10(arr):")
print(np.log10(arr))
print("Important Note: log10() is often used in scientific data (orders of magnitude).\n")

##########################################
# Example 3: Natural Log (base e)
##########################################
print("--- Example 3: Natural Log (base e) ---")
print("np.log(arr):")
print(np.log(arr))
print("Important Note: log() defaults to base e (Euler’s number ≈ 2.718).\n")

##########################################
# Example 4: Log at Any Base (Custom ufunc)
##########################################
print("--- Example 4: Log at Any Base (Custom ufunc) ---")

# Create a custom ufunc
nplog = np.frompyfunc(log, 2, 1)

print("Log of 100 at base 15:", nplog(100, 15))
print("Important Note: np.frompyfunc creates universal functions,")
print("so we can compute log for any base using math.log.\n")

##########################################
# Visualization
##########################################
print("--- Example 5: Visualization of Logs ---")

x = np.linspace(1, 50, 500)  # range for visualization
y_log2 = np.log2(x)
y_log10 = np.log10(x)
y_ln = np.log(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y_log2, label="log2(x)", color="red")
plt.plot(x, y_log10, label="log10(x)", color="blue")
plt.plot(x, y_ln, label="ln(x)", color="green")
plt.title("Comparison of Logarithmic Functions in NumPy")
plt.xlabel("x")
plt.ylabel("log(x)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

##########################################
# Summary
##########################################
print("\n==============================================")
print("SUMMARY:")
print("- np.log2 : logarithm base 2 (binary).")
print("- np.log10: logarithm base 10 (common log).")
print("- np.log  : natural logarithm (base e).")
print("- Custom log can be built with np.frompyfunc and math.log.")
print("- Visualization shows growth rates differ by base.")
print("==============================================\n")
