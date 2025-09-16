# ------------------------------------------------------------------------------
# Pandas - Cleaning Empty Cells Demonstration
# Topics Covered:
#   1. Removing Rows with Empty Cells
#   2. Replacing Empty Values with a Fixed Number
#   3. Replacing Empty Values Only in Specific Columns
#   4. Replacing with Mean, Median, and Mode
#   5. Visualization Before and After Cleaning
# ------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# Step 1. Load CSV File
# ------------------------------------------------------------------------------
print("📊 Step 1: Loading CSV file (data.csv) with missing values...\n")

# Sample dataset with some NaN values
data = {
    "Duration": [60, 60, 45, 45, 60, None, 60, 60],
    "Pulse": [110, 117, 109, 117, 102, 110, 104, 98],
    "Maxpulse": [130, 145, 175, 148, 127, 136, 134, 124],
    "Calories": [409.1, None, 282.4, 406.0, 300.0, 374.0, None, 269.0]
}

df = pd.DataFrame(data)
print("👉 Original DataFrame with empty cells:")
print(df, "\n")

# ------------------------------------------------------------------------------
# Step 2. Removing Rows with Empty Cells
# ------------------------------------------------------------------------------
print("📍 Step 2: Removing rows with NULL values using dropna()")

new_df = df.dropna()
print("👉 New DataFrame after dropna() (returns a copy, original unchanged):")
print(new_df, "\n")

print("⚡ Important Note: Original DataFrame is still unchanged.")
df_copy = df.copy()
df_copy.dropna(inplace=True)
print("👉 Using inplace=True removes rows from original DataFrame:")
print(df_copy, "\n")

# ------------------------------------------------------------------------------
# Step 3. Replace Empty Values with a Fixed Number
# ------------------------------------------------------------------------------
print("📍 Step 3: Replace empty cells with a fixed number (130)...")

df_fixed = df.copy()
df_fixed.fillna(130, inplace=True)
print("👉 DataFrame after replacing NaN with 130:")
print(df_fixed, "\n")

# ------------------------------------------------------------------------------
# Step 4. Replace Empty Values Only in Specific Column
# ------------------------------------------------------------------------------
print("📍 Step 4: Replace empty values only in 'Calories' column with 130...")

df_column_replace = df.copy()
df_column_replace.fillna({"Calories": 130}, inplace=True)
print("👉 DataFrame after replacing NaN in 'Calories' only:")
print(df_column_replace, "\n")

# ------------------------------------------------------------------------------
# Step 5. Replace Using Mean, Median, and Mode
# ------------------------------------------------------------------------------
print("📍 Step 5: Replace empty values using Mean, Median, Mode...")

# Using Mean
df_mean = df.copy()
mean_val = df_mean["Calories"].mean()
df_mean.fillna({"Calories": mean_val}, inplace=True)
print(f"👉 Mean of Calories = {mean_val:.2f}")
print("👉 DataFrame after replacing NaN with Mean:")
print(df_mean, "\n")

# Using Median
df_median = df.copy()
median_val = df_median["Calories"].median()
df_median.fillna({"Calories": median_val}, inplace=True)
print(f"👉 Median of Calories = {median_val:.2f}")
print("👉 DataFrame after replacing NaN with Median:")
print(df_median, "\n")

# Using Mode
df_mode = df.copy()
mode_val = df_mode["Calories"].mode()[0]
df_mode.fillna({"Calories": mode_val}, inplace=True)
print(f"👉 Mode of Calories = {mode_val:.2f}")
print("👉 DataFrame after replacing NaN with Mode:")
print(df_mode, "\n")

# ------------------------------------------------------------------------------
# Step 6. Visualization
# ------------------------------------------------------------------------------
print("📍 Step 6: Visualization of 'Calories' column before and after filling missing values")

plt.figure(figsize=(12, 5))

# Before cleaning
plt.subplot(1, 2, 1)
plt.plot(df["Calories"], marker="o", linestyle="--", color="red", label="Before Cleaning")
plt.title("Calories Before Cleaning")
plt.xlabel("Row Index")
plt.ylabel("Calories")
plt.legend()
plt.grid(True)

# After filling with mean
plt.subplot(1, 2, 2)
plt.plot(df_mean["Calories"], marker="o", linestyle="--", color="green", label="After Filling (Mean)")
plt.title("Calories After Filling (Mean)")
plt.xlabel("Row Index")
plt.ylabel("Calories")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

print("\n✅ Demonstration of handling empty cells completed successfully!")
