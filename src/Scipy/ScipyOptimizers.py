import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root, minimize
from math import cos

print("============================")
print("     SciPy Optimizers       ")
print("============================\n")

# ---------------------------------------------------------------
# 1. Optimizers Introduction
# ---------------------------------------------------------------
print("[INFO] Optimizers in SciPy are used to either find the ROOT of an equation or MINIMIZE a function.")
print("\n[IMPORTANT NOTE] NumPy can solve polynomials/linear equations, but SciPy is needed for non-linear equations.\n")

# ---------------------------------------------------------------
# 2. Root Finding Example
# ---------------------------------------------------------------
print("============================")
print("     Root Finding           ")
print("============================")

def eqn(x):
    return x + cos(x)

print("Equation: f(x) = x + cos(x)")

# Initial guess x0 = 0
myroot = root(eqn, 0)

print("Root (solution for f(x)=0):", myroot.x)
print("\nFull details of root finding result:")
print(myroot)

# Visualization of the root
x_vals = np.linspace(-3, 3, 400)
y_vals = [eqn(x) for x in x_vals]

plt.figure(figsize=(7,4))
plt.axhline(0, color='black', linewidth=1)
plt.plot(x_vals, y_vals, label='f(x) = x + cos(x)')
plt.scatter(myroot.x, eqn(myroot.x), color='red', s=80, label='Root Found')
plt.title("Root Finding using SciPy optimize.root")
plt.legend()
plt.show()

# ---------------------------------------------------------------
# 3. Minimization Example
# ---------------------------------------------------------------
print("\n============================")
print("     Function Minimization  ")
print("============================")

def func(x):
    return x**2 + x + 2

print("Function: f(x) = x^2 + x + 2")

# Minimize using BFGS method
mymin = minimize(func, 0, method='BFGS')
print("Minimization Result (BFGS):")
print(mymin)

# Try another method (CG)
mymin_cg = minimize(func, 0, method='CG')
print("\nMinimization Result (CG):")
print(mymin_cg)

print("\n[IMPORTANT NOTE] Different methods may converge differently, but all aim to find a local minimum.")

# Visualization of minimization
x_vals = np.linspace(-10, 10, 400)
y_vals = func(x_vals)

plt.figure(figsize=(7,4))
plt.plot(x_vals, y_vals, label='f(x) = x^2 + x + 2')
plt.scatter(mymin.x, mymin.fun, color='red', s=80, label='Minimum Found (BFGS)')
plt.title("Function Minimization using SciPy optimize.minimize")
plt.legend()
plt.show()

# ---------------------------------------------------------------
# End of Demo
# ---------------------------------------------------------------
print("\n============================")
print(" End of Optimizers Demo ")
print("============================")