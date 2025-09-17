"""
SciPy I/O - Working with MATLAB Arrays
--------------------------------------
This script demonstrates how to:
1. Export NumPy arrays into MATLAB .mat format using scipy.io.savemat()
2. Import MATLAB .mat data using scipy.io.loadmat()
3. Understand the structure of loaded data (__header__, __version__, __globals__)
4. Extract variables properly
5. Fix dimensionality issues with squeeze_me=True
6. Visualize the imported data for clarity
"""

import numpy as np
from scipy import io
import matplotlib.pyplot as plt

print("="*70)
print("      SciPy Interoperability with MATLAB Arrays (savemat & loadmat)      ")
print("="*70, "\n")

# ---------------------------------------------------------------
# Step 1: Create a NumPy array
# ---------------------------------------------------------------
arr = np.arange(10)  # simple 1D array [0..9]
print("Step 1: Created a NumPy array")
print("Array:", arr)
print("Shape:", arr.shape)
print("Type:", type(arr))
print("\n" + "-"*70 + "\n")

# ---------------------------------------------------------------
# Step 2: Export this array into MATLAB .mat file
# ---------------------------------------------------------------
print("Step 2: Exporting array to MATLAB format using io.savemat()")
io.savemat("arr.mat", {"vec": arr})
print("✅ Saved 'arr.mat' file with variable name 'vec'")
print("Important Note: savemat() requires a dictionary with variable names as keys.\n")
print("\n" + "-"*70 + "\n")

# ---------------------------------------------------------------
# Step 3: Import the data back using loadmat()
# ---------------------------------------------------------------
print("Step 3: Importing MATLAB .mat file using io.loadmat()")
mydata = io.loadmat("arr.mat")
print("Data loaded into Python as a dictionary:")
for key in mydata:
    print(f" - {key}: {type(mydata[key])}")

print("\nImportant Note: loadmat() adds extra keys '__header__', '__version__', '__globals__'")
print("These store metadata about the .mat file, not your actual data.\n")

# Extract the variable "vec"
print("Extracting variable 'vec':")
print(mydata["vec"])
print("Shape of extracted array:", mydata["vec"].shape)
print("⚠️ Notice: Our original 1D array became a 2D array (extra dimension added).")
print("\n" + "-"*70 + "\n")

# ---------------------------------------------------------------
# Step 4: Fixing dimension issue with squeeze_me=True
# ---------------------------------------------------------------
print("Step 4: Fixing dimensionality with 'squeeze_me=True'")
mydata_fixed = io.loadmat("arr.mat", squeeze_me=True)

print("Extracted variable 'vec' with squeeze_me=True:")
print(mydata_fixed["vec"])
print("Shape of extracted array:", mydata_fixed["vec"].shape)
print("✅ Dimension issue fixed, back to original 1D array.\n")
print("\n" + "-"*70 + "\n")

# ---------------------------------------------------------------
# Step 5: Visualization
# ---------------------------------------------------------------
print("Step 5: Visualization of Imported Data")
print("Plotting 'vec' from MATLAB file...")

plt.figure(figsize=(8, 5))
plt.plot(mydata_fixed["vec"], marker="o", linestyle="-", color="b", label="vec from arr.mat")
plt.title("Visualization of MATLAB Data Imported into Python", fontsize=14)
plt.xlabel("Index", fontsize=12)
plt.ylabel("Value", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

print("Important Note: This plot confirms that the data saved to MATLAB format and re-imported")
print("remains identical to the original NumPy array.")
print("="*70)
print("               🎉 End of SciPy MATLAB Arrays Demo 🎉              ")
print("="*70)
