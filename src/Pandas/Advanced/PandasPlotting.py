# ---------------------------------------------------------------
# Pandas - Plotting with Matplotlib
# ---------------------------------------------------------------
# This script demonstrates:
# 1. Plotting a DataFrame using Pandas plot() method.
# 2. Scatter plots with strong vs weak correlations.
# 3. Histogram to understand frequency distribution.
#
# Important notes are printed to the console for better learning.
# ---------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Step 1: Load Data
# -------------------------
print("\n================ STEP 1: Load Dataset ================\n")

# Load workout dataset from CSV
df = pd.read_csv("data.csv")

print("First few rows of dataset:\n")
print(df.head(), "\n")
print("Important Note: Pandas integrates with Matplotlib, so df.plot() is a shortcut to visualize data quickly.\n")

# -------------------------
# Step 2: Default Line Plot
# -------------------------
print("================ STEP 2: Default Line Plot ================\n")
print(">>> By default, df.plot() will plot all numeric columns against their index.\n")

df.plot(title="Default Line Plot of All Numeric Columns")
plt.xlabel("Index (Workout Session)")
plt.ylabel("Values")
plt.show()

# -------------------------
# Step 3: Scatter Plot - Good Correlation
# -------------------------
print("================ STEP 3: Scatter Plot (Good Correlation) ================\n")
print(">>> Scatter plot with Duration (x) vs Calories (y).")
print(">>> Earlier, we found correlation ≈ 0.92 (very strong).")
print(">>> Expectation: Longer workout duration means higher calories burned.\n")

df.plot(kind="scatter", x="Duration", y="Calories", color="green", title="Strong Correlation: Duration vs Calories")
plt.show()

# -------------------------
# Step 4: Scatter Plot - Weak Correlation
# -------------------------
print("================ STEP 4: Scatter Plot (Weak Correlation) ================\n")
print(">>> Scatter plot with Duration (x) vs Maxpulse (y).")
print(">>> Correlation ≈ 0.01 (very weak).")
print(">>> Expectation: No clear relationship between Duration and Maxpulse.\n")

df.plot(kind="scatter", x="Duration", y="Maxpulse", color="red", title="Weak Correlation: Duration vs Maxpulse")
plt.show()

# -------------------------
# Step 5: Histogram
# -------------------------
print("================ STEP 5: Histogram ================\n")
print(">>> Histogram shows frequency distribution of a single column.")
print(">>> Example: How many workouts lasted between 50–60 minutes?\n")

df["Duration"].plot(kind="hist", bins=10, title="Histogram of Workout Duration", color="blue", edgecolor="black")
plt.xlabel("Duration (minutes)")
plt.ylabel("Frequency")
plt.show()

# -------------------------
# Step 6: Summary
# -------------------------
print("================ SUMMARY ================\n")
print("1. df.plot() → Quick way to plot numeric columns against index.")
print("2. Scatter plots → Show relationships (correlations) between two variables.")
print("   - Duration vs Calories → Strong correlation (0.92).")
print("   - Duration vs Maxpulse → Weak correlation (0.01).")
print("3. Histogram → Shows distribution/frequency of values within a column.")
print("\n>>> Plotting with Pandas makes it very easy to visualize data for analysis.\n")
