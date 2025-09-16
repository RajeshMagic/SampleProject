# ------------------------------------------------------------------------------
# Pandas Read CSV - Demonstration Script
# ------------------------------------------------------------------------------
# This script demonstrates how to read CSV files using Pandas, how Pandas handles
# display of large DataFrames, and how to control options like max_rows.
#
# Additionally, we will visualize data from the CSV file.
# ------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# 1. Load CSV into a DataFrame
# ------------------------------------------------------------------------------
print("\n1️⃣ Loading CSV file into a Pandas DataFrame...")

df = pd.read_csv("data1.csv")  # ensure 'data.csv' exists in the working directory
print("\n✅ Data loaded successfully!")

print("\n👉 Displaying entire DataFrame using to_string() (may be very long):")
print(df.to_string())  # forces printing all rows and columns


# ------------------------------------------------------------------------------
# 2. Default Pandas Printing Behavior
# ------------------------------------------------------------------------------
print("\n2️⃣ Default Pandas print behavior:")
print("👉 By default, Pandas prints only the first 5 and last 5 rows if DataFrame is large.")
print(df)  # shows first 5 and last 5 rows if rows > max_rows


# ------------------------------------------------------------------------------
# 3. Check max_rows option
# ------------------------------------------------------------------------------
print("\n3️⃣ Checking Pandas option for maximum displayed rows:")
print("👉 Pandas default max_rows setting is:")
print(pd.options.display.max_rows)

print("\nImportant Note:")
print("- If the DataFrame has more rows than this value, Pandas will only show head & tail.")


# ------------------------------------------------------------------------------
# 4. Increase max_rows and display full DataFrame
# ------------------------------------------------------------------------------
print("\n4️⃣ Changing max_rows to display all rows...")

pd.options.display.max_rows = 9999  # increase limit
print("✅ Updated pd.options.display.max_rows =", pd.options.display.max_rows)

print("\n👉 Now displaying full DataFrame:")
print(df)


# ------------------------------------------------------------------------------
# 5. Visualization Example
# ------------------------------------------------------------------------------
print("\n5️⃣ Visualization Example with Matplotlib:")
print("👉 Plotting a simple bar chart for first 10 rows (Calories vs Duration)...")

# Check if columns 'calories' and 'duration' exist (for safety)
if "calories" in df.columns and "duration" in df.columns:
    df.head(10).plot(
        kind="bar", 
        x="duration", 
        y="calories", 
        title="Calories vs Duration (first 10 rows)", 
        legend=True
    )
    plt.xlabel("Duration")
    plt.ylabel("Calories")
    plt.show()
else:
    print("⚠️ The CSV does not contain 'calories' and 'duration' columns for plotting.")


# ------------------------------------------------------------------------------
# End of Script
# ------------------------------------------------------------------------------
print("\n🎯 Demonstration complete!")
print("👉 Key Takeaways:")
print("- Use pd.read_csv() to load CSV into a DataFrame.")
print("- df.to_string() prints the entire DataFrame (not truncated).")
print("- Pandas default shows only head & tail if DataFrame is large.")
print("- You can adjust pd.options.display.max_rows to change how many rows are shown.")
print("- Data can be easily visualized using matplotlib.")
