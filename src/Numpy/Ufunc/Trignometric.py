############################################
# Python Demonstration: NumPy Trigonometric Functions
#
# Concepts Covered:
# - sin(), cos(), tan()
# - Degree ↔ Radian conversion
# - arcsin(), arccos(), arctan()
# - hypot() for hypotenuse calculation
# - Visualization of trig functions
# - Console explanations for clarity
############################################

import numpy as np
import matplotlib.pyplot as plt

print("\n==============================================")
print("       Demonstration: NumPy Trigonometric Functions")
print("==============================================\n")

############################################
# Example 1: Basic Trigonometric Functions
############################################
print("--- Example 1: sin(), cos(), tan() ---")

x = np.pi / 2
print(f"sin(pi/2) = {np.sin(x)}")
print(f"cos(pi/2) = {np.cos(x)}")
print(f"tan(pi/4) = {np.tan(np.pi/4)}")

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
print("\nArray of angles (radians):", arr)
print("Sine values:", np.sin(arr))
print("Cosine values:", np.cos(arr))
print("Tangent values:", np.tan(arr))

print("Important Note: Trigonometric functions in NumPy take radians as input.\n")

############################################
# Example 2: Degree ↔ Radian Conversion
############################################
print("--- Example 2: Degree ↔ Radian Conversion ---")

degrees = np.array([90, 180, 270, 360])
radians = np.deg2rad(degrees)
print("Degrees:", degrees)
print("Converted to Radians:", radians)

radians2 = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
degrees2 = np.rad2deg(radians2)
print("\nRadians:", radians2)
print("Converted to Degrees:", degrees2)

print("Important Note: rad = deg × (π/180),  deg = rad × (180/π).\n")

############################################
# Example 3: Inverse Trigonometric Functions
############################################
print("--- Example 3: Inverse Trigonometric Functions ---")

val = 1.0
angle = np.arcsin(val)
print(f"arcsin(1.0) = {angle} rad ({np.degrees(angle)} degrees)")

arr_vals = np.array([1, -1, 0.1])
print("Array values:", arr_vals)
print("arcsin results (radians):", np.arcsin(arr_vals))
print("arccos results (radians):", np.arccos(arr_vals))
print("arctan results (radians):", np.arctan(arr_vals))

print("Important Note: Inverse trig functions return angle in radians.\n")

############################################
# Example 4: Hypotenuse Calculation
############################################
print("--- Example 4: Hypotenuse Calculation ---")

base, perp = 3, 4
hyp = np.hypot(base, perp)
print(f"Base = {base}, Perpendicular = {perp}")
print("Hypotenuse =", hyp)
print("Important Note: hypot(x, y) = sqrt(x² + y²).\n")

############################################
# Visualization Section
############################################

# Visualization 1: sin, cos, tan waves
x_vals = np.linspace(-2*np.pi, 2*np.pi, 400)
sin_vals = np.sin(x_vals)
cos_vals = np.cos(x_vals)
tan_vals = np.tan(x_vals)

plt.figure(figsize=(12, 6))
plt.plot(x_vals, sin_vals, label="sin(x)")
plt.plot(x_vals, cos_vals, label="cos(x)")
plt.plot(x_vals, tan_vals, label="tan(x)", alpha=0.7)
plt.ylim(-5, 5)  # limit for better tan visualization
plt.title("Trigonometric Functions: sin, cos, tan")
plt.xlabel("Angle (radians)")
plt.ylabel("Function value")
plt.legend()
plt.grid(True)
plt.show()

# Visualization 2: Degree vs Radian Conversion
deg = np.linspace(0, 360, 361)
rad = np.deg2rad(deg)

plt.figure(figsize=(8, 5))
plt.plot(deg, rad, label="Radians = deg × π/180", color="purple")
plt.title("Degrees to Radians Conversion")
plt.xlabel("Degrees")
plt.ylabel("Radians")
plt.grid(True)
plt.legend()
plt.show()

############################################
# Summary
############################################
print("\n==============================================")
print("SUMMARY:")
print("- sin(), cos(), tan() compute trig values (input in radians).")
print("- np.deg2rad() and np.rad2deg() convert between degrees & radians.")
print("- arcsin(), arccos(), arctan() return angles from trig values.")
print("- np.hypot() computes hypotenuse using Pythagoras theorem.")
print("- Visualization helps understand trig wave patterns & conversions.")
print("==============================================\n")
