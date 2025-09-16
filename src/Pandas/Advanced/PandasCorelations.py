# ---------------------------------------------------------------
# Pandas - Data Correlations
# ---------------------------------------------------------------
# This script demonstrates how to:
# 1. Use corr() to find relationships between numeric columns.
# 2. Interpret correlation results (good, bad, perfect).
# 3. Visualize correlation using heatmaps and scatter plots.
#
# Important Notes are explained in the console output for clarity.
# ---------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# Step 1: Load Data
# -------------------------
print("\n================ STEP 1: Load Dataset ================\n")

# Sample workout dataset (like data.csv)
data = {
    "Duration": [60, 60, 60, 45, 45, 60, 60, 45, 30, 60, 60, 60, 60, 60, 60],
    "Pulse":    [110, 117, 103, 109, 117, 102, 110, 104, 109, 98, 103, 100, 100, 106, 104],
    "Maxpulse": [130, 145, 135, 175, 148, 127, 136, 134, 133, 124, 147, 120, 120, 128, 132],
    "Calories": [409.1, 479.0, 340.0, 282.4, 406.0, 300.0, 374.0, 253.3, 195.1, 269.0, 329.3, 250.7, 250.7, 345.3, 379.3]
}

df = pd.DataFrame(data)
print(df.head(), "\n")

print("Important Note: Only numeric columns are included in correlation analysis.\n")

# -------------------------
# Step 2: Calculate Correlation
# -------------------------
print("================ STEP 2: Calculate Correlation ================\n")

correlation_matrix = df.corr()
print(correlation_matrix, "\n")

print(">>> Interpretation of Correlation:")
print("- Values range from -1 to +1.")
print("- 1 means perfect positive correlation (as one increases, so does the other).")
print("- -1 means perfect negative correlation (as one increases, the other decreases).")
print("- 0 means no correlation (completely unrelated).\n")

print(">>> Example from results:")
print("- Duration vs Duration = 1.000000 → Perfect correlation (column with itself).")
print("- Duration vs Calories ≈ 0.92 → Strong positive correlation.")
print("- Duration vs Maxpulse ≈ 0.01 → Very weak/no correlation.\n")

# -------------------------
# Step 3: Visualization - Heatmap
# -------------------------
print("================ STEP 3: Visualization - Heatmap ================\n")
print(">>> A heatmap provides a color-coded visualization of correlations.\n")

plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap", fontsize=14, weight='bold')
plt.show()

# -------------------------
# Step 4: Visualization - Scatter Plots
# -------------------------
print("================ STEP 4: Visualization - Scatter Plots ================\n")
print(">>> Scatter plots help us visually confirm the relationship between columns.\n")

plt.figure(figsize=(14,5))

# Strong correlation (Duration vs Calories)
plt.subplot(1,2,1)
plt.scatter(df["Duration"], df["Calories"], color="green")
plt.title("Strong Correlation: Duration vs Calories")
plt.xlabel("Duration")
plt.ylabel("Calories Burned")

# Weak correlation (Duration vs Maxpulse)
plt.subplot(1,2,2)
plt.scatter(df["Duration"], df["Maxpulse"], color="red")
plt.title("Weak Correlation: Duration vs Maxpulse")
plt.xlabel("Duration")
plt.ylabel("Maxpulse")

plt.tight_layout()
plt.show()

# -------------------------
# Step 5: Summary
# -------------------------
print("================ SUMMARY ================\n")
print("1. Correlation calculated using df.corr().")
print("2. Duration and Calories show strong positive correlation (0.92).")
print("3. Duration and Maxpulse show weak correlation (0.01).")
print("4. Heatmap provides an overview of all column relationships.")
print("5. Scatter plots confirm strong vs weak correlations visually.\n")
print(">>> Data correlations help identify relationships and are useful in analysis & ML models.\n")
