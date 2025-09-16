"""
Pandas Series Demonstration
----------------------------
This script demonstrates:
1. Creating Pandas Series from lists and dictionaries
2. Accessing Series data (by index and labels)
3. Custom labels in Series
4. Creating DataFrame from Series
5. Visualization using matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt

print("="*80)
print("📌 PANDAS SERIES DEMONSTRATION")
print("="*80)

# ------------------------------------------------------------------------------
# 1. Creating a simple Pandas Series from a list
# ------------------------------------------------------------------------------
print("\n1️⃣ Creating a simple Series from a list:")
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

print("\nImportant Note: If no labels are provided, Pandas automatically assigns default integer indexes (0,1,2...).")

# ------------------------------------------------------------------------------
# 2. Accessing values by index
# ------------------------------------------------------------------------------
print("\n2️⃣ Accessing values by index:")
print("Value at index 0:", myvar[0])

# ------------------------------------------------------------------------------
# 3. Creating custom labels
# ------------------------------------------------------------------------------
print("\n3️⃣ Creating a Series with custom labels:")
myvar_labels = pd.Series(a, index=["x", "y", "z"])
print(myvar_labels)

print("\nAccessing by label (y):", myvar_labels["y"])

# ------------------------------------------------------------------------------
# 4. Creating Series from dictionary
# ------------------------------------------------------------------------------
print("\n4️⃣ Creating a Series from a dictionary:")
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar_dict = pd.Series(calories)
print(myvar_dict)

print("\nImportant Note: Dictionary keys become labels in the Series.")

# ------------------------------------------------------------------------------
# 5. Selecting only some items from dictionary using index
# ------------------------------------------------------------------------------
print("\n5️⃣ Selecting only day1 and day2 from dictionary:")
myvar_partial = pd.Series(calories, index=["day1", "day2"])
print(myvar_partial)

# ------------------------------------------------------------------------------
# 6. DataFrame from Series
# ------------------------------------------------------------------------------
print("\n6️⃣ Creating a DataFrame from multiple Series (like a table):")
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
my_dataframe = pd.DataFrame(data)
print(my_dataframe)

print("\nImportant Note: A Series is like a column, a DataFrame is like the full table.")

# ------------------------------------------------------------------------------
# 7. Visualization Example
# ------------------------------------------------------------------------------
print("\n7️⃣ Visualization Example: Plotting calories vs duration")
plt.figure(figsize=(6,4))
plt.plot(my_dataframe["calories"], my_dataframe["duration"], marker="o", linestyle="--", color="b")
plt.title("Calories vs Duration")
plt.xlabel("Calories Burned")
plt.ylabel("Duration (minutes)")
plt.grid(True)
plt.show()

# ------------------------------------------------------------------------------
# END
# ------------------------------------------------------------------------------
print("\n✅ End of Demonstration. You have now learned:")
print("   - What a Pandas Series is")
print("   - How to access values by index and labels")
print("   - How to create Series from lists and dictionaries")
print("   - How to create a DataFrame from Series")
print("   - How to visualize data using matplotlib")
print("="*80)
