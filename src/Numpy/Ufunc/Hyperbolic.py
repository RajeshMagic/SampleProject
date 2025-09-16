############################################
# Python Demonstration: NumPy Hyperbolic Functions
#
# Concepts Covered:
# - sinh(), cosh(), tanh()
# - arcsinh(), arccosh(), arctanh()
# - Examples on single values & arrays
# - Visualization of hyperbolic functions
# - Console explanations for clarity
############################################

import numpy as np
import matplotlib.pyplot as plt

print("\n==============================================")
print("      Demonstration: NumPy Hyperbolic Functions")
print("==============================================\n")

############################################
# Example 1: Basic Hyperbolic Functions
############################################
print("--- Example 1: sinh(), cosh(), tanh() ---")

x = np.pi / 2
print(f"sinh(pi/2) = {np.sinh(x)}")
print(f"cosh(pi/2) = {np.cosh(x)}")
print(f"tanh(pi/2) = {np.tanh(x)}")

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
print("\nArray of angles (radians):", arr)
print("sinh values:", np.sinh(arr))
print("cosh values:", np.cosh(arr))
print("tanh values:", np.tanh(arr))

print("Important Note: Hyperbolic functions are similar to trig functions but based on exponential definitions.\n")

############################################
# Example 2: Inverse Hyperbolic Functions
############################################
print("--- Example 2: arcsinh(), arccosh(), arctanh() ---")

val = 1.0
angle_asinh = np.arcsinh(val)
print(f"arcsinh(1.0) = {angle_asinh} rad")

arr_asinh = np.array([1, 2, 3])
print("\nArray values:", arr_asinh)
print("arcsinh results (radians):", np.arcsinh(arr_asinh))

arr_acosh = np.array([2, 3, 4])  # acosh requires values >= 1
print("\nArray values for acosh:", arr_acosh)
print("arccosh results (radians):", np.arccosh(arr_acosh))

arr_atanh = np.array([0.1, 0.2, 0.5])  # atanh requires values in (-1, 1)
print("\nArray values for atanh:", arr_atanh)
print("arctanh results (radians):", np.arctanh(arr_atanh))

print("Important Note:")
print("- arcsinh works for all real numbers.")
print("- arccosh requires values >= 1.")
print("- arctanh requires values strictly between -1 and 1.\n")

############################################
# Visualization Section
############################################

# Visualization 1: sinh, cosh, tanh curves
x_vals = np.linspace(-3, 3, 400)
sinh_vals = np.sinh(x_vals)
cosh_vals = np.cosh(x_vals)
tanh_vals = np.tanh(x_vals)

plt.figure(figsize=(12, 6))
plt.plot(x_vals, sinh_vals, label="sinh(x)")
plt.plot(x_vals, cosh_vals, label="cosh(x)")
plt.plot(x_vals, tanh_vals, label="tanh(x)")
plt.title("Hyperbolic Functions: sinh, cosh, tanh")
plt.xlabel("x (radians)")
plt.ylabel("Function value")
plt.legend()
plt.grid(True)
plt.show()

# Visualization 2: Inverse hyperbolic functions
x_vals_inv = np.linspace(-2, 2, 400)
plt.figure(figsize=(12, 6))
plt.plot(x_vals_inv, np.arcsinh(x_vals_inv), label="arcsinh(x)")

# Restrict domain for arccosh (x >= 1)
x_vals_acosh = np.linspace(1, 5, 400)
plt.plot(x_vals_acosh, np.arccosh(x_vals_acosh), label="arccosh(x)")

# Restrict domain for arctanh (-1 < x < 1)
x_vals_atanh = np.linspace(-0.99, 0.99, 400)
plt.plot(x_vals_atanh, np.arctanh(x_vals_atanh), label="arctanh(x)")

plt.title("Inverse Hyperbolic Functions: arcsinh, arccosh, arctanh")
plt.xlabel("x")
plt.ylabel("Inverse Function value (radians)")
plt.legend()
plt.grid(True)
plt.show()

############################################
# Summary
############################################
print("\n==============================================")
print("SUMMARY:")
print("- sinh(), cosh(), tanh() compute hyperbolic trig values.")
print("- arcsinh(), arccosh(), arctanh() return angles in radians.")
print("- Domain Restrictions:")
print("   * arcsinh: all real numbers")
print("   * arccosh: input >= 1")
print("   * arctanh: -1 < input < 1")
print("- Visualization shows exponential-like growth of sinh, cosh, and bounded nature of tanh.")
print("==============================================\n")
