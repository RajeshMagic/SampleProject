"""
CategoricalData.py
Machine Learning Example: Handling Categorical Data and Predicting CO2 Emissions

This script demonstrates:
- Reading CSV data
- One-hot encoding categorical features (Car brand)
- Combining numeric and categorical features
- Training Linear Regression model
- Predicting CO2 emissions for single and multiple new cars
- Ensuring no NaN errors for new data
"""

import pandas as pd
from sklearn.linear_model import LinearRegression

# ------------------------------
# Step 1: Load the dataset
# ------------------------------
print("Step 1: Loading data...")
cars = pd.read_csv("data.csv")  # Ensure data.csv exists
print(cars.head(), "\n")
print("Important Note: Dataset has columns: Car, Model, Volume, Weight, CO2\n")

# ------------------------------
# Step 2: One-Hot Encode 'Car' column (0/1)
# ------------------------------
print("Step 2: One-Hot Encoding categorical column 'Car'...")
ohe_cars = pd.get_dummies(cars[['Car']], drop_first=False).astype(int)  # convert True/False to 0/1
print(ohe_cars.head(), "\n")

# ------------------------------
# Step 3: Prepare features and target
# ------------------------------
print("Step 3: Creating feature matrix X and target y...")
X = pd.concat([cars[['Volume', 'Weight']], ohe_cars], axis=1)
y = cars['CO2']
print(f"X shape: {X.shape}, y shape: {y.shape}\n")
print("Important Note: Each coefficient represents the impact of that feature on CO2 emissions.\n")

# ------------------------------
# Step 4: Train Linear Regression model
# ------------------------------
print("Step 4: Training Linear Regression model...")
regr = LinearRegression()
regr.fit(X, y)
print("Model trained successfully!\n")
print("Model Coefficients:")
for feature, coef in zip(X.columns, regr.coef_):
    print(f"{feature}: {coef:.4f}")
print(f"Intercept: {regr.intercept_:.4f}\n")

# ------------------------------
# Step 5: Predict CO2 for a single new car
# ------------------------------
print("Step 5: Predict CO2 for a VW with Volume=1300, Weight=2300...")
new_car = {'Volume': 1300, 'Weight': 2300, 'Car_VW': 1}  # VW set to 1
new_car_df = pd.DataFrame([new_car])

# Fill missing columns with 0
for col in X.columns:
    if col not in new_car_df.columns:
        new_car_df[col] = 0

# Reorder columns to match training data
new_car_df = new_car_df[X.columns]

predicted_CO2 = regr.predict(new_car_df)
print(f"Predicted CO2 emission: {predicted_CO2[0]:.2f} g/km\n")

# ------------------------------
# Step 6: Predict CO2 for multiple new cars
# ------------------------------
print("Step 6: Predict CO2 for multiple new cars...")

new_cars_data = [
    {'Volume': 1400, 'Weight': 1200, 'Car_BMW': 1},       # BMW
    {'Volume': 2000, 'Weight': 1500, 'Car_Audi': 1},      # Audi
    {'Volume': 1600, 'Weight': 1300, 'Car_Mercedes': 1},  # Mercedes
]

new_cars_df = pd.DataFrame(new_cars_data)

# Fill missing columns with 0 and reorder
for col in X.columns:
    if col not in new_cars_df.columns:
        new_cars_df[col] = 0
new_cars_df = new_cars_df[X.columns]

# Predict
predictions = regr.predict(new_cars_df)

print("Predicted CO2 emissions for new cars:")
for i, co2 in enumerate(predictions):
    print(f"Car {i+1}: {co2:.2f} g/km")

print("\nImportant Notes:")
print("- Always ensure new data has the same features as the training data.")
print("- Missing one-hot columns must be filled with 0.")
print("- Column order must match training feature matrix to avoid errors.")
