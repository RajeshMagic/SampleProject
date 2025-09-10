# ===============================================================
# PYTHON MATH - DEMONSTRATION
# ===============================================================
# Python provides:
#   1. Built-in math functions (like min, max, abs, pow).
#   2. The 'math' module, which contains advanced mathematical 
#      functions and constants like sqrt, ceil, floor, pi, etc.
# This script will demonstrate both, step by step.
# ===============================================================

import math

print("\n==============================")
print(" 1. BUILT-IN MATH FUNCTIONS ")
print("==============================")

# Finding minimum and maximum values
x = min(5, 10, 25)
y = max(5, 10, 25)
print("min(5, 10, 25) =", x)
print("max(5, 10, 25) =", y)
print("Important Note: min() finds the smallest, max() finds the largest among inputs.")

# Absolute value
a = abs(-7.25)
print("\nabs(-7.25) =", a)
print("Important Note: abs() always returns the positive magnitude of a number.")

# Power function
b = pow(4, 3)  # 4^3 = 64
print("\npow(4, 3) =", b)
print("Important Note: pow(x, y) returns x raised to the power of y (same as x ** y).")


print("\n==============================")
print(" 2. USING THE MATH MODULE ")
print("==============================")

# Square root
sq = math.sqrt(64)
print("math.sqrt(64) =", sq)
print("Important Note: math.sqrt() always returns a float result, even if the input is a perfect square.")

# Ceiling (round up) and Floor (round down)
ceil_val = math.ceil(1.4)
floor_val = math.floor(1.4)
print("\nmath.ceil(1.4) =", ceil_val, " -> rounds UP to nearest integer")
print("math.floor(1.4) =", floor_val, " -> rounds DOWN to nearest integer")

# Value of Pi
pi_val = math.pi
print("\nmath.pi =", pi_val)
print("Important Note: math.pi is a constant representing π (3.14159...).")


print("\n==============================")
print(" 3. EXTRA MATH METHODS (Useful Examples)")
print("==============================")

# Trigonometry
print("math.sin(90 degrees in radians) =", math.sin(math.radians(90)))
print("math.cos(0 degrees in radians) =", math.cos(math.radians(0)))
print("Important Note: math trigonometric functions take input in RADIANS, not degrees.")

# Exponential and Logarithms
exp_val = math.exp(2)   # e^2
log_val = math.log(10)  # natural log (base e)
log10_val = math.log10(100) # base-10 log
print("\nmath.exp(2) = e^2 =", exp_val)
print("math.log(10) = natural log of 10 =", log_val)
print("math.log10(100) = log base 10 of 100 =", log10_val)

# Factorial
fact_val = math.factorial(5)
print("\nmath.factorial(5) =", fact_val)
print("Important Note: factorial is only defined for non-negative integers.")


print("\n==============================")
print(" 4. ROUNDING & CONSTANTS ")
print("==============================")

print("math.e =", math.e)   # Euler’s number (2.718...)
print("math.tau =", math.tau) # Tau constant (2 * pi)
print("Important Note: math.e is the base of natural logarithms, math.tau = 2π.")


print("\n==============================")
print(" END OF PYTHON MATH DEMO ")
print("==============================\n")
