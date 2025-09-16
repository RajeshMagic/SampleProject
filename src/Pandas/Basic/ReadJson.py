# ------------------------------------------------------------------------------
# Pandas Read JSON - Demonstration Script
# ------------------------------------------------------------------------------
# This script demonstrates how Pandas can read JSON data from a file or directly
# from a Python dictionary (since JSON and dict have similar structures).
#
# We will also visualize data for better understanding.
# ------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# 1. Load JSON from File
# ------------------------------------------------------------------------------
print("\n1️⃣ Loading JSON data from file (data.json)...")

try:
    df_file = pd.read_json("data.json")
    print("\n✅ Data loaded successfully from JSON file!")

    print("\n👉 Displaying entire DataFrame using to_string():")
    print(df_file.to_string())

    print("\n👉 Default DataFrame display (may be truncated if large):")
    print(df_file)

except FileNotFoundError:
    print("⚠️ File 'data.json' not found. Please ensure it exists in working directory.")


# ------------------------------------------------------------------------------
# 2. Load JSON from a Python Dictionary
# ------------------------------------------------------------------------------
print("\n2️⃣ Loading JSON data directly from a Python Dictionary...")

data_dict = {
  "Duration": { "0": 60, "1": 60, "2": 60, "3": 45, "4": 45, "5": 60 },
  "Pulse":    { "0": 110, "1": 117, "2": 103, "3": 109, "4": 117, "5": 102 },
  "Maxpulse": { "0": 130, "1": 145, "2": 135, "3": 175, "4": 148, "5": 127 },
  "Calories": { "0": 409, "1": 479, "2": 340, "3": 282, "4": 406, "5": 300 }
}

df_dict = pd.DataFrame(data_dict)
print("\n✅ Data loaded successfully from dictionary!")

print("\n👉 DataFrame created from dictionary:")
print(df_dict)


# ------------------------------------------------------------------------------
# 3. Important Note on JSON vs Dict
# ------------------------------------------------------------------------------
print("\nℹ️ Important Note:")
print("- JSON objects have the same structure as Python dictionaries.")
print("- That is why Pandas can load both seamlessly into DataFrames.")
print("- Use `pd.read_json()` for files or `pd.DataFrame(dict)` for in-memory data.")


# ------------------------------------------------------------------------------
# 4. Visualization Example
# ------------------------------------------------------------------------------
print("\n3️⃣ Visualization Example with Matplotlib:")
print("👉 Plotting Duration vs Calories from dictionary data...")

df_dict.plot(
    kind="line",
    x="Duration",
    y="Calories",
    marker="o",
    title="Calories Burned vs Duration"
)
plt.xlabel("Duration (minutes)")
plt.ylabel("Calories Burned")
plt.grid(True)
plt.show()


# ------------------------------------------------------------------------------
# End of Script
# ------------------------------------------------------------------------------
print("\n🎯 Demonstration complete!")
print("👉 Key Takeaways:")
print("- Use `pd.read_json('file.json')` to read JSON files.")
print("- JSON and Python dictionaries share the same structure.")
print("- Use `df.to_string()` to display the full DataFrame.")
print("- Visualization makes JSON data insights clearer.")
