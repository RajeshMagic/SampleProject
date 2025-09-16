"""
Pandas DataFrame Demonstration
-------------------------------
This script demonstrates:
1. Creating DataFrames from dictionaries
2. Accessing rows using loc
3. Using custom row indexes
4. Loading DataFrames from CSV
5. Visualizing DataFrames with matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

print("="*80)
print("📌 PANDAS DATAFRAME DEMONSTRATION")
print("="*80)

# ------------------------------------------------------------------------------
# 1. Create a simple DataFrame
# ------------------------------------------------------------------------------
print("\n1️⃣ Creating a DataFrame from a dictionary:")

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)

print("\nImportant Note: A DataFrame is like a table (2D structure) with rows & columns.")

# ------------------------------------------------------------------------------
# 2. Locate rows using loc
# ------------------------------------------------------------------------------
print("\n2️⃣ Locating rows using df.loc[]:")

print("\n- Access row 0 (returns a Series):")
print(df.loc[0])

print("\n- Access rows 0 and 1 (returns a DataFrame):")
print(df.loc[[0, 1]])

# ------------------------------------------------------------------------------
# 3. Using custom indexes (Named Indexes)
# ------------------------------------------------------------------------------
print("\n3️⃣ Creating DataFrame with custom row indexes:")

df_named = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df_named)

print("\n- Access row with label 'day2':")
print(df_named.loc["day2"])

print("\nImportant Note: When you set custom indexes, you can access rows by name.")

# ------------------------------------------------------------------------------
# 4. Load DataFrame from a CSV file
# ------------------------------------------------------------------------------
print("\n4️⃣ Loading a DataFrame from CSV:")

csv_file = "data.csv"

if os.path.exists(csv_file):
    df_csv = pd.read_csv(csv_file)
    print(df_csv.head())
    print("\nImportant Note: Always check your dataset with head(), tail(), and info().")
else:
    print(f"⚠️ File '{csv_file}' not found. Skipping CSV load demonstration.")

# ------------------------------------------------------------------------------
# 5. Visualization
# ------------------------------------------------------------------------------
print("\n5️⃣ Visualization: Bar chart of calories vs duration")

plt.figure(figsize=(6,4))
plt.bar(df.index, df["calories"], color="orange", label="Calories")
plt.plot(df.index, df["duration"], marker="o", color="blue", label="Duration (min)")
plt.xlabel("Row Index")
plt.ylabel("Values")
plt.title("Calories & Duration Visualization")
plt.legend()
plt.grid(True)
plt.show()

# ------------------------------------------------------------------------------
# END
# ------------------------------------------------------------------------------
print("\n✅ End of Demonstration. You have now learned:")
print("   - How to create DataFrames")
print("   - How to access rows using loc")
print("   - How to use custom row indexes")
print("   - How to load CSV files into DataFrames")
print("   - How to visualize DataFrame data")
print("="*80)
