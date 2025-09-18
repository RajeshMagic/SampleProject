# Machine Learning - Preprocessing Categorical Data
# -------------------------------------------------
# This script demonstrates:
#   - Loading a dataset
#   - Handling categorical data using One Hot Encoding
#   - Using linear regression to predict a numeric variable (CO2)
#   - Using dummy variables to avoid multicollinearity
#   - Making predictions
# -------------------------------------------------

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# -------------------------------------------------
# Step 1: Load Dataset
# -------------------------------------------------
# For this demonstration, ensure 'data.csv' exists in the current directory
# The dataset contains car information: Car, Model, Volume, Weight, CO2

cars = pd.read_csv("data.csv")
print("\n--- Step 1: Dataset Overview ---")
print(cars.head(10))  # Show first 10 rows

# Important Note
print("\nImportant Note: 'Car' and 'Model' are categorical columns. "
      "We cannot use them directly in ML models.")

# -------------------------------------------------
# Step 2: One Hot Encoding of Categorical Data
# -------------------------------------------------
# Transform the 'Car' column into numeric columns using get_dummies
ohe_cars = pd.get_dummies(cars[['Car']])
print("\n--- Step 2: One Hot Encoding 'Car' Column ---")
print(ohe_cars.head(10))

# -------------------------------------------------
# Step 3: Combine numerical and encoded categorical features
# -------------------------------------------------
# Concatenate original numerical features with the encoded categorical variables
X = pd.concat([cars[['Volume', 'Weight']], ohe_cars], axis=1)
y = cars['CO2']

print("\n--- Step 3: Combined Features ---")
print(X.head(5))

# Important Note
print("\nImportant Note: Now the dataset is fully numeric and ready for ML models.")

# -------------------------------------------------
# Step 4: Train Linear Regression Model
# -------------------------------------------------
regr = LinearRegression()
regr.fit(X, y)

print("\n--- Step 4: Linear Regression Model Trained ---")
print("Model Coefficients:")
coeff_df = pd.DataFrame({'Feature': X.columns, 'Coefficient': regr.coef_})
print(coeff_df)

print(f"Intercept: {regr.intercept_}")

# Important Note
print("\nImportant Note: Each coefficient represents the impact of that feature on CO2 emissions.")

# -------------------------------------------------
# Step 5: Predict CO2 Emission for a New Car
# -------------------------------------------------
# Example: Predict CO2 for a VW with weight=2300 kg, volume=1300 cm^3
# We need to provide values for all one-hot encoded columns
# Order: [Volume, Weight, Car_Audi, Car_BMW, ..., Car_Volvo]
# VW corresponds to 1 in the 'Car_VW' column
new_car_features = [1300, 2300] + [0]*16 + [1] + [0]  # Adjust according to columns

predicted_CO2 = regr.predict([new_car_features])
print("\n--- Step 5: Prediction ---")
print(f"Predicted CO2 emission for VW (Volume=1300, Weight=2300): {predicted_CO2[0]:.2f} g/km")

# -------------------------------------------------
# Step 6: Dummy Variable Technique (drop_first)
# -------------------------------------------------
# Demonstrate creating dummy variables while dropping the first column
colors = pd.DataFrame({'color': ['blue', 'red', 'green']})
dummies = pd.get_dummies(colors, drop_first=True)
dummies['color'] = colors['color']

print("\n--- Step 6: Dummy Variable Encoding with drop_first ---")
print(dummies)

# Important Note
print("\nImportant Note: Dropping the first column avoids multicollinearity in regression models.")

# -------------------------------------------------
# Step 7: Optional Visualization
# -------------------------------------------------
# Visualize the relationship between CO2 and Volume
plt.scatter(cars['Volume'], cars['CO2'], color='blue', label='CO2 vs Volume')
plt.title("Scatter Plot of CO2 vs Engine Volume")
plt.xlabel("Engine Volume (cm3)")
plt.ylabel("CO2 Emissions (g/km)")
plt.grid(True)
plt.legend()
plt.show()
