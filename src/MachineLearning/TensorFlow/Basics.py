"""
Machine Learning Basics with Python
Author: OpenAI ChatGPT

This script demonstrates:
1. Understanding datasets: arrays and tables
2. Data types: numerical (discrete, continuous), categorical, ordinal
3. Basic statistics: mean, min, max, median
4. Visualization of data with Matplotlib and Seaborn
5. Simple prediction using basic rules
6. Console explanations and important points
"""

# ---------------------------------------------------
# Import required libraries
# ---------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("\n================ Machine Learning Basics ================\n")
print("Machine Learning is about making computers learn from data to predict outcomes.\n")
print("Important Note: Understanding data types is critical to decide the right analysis method.\n")

# ---------------------------------------------------
# Step 1: Demonstrate a simple array (numerical data)
# ---------------------------------------------------
print("[Step 1] Numerical Array Example (Discrete Data)\n")
data_array = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
print("Data array:", data_array)

# Basic statistics
mean_val = np.mean(data_array)
max_val = np.max(data_array)
min_val = np.min(data_array)
median_val = np.median(data_array)

print(f"\nImportant statistics:")
print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Max: {max_val}")
print(f"Min: {min_val}")

# Visualization: Histogram
plt.hist(data_array, bins=5, color='skyblue', edgecolor='black')
plt.title("Histogram of Numerical Array")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# ---------------------------------------------------
# Step 2: Demonstrate a dataset (categorical, ordinal, numerical)
# ---------------------------------------------------
print("[Step 2] Example Dataset (Car Database)\n")
data_dict = {
    "CarName": ["BMW", "Volvo", "VW", "VW", "Ford", "VW", "Tesla", "BMW", "Volvo", "Ford", "Toyota", "VW", "Toyota"],
    "Color": ["red","black","gray","white","white","white","red","black","gray","white","gray","white","blue"],
    "Age": [5,7,8,7,2,17,2,9,4,11,12,9,6],
    "Speed": [99,86,87,88,111,86,103,87,94,78,77,85,86],
    "AutoPass": ["Y","Y","N","Y","Y","Y","Y","Y","N","N","N","N","Y"]
}

df = pd.DataFrame(data_dict)
print(df.head())

# ---------------------------------------------------
# Step 3: Analyze numerical columns
# ---------------------------------------------------
print("\n[Step 3] Numerical Column Analysis\n")
print("Statistics for 'Age':")
print(df['Age'].describe())

print("\nStatistics for 'Speed':")
print(df['Speed'].describe())

# Visualization: Boxplot
sns.boxplot(x='Age', data=df, color='lightgreen')
plt.title("Boxplot of Car Ages")
plt.show()

sns.boxplot(x='Speed', data=df, color='lightcoral')
plt.title("Boxplot of Car Speeds")
plt.show()

# ---------------------------------------------------
# Step 4: Analyze categorical data
# ---------------------------------------------------
print("\n[Step 4] Categorical Column Analysis\n")
print("Most popular color:")
print(df['Color'].value_counts())

# Visualization: Bar Chart
df['Color'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Car Colors Frequency")
plt.xlabel("Color")
plt.ylabel("Count")
plt.show()

# ---------------------------------------------------
# Step 5: Analyze ordinal / binary data
# ---------------------------------------------------
print("\n[Step 5] Ordinal / Binary Column Analysis ('AutoPass')\n")
print(df['AutoPass'].value_counts())

# Visualization: Pie Chart
df['AutoPass'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#4CAF50','hotpink'])
plt.title("AutoPass Distribution")
plt.show()

# ---------------------------------------------------
# Step 6: Simple prediction based on rules
# ---------------------------------------------------
print("\n[Step 6] Simple Prediction Example\n")
print("Rule: If Age <= 5 and Speed >= 90, predict 'AutoPass' = Y, else N")

def simple_predict(row):
    if row['Age'] <= 5 and row['Speed'] >= 90:
        return 'Y'
    else:
        return 'N'

df['Predicted'] = df.apply(simple_predict, axis=1)
print(df[['CarName','Age','Speed','AutoPass','Predicted']])

# ---------------------------------------------------
# Step 7: Visual comparison of prediction
# ---------------------------------------------------
print("\n[Step 7] Visual Comparison of Actual vs Predicted AutoPass\n")
comparison = pd.crosstab(df['AutoPass'], df['Predicted'])
print(comparison)

comparison.plot(kind='bar', color=['#4CAF50','orange'])
plt.title("Actual vs Predicted AutoPass")
plt.xlabel("Actual AutoPass")
plt.ylabel("Count")
plt.show()

print("\n====================== Summary ======================\n")
print("1. Data can be numerical (discrete/continuous), categorical, or ordinal.")
print("2. Use statistical methods to understand numerical data (mean, median, max, min).")
print("3. Use counts and frequency for categorical and ordinal data.")
print("4. Simple rules can be used to predict outcomes before applying ML models.")
print("5. Visualization helps in understanding patterns in data.\n")
print("=====================================================\n")
