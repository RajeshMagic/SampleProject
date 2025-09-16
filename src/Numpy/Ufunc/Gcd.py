############################################
# Python Demonstration: NumPy GCD (Greatest Common Divisor / HCF)
#
# This script demonstrates:
# - GCD of two numbers
# - GCD of multiple numbers in an array
# - Visualization of GCD patterns
# - Console outputs with Important Notes
############################################

import numpy as np
import matplotlib.pyplot as plt

print("\n==============================================")
print("         Demonstration: NumPy GCD / HCF")
print("==============================================\n")

############################################
# Example 1: GCD of two numbers
############################################
print("--- Example 1: GCD of two numbers ---")

num1 = 6
num2 = 9
gcd_two = np.gcd(num1, num2)

print(f"Numbers: {num1} and {num2}")
print("GCD (HCF):", gcd_two)
print("Important Note: GCD is the largest number that divides both numbers exactly.\n")

############################################
# Example 2: GCD of an array of numbers
############################################
print("--- Example 2: GCD of an array of numbers ---")

arr = np.array([20, 8, 32, 36, 16])
gcd_array = np.gcd.reduce(arr)

print("Array:", arr)
print("GCD of array elements:", gcd_array)
print("Important Note: np.gcd.reduce() applies GCD successively across the array.\n")

############################################
# Example 3: Visualization of GCD patterns
############################################
print("--- Example 3: Visualization of GCD patterns ---")

x_vals = np.arange(1, 21)   # first 20 numbers
y_vals = np.arange(1, 21)
X, Y = np.meshgrid(x_vals, y_vals)
Z = np.gcd(X, Y)  # compute GCD for each pair

plt.figure(figsize=(8, 6))
plt.imshow(Z, origin="lower", cmap="viridis", extent=[1, 20, 1, 20])
plt.colorbar(label="GCD Value")
plt.title("Heatmap of GCD for Numbers 1–20")
plt.xlabel("First Number")
plt.ylabel("Second Number")
plt.grid(False)
plt.show()

print("Important Note: Heatmap shows GCD values for pairs of numbers 1–20.")
print("Diagonal values show the number itself (since GCD(n,n) = n).\n")

############################################
# Summary
############################################
print("\n==============================================")
print("SUMMARY:")
print("- np.gcd(x, y) calculates GCD of two numbers.")
print("- np.gcd.reduce(array) calculates GCD across multiple numbers.")
print("- GCD is useful in simplification, number theory, cryptography, etc.")
print("- Visualization helps see common factors between number pairs.")
print("==============================================\n")
