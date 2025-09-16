# ---------------------------------------------------------------
# Pandas - Removing Duplicates
# ---------------------------------------------------------------
# This script demonstrates how to:
# 1. Identify duplicate rows in a DataFrame.
# 2. Remove duplicate rows.
# 3. Visualize the effect before and after removing duplicates.
#
# Important Notes are printed in the console for clarity.
# ---------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Step 1: Create sample data
# -------------------------
data = {
    "Duration": [60, 60, 60, 45, 45, 60, 60, 450, 30, 60, 60, 60, 60, 60, 60, 60, 60, 60, 45, 60, 45, 60, 45, 60, 45, 60, 60, 60, 60, 60, 60, 60],
    "Date": [
        "2020/12/01", "2020/12/02", "2020/12/03", "2020/12/04", "2020/12/05", "2020/12/06", "2020/12/07", "2020/12/08",
        "2020/12/09", "2020/12/10", "2020/12/11", "2020/12/12", "2020/12/12", "2020/12/13", "2020/12/14", "2020/12/15",
        "2020/12/16", "2020/12/17", "2020/12/18", "2020/12/19", "2020/12/20", "2020/12/21", None, "2020/12/23",
        "2020/12/24", "2020/12/25", "20201226", "2020/12/27", "2020/12/28", "2020/12/29", "2020/12/30", "2020/12/31"
    ],
    "Pulse": [110, 117, 103, 109, 117, 102, 110, 104, 109, 98, 103, 100, 100, 106, 104, 98, 98, 100, 90, 103, 97, 108, 100, 130, 105, 102, 100, 92, 103, 100, 102, 92],
    "Maxpulse": [130, 145, 135, 175, 148, 127, 136, 134, 133, 124, 147, 120, 120, 128, 132, 123, 120, 120, 112, 123, 125, 131, 119, 101, 132, 126, 120, 118, 132, 132, 129, 115],
    "Calories": [409.1, 479.0, 340.0, 282.4, 406.0, 300.0, 374.0, 253.3, 195.1, 269.0, 329.3, 250.7, 250.7, 345.3, 379.3, 275.0, 215.2, 300.0, None, 323.0, 243.0, 364.2, 282.0, 300.0, 246.0, 334.5, 250.0, 241.0, None, 280.0, 380.3, 243.0]
}

df = pd.DataFrame(data)

print("\n================ ORIGINAL DATA (First 15 rows) ================\n")
print(df.head(15))
print("\nImportant Note: Row 11 and 12 are duplicates.\n")

# -------------------------
# Step 2: Detect duplicates
# -------------------------
print(">>> Detecting duplicates using df.duplicated()...\n")

duplicates = df.duplicated()
print(duplicates.head(15))
print("\nImportant Note: 'True' indicates the row is a duplicate.\n")

# -------------------------
# Step 3: Remove duplicates
# -------------------------
print(">>> Removing duplicates using df.drop_duplicates(inplace=True)...\n")

df.drop_duplicates(inplace=True)

print("\n================ DATA AFTER REMOVING DUPLICATES (First 15 rows) ================\n")
print(df.head(15))
print("\nImportant Note: Duplicate rows have been removed.\n")

# -------------------------
# Step 4: Visualization
# -------------------------
print(">>> Visualizing Duration column before and after removing duplicates...\n")

plt.figure(figsize=(12,5))

# Original Data with duplicates
plt.subplot(1, 2, 1)
plt.plot(range(len(data["Duration"])), data["Duration"], marker='o', color="red", label="Original")
plt.title("Before Removing Duplicates")
plt.xlabel("Row Index")
plt.ylabel("Duration")
plt.legend()

# Data after removing duplicates
plt.subplot(1, 2, 2)
plt.plot(df.index, df["Duration"], marker='o', color="green", label="No Duplicates")
plt.title("After Removing Duplicates")
plt.xlabel("Row Index")
plt.ylabel("Duration")
plt.legend()

plt.tight_layout()
plt.show()

print("\nImportant Note: Left chart shows original data (duplicates included). Right chart shows cleaned data.\n")

# -------------------------
# Step 5: Summary
# -------------------------
print("================ SUMMARY ================\n")
print("1. Duplicate rows detected using df.duplicated().")
print("2. Duplicate rows removed using df.drop_duplicates(inplace=True).")
print("3. Visualization confirms duplicates removed (no repeated points in green plot).")
print(">>> Data is now clean and ready for analysis.\n")
