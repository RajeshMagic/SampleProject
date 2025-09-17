"""
Matplotlib Line Demonstration
Author: OpenAI ChatGPT

This script demonstrates:
1. Different line styles (solid, dotted, dashed, dashdot)
2. Shorter syntax (ls, c)
3. Line colors (short, hex, named colors)
4. Line width customization
5. Multiple lines in one figure
6. Console outputs with 'Important Notes'
"""

# ---------------------------------------------------
# Import required modules
# ---------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

print("\n================= Matplotlib Line Tutorial =================\n")
print("Lines in Matplotlib can be customized with style, color, and width.")
print("Important Note: Use plt.plot(x, y, ...) with additional arguments like linestyle, color, linewidth.\n")

# ---------------------------------------------------
# Example 1: Dotted Line
# ---------------------------------------------------
print("[Example 1] Using a DOTTED line (linestyle='dotted').\n")

plt.figure(figsize=(6, 4))
plt.plot(ypoints, linestyle='dotted')
plt.title("Dotted Line Example")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 2: Dashed Line
# ---------------------------------------------------
print("[Example 2] Using a DASHED line (linestyle='dashed').\n")

plt.figure(figsize=(6, 4))
plt.plot(ypoints, linestyle='dashed')
plt.title("Dashed Line Example")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 3: Shorter Syntax for Linestyle
# ---------------------------------------------------
print("[Example 3] Shorter syntax for line style: ls=':', ls='--', ls='-.'\n")

plt.figure(figsize=(7, 5))
plt.plot(ypoints, ls=':', label="Dotted (ls=':')")
plt.plot(ypoints + 2, ls='--', label="Dashed (ls='--')")
plt.plot(ypoints + 4, ls='-.', label="Dashdot (ls='-.')")
plt.title("Short Syntax for Linestyles")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 4: Line Colors
# ---------------------------------------------------
print("[Example 4] Customizing line colors.")
print("-> Using short notation (c='r'), hex codes, and named colors.\n")

plt.figure(figsize=(7, 5))
plt.plot(ypoints, c='r', label="Red (c='r')")
plt.plot(ypoints + 2, c='#4CAF50', label="Hex Color #4CAF50")
plt.plot(ypoints + 4, c='hotpink', label="Named Color 'hotpink'")
plt.title("Line Colors")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 5: Line Width
# ---------------------------------------------------
print("[Example 5] Customizing line width with linewidth (lw).")
print("-> Here linewidth=5 for a thick line.\n")

plt.figure(figsize=(6, 4))
plt.plot(ypoints, color="blue", linewidth=5)
plt.title("Line Width Example (linewidth=5)")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 6: Multiple Lines (Separate plt.plot() calls)
# ---------------------------------------------------
print("[Example 6] Plotting multiple lines using multiple plt.plot() calls.\n")

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.figure(figsize=(7, 5))
plt.plot(y1, label="Line 1 (default x)")
plt.plot(y2, label="Line 2 (default x)")
plt.title("Multiple Lines (Separate Calls)")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 7: Multiple Lines (Single plt.plot() call with pairs)
# ---------------------------------------------------
print("[Example 7] Plotting multiple lines in a SINGLE plt.plot() call.")
print("-> Passing x1,y1,x2,y2 pairs.\n")

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.figure(figsize=(7, 5))
plt.plot(x1, y1, x2, y2)
plt.title("Multiple Lines (Single plt.plot Call)")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Conclusion
# ---------------------------------------------------
print("\n====================== Summary ======================\n")
print("1. Lines can be solid, dotted, dashed, or dashdot.")
print("2. Shorter syntax: ls for linestyle, c for color, lw for line width.")
print("3. Colors can be given as shorthand (r, g, b...), hex codes, or named colors.")
print("4. Line thickness is adjusted using linewidth (or lw).")
print("5. Multiple lines can be drawn with multiple plt.plot() calls or in a single call with pairs of x,y values.\n")
print("Important Note: These concepts are the foundation for styling plots in Matplotlib.\n")
print("=====================================================\n")
