"""
Pandas Introduction Demonstration Script
----------------------------------------
This script introduces Pandas, demonstrates its basic functionalities,
and explains important concepts with clear console outputs and visualization.

Author: Your Name
"""

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("="*80)
print("📌 PANDAS INTRODUCTION DEMO")
print("="*80)

# ------------------------------------------------------------------------------
# 1. What is Pandas?
# ------------------------------------------------------------------------------
print("\n1️⃣ What is Pandas?")
print("Pandas is a Python library for working with data sets.")
print("It helps in analyzing, cleaning, exploring, and manipulating data.\n")

# Example: Creating a simple DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 29],
    "Department": ["HR", "Finance", "IT", "IT", "HR"],
    "Salary": [50000, 60000, 75000, 80000, 52000],
}
df = pd.DataFrame(data)
print("🔹 Example DataFrame created using Pandas:\n")
print(df)

# ------------------------------------------------------------------------------
# 2. Why use Pandas?
# ------------------------------------------------------------------------------
print("\n2️⃣ Why Use Pandas?")
print("✅ Helps analyze large datasets")
print("✅ Makes messy data clean and relevant")
print("✅ Enables statistical analysis\n")

# Example: Check basic statistics of Salary column
print("📊 Basic statistics of Salary column:\n")
print(df["Salary"].describe())

# ------------------------------------------------------------------------------
# 3. What can Pandas do?
# ------------------------------------------------------------------------------
print("\n3️⃣ What Can Pandas Do?")

# a) Correlation
print("\n🔹 Correlation between Age and Salary:\n")
print(df[["Age", "Salary"]].corr())

# b) Finding average, max, min
print("\n🔹 Average Salary:", df["Salary"].mean())
print("🔹 Max Salary:", df["Salary"].max())
print("🔹 Min Salary:", df["Salary"].min())

# ------------------------------------------------------------------------------
# 4. Data Cleaning Example
# ------------------------------------------------------------------------------
print("\n4️⃣ Data Cleaning Example")

# Introduce some messy data with NaN values
messy_data = {
    "Name": ["Frank", "Grace", None, "Hannah"],
    "Age": [28, None, 33, 26],
    "Department": ["IT", "Finance", "HR", None],
    "Salary": [58000, None, 62000, 50000],
}
df_messy = pd.DataFrame(messy_data)
print("\nMessy DataFrame with NULL values:\n")
print(df_messy)

# Drop rows with NULL values
cleaned_df = df_messy.dropna()
print("\n✅ Cleaned DataFrame (NULL values removed):\n")
print(cleaned_df)

# ------------------------------------------------------------------------------
# 5. Visualization Example
# ------------------------------------------------------------------------------
print("\n5️⃣ Visualization Example: Salary Distribution by Department")

# Group salaries by Department
salary_by_dept = df.groupby("Department")["Salary"].mean()

# Plot bar chart
salary_by_dept.plot(kind="bar", color=["skyblue", "lightgreen", "salmon"], edgecolor="black")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=0)
plt.show()

# ------------------------------------------------------------------------------
# 6. GitHub Source Code Reference
# ------------------------------------------------------------------------------
print("\n6️⃣ Pandas Source Code Repository:")
print("🔗 https://github.com/pandas-dev/pandas")

print("\n✅ End of Demonstration. You have now seen how Pandas can:")
print("   - Create and manipulate data")
print("   - Perform statistical analysis")
print("   - Clean messy datasets")
print("   - Visualize meaningful results")
print("="*80)
