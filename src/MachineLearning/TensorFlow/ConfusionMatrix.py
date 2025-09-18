# Machine Learning - Confusion Matrix Demonstration
# Author: Training Script
# -------------------------------------------------
# This script demonstrates:
#   - Creating actual and predicted values for classification
#   - Creating a Confusion Matrix
#   - Visualizing the Confusion Matrix
#   - Calculating key metrics: Accuracy, Precision, Recall, Specificity, F1-score
# -------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

# -------------------------------------------------
# Step 1: Generate Actual and Predicted Data
# -------------------------------------------------
# For demonstration purposes, we generate random binary data
np.random.seed(42)  # Ensures reproducibility

# Actual outcomes (1 = Positive, 0 = Negative)
actual = np.random.binomial(1, 0.9, size=1000)

# Predicted outcomes (simulate model predictions)
predicted = np.random.binomial(1, 0.9, size=1000)

print("\n--- Step 1: Sample of Actual vs Predicted ---")
for i in range(10):
    print(f"Actual: {actual[i]}, Predicted: {predicted[i]}")

# -------------------------------------------------
# Step 2: Create Confusion Matrix
# -------------------------------------------------
conf_matrix = metrics.confusion_matrix(actual, predicted)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=[0,1])

print("\n--- Step 2: Confusion Matrix ---")
print(conf_matrix)

# Visualize Confusion Matrix
cm_display.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix")
plt.show()

# Important note
print("\nImportant Note:")
print("Top-Left: True Negatives (TN)")
print("Top-Right: False Positives (FP)")
print("Bottom-Left: False Negatives (FN)")
print("Bottom-Right: True Positives (TP)")

# -------------------------------------------------
# Step 3: Calculate Key Metrics
# -------------------------------------------------
# Accuracy: How often is the model correct
Accuracy = metrics.accuracy_score(actual, predicted)

# Precision: Of predicted positives, how many are truly positive
Precision = metrics.precision_score(actual, predicted)

# Recall (Sensitivity): Of all actual positives, how many were correctly predicted
Sensitivity_recall = metrics.recall_score(actual, predicted)

# Specificity: How well the model predicts negatives
Specificity = metrics.recall_score(actual, predicted, pos_label=0)

# F1-score: Harmonic mean of Precision and Recall
F1_score = metrics.f1_score(actual, predicted)

# -------------------------------------------------
# Step 4: Display Metrics
# -------------------------------------------------
print("\n--- Step 3: Classification Metrics ---")
print(f"Accuracy: {Accuracy:.4f}")
print(f"Precision: {Precision:.4f}")
print(f"Sensitivity (Recall): {Sensitivity_recall:.4f}")
print(f"Specificity: {Specificity:.4f}")
print(f"F1-score: {F1_score:.4f}")

# Important notes for understanding metrics
print("\nImportant Notes on Metrics:")
print("1. Accuracy = (TP + TN) / Total predictions")
print("2. Precision = TP / (TP + FP)")
print("3. Recall (Sensitivity) = TP / (TP + FN)")
print("4. Specificity = TN / (TN + FP)")
print("5. F1-score = 2 * (Precision * Recall) / (Precision + Recall)")
print("6. Metrics help evaluate classification model performance, especially for imbalanced datasets.")
