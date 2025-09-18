# Machine Learning - Feature Scaling Demonstration
# Author: Training Script
# -------------------------------------------------
# This script demonstrates:
#   - Why scaling is important
#   - How to use sklearn's StandardScaler
#   - Predicting values with scaled data
#   - Visualizing original vs scaled features
#
# Dataset: Car dataset with Volume (liters), Weight (kg), CO2 (g/km)
# -------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

# -------------------------------------------------
# Step 1: Load the dataset
# -------------------------------------------------
print("\n--- Step 1: Loading Dataset ---")
data = {
    "Car": ["Toyota Aygo", "Mitsubishi Space Star", "Skoda Citigo", "Fiat 500", "Mini Cooper", "VW Up!", 
            "Skoda Fabia", "Mercedes A-Class", "Ford Fiesta", "Audi A1", "Hyundai I20", "Suzuki Swift", 
            "Ford Fiesta", "Honda Civic", "Hundai I30", "Opel Astra", "BMW 1", "Mazda 3", "Skoda Rapid", 
            "Ford Focus", "Ford Mondeo", "Opel Insignia", "Mercedes C-Class", "Skoda Octavia", "Volvo S60", 
            "Mercedes CLA", "Audi A4", "Audi A6", "Volvo V70", "BMW 5", "Mercedes E-Class", "Volvo XC70", 
            "Ford B-Max", "BMW 2", "Opel Zafira", "Mercedes SLK"],
    "Volume": [1.0,1.2,1.0,0.9,1.5,1.0,1.4,1.5,1.5,1.6,1.1,1.3,1.0,1.6,1.6,1.6,1.6,2.2,1.6,2.0,1.6,2.0,2.1,
               1.6,2.0,1.5,2.0,2.0,1.6,2.0,2.1,2.0,1.6,1.6,1.6,2.5],
    "Weight": [790,1160,929,865,1140,929,1109,1365,1112,1150,980,990,1112,1252,1326,1330,1365,1280,1119,1328,
               1584,1428,1365,1415,1415,1465,1490,1725,1523,1705,1605,1746,1235,1390,1405,1395],
    "CO2": [99,95,95,90,105,105,90,92,98,99,99,101,99,94,97,97,99,104,104,105,94,99,99,99,99,102,104,114,109,
            114,115,117,104,108,109,120]
}
df = pd.DataFrame(data)
print(df.head())

# -------------------------------------------------
# Step 2: Compare raw values of Weight vs Volume
# -------------------------------------------------
print("\n--- Step 2: Why Scaling is Needed ---")
print("Example: Comparing Volume=1.0 liters with Weight=790 kg makes little sense.")
print("Units differ greatly. We need scaling for fair comparison.")

# -------------------------------------------------
# Step 3: Apply Standardization (Z = (X - mean)/std)
# -------------------------------------------------
print("\n--- Step 3: Applying StandardScaler ---")
X = df[['Weight','Volume']]
y = df['CO2']

scaler = StandardScaler()
scaledX = scaler.fit_transform(X)

print("Original First Row (Weight, Volume):", X.iloc[0].values)
print("Scaled First Row:", scaledX[0])
print("\nImportant Note: Scaling makes values unitless and comparable.")

# -------------------------------------------------
# Step 4: Train Linear Regression on Scaled Data
# -------------------------------------------------
print("\n--- Step 4: Training Regression Model ---")
regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

# Predict CO2 for a car (Weight=2300 kg, Volume=1.3 liters)
scaled_input = scaler.transform([[2300, 1.3]])
predictedCO2 = regr.predict([scaled_input[0]])

print(f"Predicted CO2 for car [2300 kg, 1.3 L]: {predictedCO2[0]:.2f} g/km")

# -------------------------------------------------
# Step 5: Manual Check of Scaling Formula
# -------------------------------------------------
print("\n--- Step 5: Manual Check of Scaling Formula ---")
mean_weight, mean_volume = X['Weight'].mean(), X['Volume'].mean()
std_weight, std_volume = X['Weight'].std(), X['Volume'].std()

manual_scaled_weight = (2300 - mean_weight)/std_weight
manual_scaled_volume = (1.3 - mean_volume)/std_volume
print("Manual scaled input:", [manual_scaled_weight, manual_scaled_volume])
print("Sklearn scaled input:", scaled_input[0])

# -------------------------------------------------
# Step 6: Visualization
# -------------------------------------------------
print("\n--- Step 6: Visualizing Original vs Scaled Features ---")

plt.figure(figsize=(12,5))

# Scatter plot before scaling
plt.subplot(1,2,1)
plt.scatter(df['Weight'], df['Volume'], c='blue')
plt.xlabel("Weight (kg)")
plt.ylabel("Volume (liters)")
plt.title("Original Features (Different Scales)")

# Scatter plot after scaling
plt.subplot(1,2,2)
plt.scatter(scaledX[:,0], scaledX[:,1], c='red')
plt.xlabel("Scaled Weight")
plt.ylabel("Scaled Volume")
plt.title("Scaled Features (Standardized)")

plt.tight_layout()
plt.show()

# -------------------------------------------------
# Step 7: Important Notes
# -------------------------------------------------
print("\n--- Step 7: Key Takeaways ---")
print("1. Scaling is essential when features have very different units or ranges.")
print("2. StandardScaler rescales features to have mean=0 and std=1.")
print("3. Always apply the SAME scaler to training and new data before prediction.")
print("4. Without scaling, regression coefficients may be misleading.")
