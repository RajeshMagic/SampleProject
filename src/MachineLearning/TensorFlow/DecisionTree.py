# Machine Learning - Decision Tree Demonstration
# Author: Training Script
# -------------------------------------------------
# This script demonstrates:
#   - Creating a Decision Tree classifier
#   - Converting categorical data into numerical
#   - Fitting the model to data
#   - Visualizing the Decision Tree
#   - Predicting outcomes for new data points
#   - Understanding Gini, samples, and values
# -------------------------------------------------

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# -------------------------------------------------
# Step 1: Load Data
# -------------------------------------------------
# Our dataset contains comedian shows and whether the person attended
data = {
    'Age': [36, 42, 23, 52, 43, 44, 66, 35, 52, 35, 24, 18, 45],
    'Experience': [10, 12, 4, 4, 21, 14, 3, 14, 13, 5, 3, 3, 9],
    'Rank': [9, 4, 6, 4, 8, 5, 7, 9, 7, 9, 5, 7, 9],
    'Nationality': ['UK','USA','N','USA','USA','UK','N','UK','N','N','USA','UK','UK'],
    'Go': ['NO','NO','NO','NO','YES','NO','YES','YES','YES','YES','NO','YES','YES']
}

df = pd.DataFrame(data)

print("\n--- Step 1: Original Data ---")
print(df)

# -------------------------------------------------
# Step 2: Convert categorical columns to numerical
# -------------------------------------------------
# Nationality: {'UK':0, 'USA':1, 'N':2}
# Go: {'YES':1, 'NO':0}
df['Nationality'] = df['Nationality'].map({'UK':0, 'USA':1, 'N':2})
df['Go'] = df['Go'].map({'YES':1, 'NO':0})

print("\n--- Step 2: Convert Categorical to Numerical ---")
print(df)

# -------------------------------------------------
# Step 3: Define features and target
# -------------------------------------------------
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']

print("\n--- Step 3: Features (X) and Target (y) ---")
print("Features (X):\n", X)
print("Target (y):\n", y)

# -------------------------------------------------
# Step 4: Create and Train Decision Tree Classifier
# -------------------------------------------------
dtree = DecisionTreeClassifier()
dtree.fit(X, y)

print("\n--- Step 4: Decision Tree Created and Trained ---")
print("Decision Tree Classifier:\n", dtree)

# -------------------------------------------------
# Step 5: Visualize the Decision Tree
# -------------------------------------------------
plt.figure(figsize=(15,10))
plot_tree(dtree, feature_names=features, class_names=['NO','YES'], filled=True)
plt.title("Decision Tree Visualization")
plt.show()

# Important Note
print("\nImportant Note:")
print("1. Each node shows: Gini, samples, and value [NO, YES].")
print("2. The splits show conditions for True/False decisions.")
print("3. Gini measures impurity: 0 = pure, 0.5 = mixed.")
print("4. Decision tree splits based on features to predict the outcome.")

# -------------------------------------------------
# Step 6: Predict New Values
# -------------------------------------------------
# Example: 40 years old American comedian, 10 years experience, Rank 7
new_show_1 = [[40, 10, 7, 1]]
prediction_1 = dtree.predict(new_show_1)
print("\n--- Step 6: Predicting New Shows ---")
print(f"Prediction for 40yo USA comedian, 10 yrs experience, Rank 7: {prediction_1[0]} (1=GO, 0=NO)")

# Example: Same but Rank 6
new_show_2 = [[40, 10, 6, 1]]
prediction_2 = dtree.predict(new_show_2)
print(f"Prediction for 40yo USA comedian, 10 yrs experience, Rank 6: {prediction_2[0]} (1=GO, 0=NO)")

# -------------------------------------------------
# Step 7: Explain Predictions
# -------------------------------------------------
print("\nImportant Note:")
print("1. Decision Trees are based on probability of outcomes, not certainty.")
print("2. Predictions may vary if the tree structure changes with different training data.")
print("3. Use more data to improve tree stability and generalization.")
