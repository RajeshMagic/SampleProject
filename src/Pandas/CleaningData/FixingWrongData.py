# ---------------------------------------------------------------
# Pandas - Fixing Wrong Data
# ---------------------------------------------------------------
# This script demonstrates how to:
# 1. Detect wrong data values.
# 2. Replace wrong values directly (manual correction).
# 3. Replace wrong values using rules/boundaries.
# 4. Remove rows containing wrong values.
# 5. Visualize the dataset before and after cleaning.
#
# Console outputs are organized with "Important Note" messages
# for clarity and better learning.
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

print("\n================ ORIGINAL DATA (First 12 rows) ================\n")
print(df.head(12))
print("\nImportant Note: In row 7, Duration = 450 (suspicious, looks like a typo!).\n")

# -------------------------
# Step 2: Fix wrong data by direct replacement
# -------------------------
print(">>> Fixing wrong value in row 7 directly...\n")
df.loc[7, "Duration"] = 45   # Replace manually

print("\n================ AFTER DIRECT FIX ================\n")
print(df.head(12))
print("\nImportant Note: Row 7 Duration changed from 450 → 45.\n")

# -------------------------
# Step 3: Fix wrong data by applying rules
# -------------------------
print(">>> Applying rule: If Duration > 120, replace it with 120.\n")

# Simulate a wrong dataset again to demonstrate rules
df_rules = pd.DataFrame(data)

for x in df_rules.index:
    if df_rules.loc[x, "Duration"] > 120:
        df_rules.loc[x, "Duration"] = 120

print("\n================ AFTER APPLYING RULES ================\n")
print(df_rules.head(12))
print("\nImportant Note: Any Duration > 120 is capped at 120.\n")

# -------------------------
# Step 4: Removing rows with wrong values
# -------------------------
print(">>> Removing rows where Duration > 120 (instead of replacing)...\n")

df_removed = pd.DataFrame(data)

for x in df_removed.index:
    if df_removed.loc[x, "Duration"] > 120:
        df_removed.drop(x, inplace=True)

print("\n================ AFTER REMOVING ROWS ================\n")
print(df_removed.head(12))
print("\nImportant Note: Row with Duration = 450 has been removed completely.\n")

# -------------------------
# Step 5: Visualization
# -------------------------
print(">>> Creating visualization of 'Duration' column before and after fixing...")

plt.figure(figsize=(12,5))

# Original Data
plt.subplot(1, 2, 1)
plt.plot(df.index, data["Duration"], marker='o', color="red", label="Original")
plt.title("Before Fixing Wrong Data")
plt.xlabel("Row Index")
plt.ylabel("Duration")
plt.legend()

# Fixed Data
plt.subplot(1, 2, 2)
plt.plot(df.index, df["Duration"], marker='o', color="green", label="Fixed")
plt.title("After Fixing Wrong Data")
plt.xlabel("Row Index")
plt.ylabel("Duration")
plt.legend()

plt.tight_layout()
plt.show()

print("\nVisualization Complete!\n")
print("Important Note: Left chart shows wrong data (spike at 450). Right chart shows fixed value.\n")

# -------------------------
# Step 6: Summary
# -------------------------
print("================ SUMMARY ================\n")
print("1. Wrong data (Duration=450) was detected in row 7.")
print("2. Fixed using direct replacement: df.loc[row, 'col'] = value.")
print("3. Applied rules: capped values >120 to 120.")
print("4. Alternative: Removed rows with Duration >120.")
print("5. Visualization confirms the fix (no large spike).\n")
print(">>> Data is now corrected and ready for further analysis!")
