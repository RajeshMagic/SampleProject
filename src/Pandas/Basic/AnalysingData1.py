# ------------------------------------------------------------------------------
# Pandas - Analyzing DataFrames with Missing Values
# Demonstrating head(), tail(), and info() methods with proper explanations
# ------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# ------------------------------------------------------------------------------
# 1. Load or Create CSV File
# ------------------------------------------------------------------------------
csv_file = "data.csv"

if not os.path.exists(csv_file):
    print("⚠️ 'data.csv' not found. Creating a new one with sample data (50 rows)...")

    # Generate sample dataset
    sample_data = {
        "Duration": [i % 60 + 20 for i in range(50)],       # 20–79 minutes
        "Pulse": [80 + (i % 40) for i in range(50)],        # 80–119
        "Maxpulse": [120 + (i % 60) for i in range(50)],    # 120–179
        "Calories": [200 + (i * 3) % 300 for i in range(50)]  # 200–499
    }
    df_sample = pd.DataFrame(sample_data)

    # Introduce some NaN values in Calories column
    nan_indices = np.random.choice(df_sample.index, size=5, replace=False)
    df_sample.loc[nan_indices, "Calories"] = np.nan

    # Save to CSV
    df_sample.to_csv(csv_file, index=False)
    print("✅ Sample 'data.csv' with NaN values created!\n")

print("1️⃣ Loading CSV file into a Pandas DataFrame...")
df = pd.read_csv(csv_file)

print("\n👉 DataFrame loaded successfully!")
print("Shape of DataFrame (rows, columns):", df.shape)
print("Columns available:", list(df.columns))

# ------------------------------------------------------------------------------
# 2. Viewing Data - head() and tail()
# ------------------------------------------------------------------------------
print("\n2️⃣ Viewing the first 5 rows using df.head():")
print(df.head())

print("\n3️⃣ Viewing the first 10 rows using df.head(10):")
print(df.head(10))

print("\n4️⃣ Viewing the last 5 rows using df.tail():")
print(df.tail())

# ------------------------------------------------------------------------------
# 3. DataFrame Info
# ------------------------------------------------------------------------------
print("\n5️⃣ Displaying DataFrame info using df.info():")
print("⚡ Important Note: Non-Null Count shows missing values (NaN).")
print(df.info())

# ------------------------------------------------------------------------------
# 4. Visualization for Better Understanding
# ------------------------------------------------------------------------------
print("\n6️⃣ Visualizing data distribution... (Matplotlib)")

# Scatter Plot: Duration vs Calories
plt.figure(figsize=(8, 5))
plt.scatter(df["Duration"], df["Calories"], c="blue", alpha=0.6, edgecolors="k")
plt.title("Scatter Plot: Duration vs Calories (with NaN values)")
plt.xlabel("Duration (minutes)")
plt.ylabel("Calories Burned")
plt.grid(True)
plt.show()

# Histogram: Pulse distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Pulse"], bins=10, color="green", alpha=0.7, edgecolor="black")
plt.title("Histogram: Pulse Distribution")
plt.xlabel("Pulse Rate")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# ------------------------------------------------------------------------------
# 5. Summary
# ------------------------------------------------------------------------------
print("\n✅ Demonstration Complete!")
print("👉 You learned how to:")
print("- Load a CSV file into Pandas")
print("- View top and bottom rows using head() and tail()")
print("- Explore dataset metadata using info() (including missing values)")
print("- Visualize numeric columns for quick insights")
