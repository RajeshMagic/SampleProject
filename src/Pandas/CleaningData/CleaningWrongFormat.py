# ---------------------------------------------------------------
# Pandas - Cleaning Data of Wrong Format (Date Column Example)
# ---------------------------------------------------------------
# This script demonstrates how to:
# 1. Detect wrong formats in data.
# 2. Convert to the correct datetime format using pandas.
# 3. Handle invalid or missing values (NaT).
# 4. Remove rows with invalid date values.
# 5. Visualize before and after cleaning.
#
# Console outputs are organized with "Important Note" messages 
# for clarity and better learning.
# ---------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Step 1: Create sample data (similar to given example)
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

print("\n================ ORIGINAL DATA ================\n")
print(df.head(15))
print("\nImportant Note: Notice rows 22 and 26 -> Wrong date formats (None and '20201226').\n")

# -------------------------
# Step 2: Convert 'Date' column to datetime
# -------------------------
print("Converting 'Date' column into proper datetime format...\n")

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

print("\n================ DATA AFTER DATE CONVERSION ================\n")
print(df.head(15))
print("\nImportant Note: Wrong formats are converted. Invalid dates -> NaT (Not a Time).\n")

# -------------------------
# Step 3: Handling NaT values
# -------------------------
print("Handling NaT values in the 'Date' column...")

# Count NaT values
nat_count = df['Date'].isna().sum()
print(f"\nImportant Note: Found {nat_count} rows with NaT (invalid/missing dates).\n")

# Option 1: Remove rows with NaT
df_cleaned = df.dropna(subset=['Date'])

print("\n================ DATA AFTER REMOVING NaT ROWS ================\n")
print(df_cleaned.head(15))
print("\nImportant Note: Rows with NaT values in 'Date' have been removed.\n")

# -------------------------
# Step 4: Visualization
# -------------------------
print("Creating visualization of Calories vs Date before and after cleaning...")

plt.figure(figsize=(12,5))

# Before cleaning
plt.subplot(1, 2, 1)
plt.scatter(df.index, df['Calories'], color='red', label="With NaT")
plt.title("Before Cleaning (NaT present)")
plt.xlabel("Row Index")
plt.ylabel("Calories")
plt.legend()

# After cleaning
plt.subplot(1, 2, 2)
plt.plot(df_cleaned['Date'], df_cleaned['Calories'], marker='o', linestyle='-', color='green', label="Cleaned Data")
plt.title("After Cleaning (Dates fixed)")
plt.xlabel("Date")
plt.ylabel("Calories")
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()

print("\nVisualization Complete!\n")
print("Important Note: Left chart shows raw data (with errors). Right chart shows cleaned data (proper dates).\n")

# -------------------------
# Step 5: Summary
# -------------------------
print("================ SUMMARY ================\n")
print("1. Wrong formats in 'Date' were detected and converted using pd.to_datetime().")
print("2. Invalid/missing dates became NaT (Not a Time).")
print("3. NaT rows were removed using dropna(subset=['Date']).")
print("4. Visualizations confirmed the effect of cleaning.\n")
print(">>> Data is now clean and ready for analysis!")
