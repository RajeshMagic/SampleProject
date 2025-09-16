# ------------------------------------------------------------------------------
# Pandas - Data Cleaning Demonstration
# Topics Covered:
#   1. Handling Empty Cells
#   2. Fixing Data Formats
#   3. Identifying & Correcting Wrong Data
#   4. Removing Duplicates
#   5. Visualization Before and After Cleaning
# ------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# 1. Load Dataset (Messy Data)
# ------------------------------------------------------------------------------
print("📊 Step 1: Loading messy dataset...\n")

data = {
    "Duration": [60, 60, 60, 45, 45, 60, 60, 450, 30, 60, 60, 60, 60, 60, 60,
                 60, 60, 60, 45, 60, 45, 60, None, 60, 45, 60, 60, 60, 60, 60,
                 60, 60],
    "Date": ["2020/12/01", "2020/12/02", "2020/12/03", "2020/12/04", "2020/12/05",
             "2020/12/06", "2020/12/07", "2020/12/08", "2020/12/09", "2020/12/10",
             "2020/12/11", "2020/12/12", "2020/12/12", "2020/12/13", "2020/12/14",
             "2020/12/15", "2020/12/16", "2020/12/17", "2020/12/18", "2020/12/19",
             "2020/12/20", "2020/12/21", None, "2020/12/23", "2020/12/24", "2020/12/25",
             "2020/12/26", "2020/12/27", "2020/12/28", "2020/12/29", "2020/12/30", "2020/12/31"],
    "Pulse": [110, 117, 103, 109, 117, 102, 110, 104, 109, 98, 103, 100, 100,
              106, 104, 98, 98, 100, 90, 103, 97, 108, 100, 130, 105, 102, 100,
              92, 103, 100, 102, 92],
    "Maxpulse": [130, 145, 135, 175, 148, 127, 136, 134, 133, 124, 147, 120, 120,
                 128, 132, 123, 120, 120, 112, 123, 125, 131, 119, 101, 132, 126,
                 120, 118, 132, 132, 129, 115],
    "Calories": [409.1, 479.0, 340.0, 282.4, 406.0, 300.0, 374.0, 253.3, 195.1,
                 269.0, 329.3, 250.7, 250.7, 345.3, 379.3, 275.0, 215.2, 300.0,
                 None, 323.0, 243.0, 364.2, 282.0, 300.0, 246.0, 334.5, 250.0,
                 241.0, None, 280.0, 380.3, 243.0]
}

df = pd.DataFrame(data)

print("👉 Initial DataFrame with issues:")
print(df.head(15))
print("\n⚡ Note: Contains NaN values, wrong Duration (row 7), wrong Date format (row 26), and duplicates (row 11 & 12).")

# ------------------------------------------------------------------------------
# 2. Handling Empty Cells
# ------------------------------------------------------------------------------
print("\n📍 Step 2: Handling Empty Cells...")

print("👉 Checking for NaN values:\n", df.isnull().sum())

# Fill missing Calories with mean value
df["Calories"].fillna(df["Calories"].mean(), inplace=True)

# Drop rows where "Date" is missing
df.dropna(subset=["Date"], inplace=True)

print("✅ Fixed missing values: Filled 'Calories' NaN with mean, dropped rows with missing Date.\n")

# ------------------------------------------------------------------------------
# 3. Fixing Wrong Format
# ------------------------------------------------------------------------------
print("📍 Step 3: Fixing Wrong Data Format...")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

print("✅ Date column converted to proper datetime format.\n")

# ------------------------------------------------------------------------------
# 4. Wrong Data (Outlier Fixing)
# ------------------------------------------------------------------------------
print("📍 Step 4: Detecting Wrong Data (e.g., extreme Duration)...")

# Duration should not be > 120, replace with mean of valid durations
mean_duration = df.loc[df["Duration"] < 120, "Duration"].mean()
df.loc[df["Duration"] > 120, "Duration"] = mean_duration

print(f"✅ Replaced invalid 'Duration' values (>120) with mean ({mean_duration:.2f}).\n")

# ------------------------------------------------------------------------------
# 5. Removing Duplicates
# ------------------------------------------------------------------------------
print("📍 Step 5: Removing Duplicates...")

before = len(df)
df.drop_duplicates(inplace=True)
after = len(df)

print(f"✅ Removed {before - after} duplicate rows.\n")

# ------------------------------------------------------------------------------
# 6. Final Clean Data Overview
# ------------------------------------------------------------------------------
print("📍 Step 6: Final Clean Data Overview")
print(df.head(15))
print("\n👉 Clean DataFrame Info:")
print(df.info())

# ------------------------------------------------------------------------------
# 7. Visualization Before vs After Cleaning
# ------------------------------------------------------------------------------
print("\n📍 Step 7: Visualizing Before vs After Cleaning")

# Plot Calories vs Duration
plt.figure(figsize=(10, 5))
plt.scatter(data["Duration"], data["Calories"], color="red", label="Before Cleaning", alpha=0.6, edgecolors="k")
plt.scatter(df["Duration"], df["Calories"], color="green", label="After Cleaning", alpha=0.6, edgecolors="k")
plt.xlabel("Duration (minutes)")
plt.ylabel("Calories Burned")
plt.title("Calories vs Duration (Before vs After Cleaning)")
plt.legend()
plt.grid(True)
plt.show()

print("\n✅ Data Cleaning Completed Successfully!")
