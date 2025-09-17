"""
Matplotlib Markers Demonstration
Author: OpenAI ChatGPT

This script demonstrates:
1. Using markers to emphasize points in plots
2. Marker reference options (circle, star, etc.)
3. Format strings (marker|line|color)
4. Customizing marker size, edge color, face color
5. Using hex color codes and named colors
6. Console outputs with 'Important Notes'
"""

# ---------------------------------------------------
# Import required modules
# ---------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

print("\n================= Matplotlib Markers Tutorial =================\n")
print("Markers are symbols used to highlight individual data points in a plot.")
print("You can use 'marker' argument or shorthand format strings (fmt).")
print("Important Note: Markers help visualize exact data positions.\n")

# ---------------------------------------------------
# Example 1: Basic Marker (Circle)
# ---------------------------------------------------
print("[Example 1] Mark each point with a Circle ('o').\n")

plt.figure(figsize=(6, 4))
plt.plot(ypoints, marker='o')
plt.title("Markers: Circle ('o')")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 2: Star Marker
# ---------------------------------------------------
print("[Example 2] Mark each point with a Star ('*').\n")

plt.figure(figsize=(6, 4))
plt.plot(ypoints, marker='*')
plt.title("Markers: Star ('*')")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 3: Marker Reference Variety
# ---------------------------------------------------
print("[Example 3] Demonstrating a few different marker types.\n")
markers = ['o', 's', 'D', '^', 'x', 'P']  # Circle, Square, Diamond, TriangleUp, X, Plus Filled
labels = ['Circle', 'Square', 'Diamond', 'Triangle Up', 'X', 'Plus (Filled)']

plt.figure(figsize=(7, 5))
for i, m in enumerate(markers):
    plt.plot(i, ypoints[i % len(ypoints)], marker=m, ms=12, label=labels[i])
plt.title("Different Marker Types")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 4: Format String (fmt) marker|line|color
# ---------------------------------------------------
print("[Example 4] Using fmt string 'o:r' → Circle markers, dotted line, red color.\n")

plt.figure(figsize=(6, 4))
plt.plot(ypoints, 'o:r')  # circle marker, dotted line, red color
plt.title("Format String Example: 'o:r'")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 5: Marker Size
# ---------------------------------------------------
print("[Example 5] Customizing marker size with ms=20.\n")

plt.figure(figsize=(6, 4))
plt.plot(ypoints, marker='o', ms=20)
plt.title("Marker Size Example (ms=20)")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 6: Marker Edge Color (mec)
# ---------------------------------------------------
print("[Example 6] Customizing edge color of markers (mec='red').\n")

plt.figure(figsize=(6, 4))
plt.plot(ypoints, marker='o', ms=20, mec='r')
plt.title("Marker Edge Color (mec='r')")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 7: Marker Face Color (mfc)
# ---------------------------------------------------
print("[Example 7] Customizing face color of markers (mfc='red').\n")

plt.figure(figsize=(6, 4))
plt.plot(ypoints, marker='o', ms=20, mfc='r')
plt.title("Marker Face Color (mfc='r')")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 8: Both Edge + Face Color
# ---------------------------------------------------
print("[Example 8] Setting both edge and face color to red.\n")

plt.figure(figsize=(6, 4))
plt.plot(ypoints, marker='o', ms=20, mec='r', mfc='r')
plt.title("Edge + Face Color (Red)")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 9: Hexadecimal Color
# ---------------------------------------------------
print("[Example 9] Using hexadecimal color code '#4CAF50' (green shade).\n")

plt.figure(figsize=(6, 4))
plt.plot(ypoints, marker='o', ms=20, mec='#4CAF50', mfc='#4CAF50')
plt.title("Hexadecimal Color Example (#4CAF50)")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Example 10: Named Color
# ---------------------------------------------------
print("[Example 10] Using named color 'hotpink'.\n")

plt.figure(figsize=(6, 4))
plt.plot(ypoints, marker='o', ms=20, mec='hotpink', mfc='hotpink')
plt.title("Named Color Example (hotpink)")
plt.grid(True)
plt.show()

# ---------------------------------------------------
# Conclusion
# ---------------------------------------------------
print("\n====================== Summary ======================\n")
print("1. Markers emphasize individual points in a line or scatter plot.")
print("2. You can choose from many marker shapes like circle, star, square, triangle, etc.")
print("3. Format string (fmt) shorthand lets you combine marker, line style, and color.")
print("4. Customize marker size with ms, edge color with mec, and face color with mfc.")
print("5. Colors can be standard letters, hex codes, or 140+ named colors.\n")
print("Important Note: Markers are a powerful way to make your plots clearer and more visually appealing.\n")
print("=====================================================\n")
