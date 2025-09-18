"""
multiple_regression_demo.py
Demonstrates Multiple Linear Regression using Python, Pandas, Matplotlib, and Scikit-Learn.
Author: OpenAI ChatGPT

Concepts Covered:
 - Reading dataset into DataFrame
 - Defining independent (X) and dependent (y) variables
 - Fitting Multiple Linear Regression model
 - Predicting new values
 - Understanding model coefficients
 - Demonstrating effect of changing variables
 - Visualization with 3D scatter + regression plane
 - Console explanations with Important Notes
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import linear_model

print("\n================ MULTIPLE LINEAR REGRESSION DEMO =================\n")
print("Multiple Regression models a dependent variable (CO2) using multiple independent variables (Weight, Volume).\n")

# ------------------------------------------------------------
# 1) Load Dataset
# ------------------------------------------------------------
print("1) Loading Dataset (Cars: Model, Volume, Weight, CO2)\n")

data = {
    "Car": ["Toyota Aygo","Mitsubishi Space Star","Skoda Citigo","Fiat 500","Mini Cooper","VW Up!","Skoda Fabia",
            "Mercedes A-Class","Ford Fiesta","Audi A1","Hyundai I20","Suzuki Swift","Ford Fiesta","Honda Civic",
            "Hundai I30","Opel Astra","BMW 1","Mazda 3","Skoda Rapid","Ford Focus","Ford Mondeo","Opel Insignia",
            "Mercedes C-Class","Skoda Octavia","Volvo S60","Mercedes CLA","Audi A4","Audi A6","Volvo V70","BMW 5",
            "Mercedes E-Class","Volvo XC70","Ford B-Max","BMW 2","Opel Zafira","Mercedes SLK"],
    "Volume": [1000,1200,1000,900,1500,1000,1400,1500,1500,1600,1100,1300,1000,1600,1600,1600,1600,2200,1600,
               2000,1600,2000,2100,1600,2000,1500,2000,2000,1600,2000,2100,2000,1600,1600,1600,2500],
    "Weight": [790,1160,929,865,1140,929,1109,1365,1112,1150,980,990,1112,1252,1326,1330,1365,1280,1119,
               1328,1584,1428,1365,1415,1415,1465,1490,1725,1523,1705,1605,1746,1235,1390,1405,1395],
    "CO2": [99,95,95,90,105,105,90,92,98,99,99,101,99,94,97,97,99,104,104,105,94,99,99,99,99,102,104,114,109,114,115,117,104,108,109,120]
}
df = pd.DataFrame(data)

print(df.head(), "\n")

# ------------------------------------------------------------
# 2) Define Independent and Dependent Variables
# ------------------------------------------------------------
print("2) Defining Independent Variables (Weight, Volume) and Dependent Variable (CO2)\n")

X = df[["Weight", "Volume"]]
y = df["CO2"]

print("Independent variables (X): Weight, Volume")
print("Dependent variable (y): CO2 Emissions\n")

# ------------------------------------------------------------
# 3) Train Regression Model
# ------------------------------------------------------------
print("3) Training Multiple Linear Regression Model\n")

regr = linear_model.LinearRegression()
regr.fit(X, y)

print("Model training complete.\n")

# ------------------------------------------------------------
# 4) Prediction Example
# ------------------------------------------------------------
print("4) Prediction Example\n")

predictedCO2 = regr.predict([[2300, 1300]])
print("Predicted CO2 for car with 2300kg weight & 1300cm³ engine:", predictedCO2[0])
print("\nImportant Note:")
print(" - This prediction is based on both Weight and Volume.")
print(" - Multiple regression uses more information than simple linear regression, hence more accurate.\n")

# ------------------------------------------------------------
# 5) Coefficients
# ------------------------------------------------------------
print("5) Coefficients of the Model\n")

print("Coefficients (Weight, Volume):", regr.coef_)
print("Intercept:", regr.intercept_, "\n")

print("Important Note:")
print(f" - Weight coefficient ({regr.coef_[0]:.6f}) means: Each +1kg increases CO2 by ~{regr.coef_[0]:.6f}g/km.")
print(f" - Volume coefficient ({regr.coef_[1]:.6f}) means: Each +1cm³ increases CO2 by ~{regr.coef_[1]:.6f}g/km.\n")

# ------------------------------------------------------------
# 6) Demonstrating Variable Change Effect
# ------------------------------------------------------------
print("6) Demonstrating Effect of Increasing Weight by 1000kg (keeping Volume=1300)\n")

predictedCO2_2300 = regr.predict([[2300, 1300]])[0]
predictedCO2_3300 = regr.predict([[3300, 1300]])[0]

print(f"Prediction (2300kg, 1300cm³): {predictedCO2_2300:.2f}")
print(f"Prediction (3300kg, 1300cm³): {predictedCO2_3300:.2f}")
print(f"Difference ≈ {predictedCO2_3300 - predictedCO2_2300:.2f}, matches coefficient of Weight × 1000.\n")

# ------------------------------------------------------------
# 7) Visualization: 3D Scatter + Regression Plane
# ------------------------------------------------------------
print("7) Visualization: 3D Scatter Plot + Regression Plane\n")

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot actual data
ax.scatter(df["Weight"], df["Volume"], df["CO2"], color='blue', s=40, label="Actual Data")

# Create regression plane
x_surf, y_surf = np.meshgrid(np.linspace(df.Weight.min(), df.Weight.max(), 20),
                             np.linspace(df.Volume.min(), df.Volume.max(), 20))
z_surf = regr.predict(np.c_[x_surf.ravel(), y_surf.ravel()]).reshape(x_surf.shape)

ax.plot_surface(x_surf, y_surf, z_surf, color='red', alpha=0.4)

ax.set_xlabel("Weight (kg)")
ax.set_ylabel("Volume (cm³)")
ax.set_zlabel("CO2 (g/km)")
ax.set_title("Multiple Regression: Weight + Volume → CO2")
ax.legend()
plt.show()

# ------------------------------------------------------------
# 8) Method Explanation
# ------------------------------------------------------------
print("================ METHOD EXPLANATION =================")
print("Method: sklearn.linear_model.LinearRegression().fit(X, y)")
print(" - Trains regression model on independent variables X and dependent variable y.\n")

print("Method: .predict([[Weight, Volume]])")
print(" - Predicts new CO2 values for given Weight & Volume.\n")

print("Method: .coef_")
print(" - Returns coefficients (effect of each independent variable).\n")

print("Method: .intercept_")
print(" - Returns base value of y when all X=0.\n")

print("================ SUMMARY / IMPORTANT POINTS =================")
print(" - Multiple Regression uses multiple independent variables (Weight, Volume).")
print(" - Model coefficients show how much each variable contributes to CO2.")
print(" - Predictions become more accurate compared to single-variable regression.")
print(" - Visualization (3D plane) helps us see combined effect of variables.")
print("================================================================\n")
