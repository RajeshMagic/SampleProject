"""
AUC-ROC Curve Demonstration in Classification
This script demonstrates:
- Imbalanced dataset challenges
- Accuracy and confusion matrix evaluation
- ROC curve plotting
- AUC calculation
- Probabilistic model evaluation
"""

# ------------------------------
# Step 1: Import required modules
# ------------------------------
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve

# ------------------------------
# Step 2: Create an imbalanced dataset
# ------------------------------
print("Step 2: Creating imbalanced dataset...")
n = 10000
ratio = 0.95  # 95% of class 1
n_0 = int((1-ratio) * n)
n_1 = int(ratio * n)

y = np.array([0]*n_0 + [1]*n_1)

# Hypothetical model that predicts majority class 1 every time
y_proba = np.array([1]*n)
y_pred = y_proba > 0.5

print("\nModel 1 (predicts only majority class)")
print(f"Accuracy score: {accuracy_score(y, y_pred):.4f}")
cf_mat = confusion_matrix(y, y_pred)
print("Confusion Matrix:")
print(cf_mat)
print(f"Class 0 accuracy: {cf_mat[0][0]/n_0 if n_0 > 0 else 'N/A'}")
print(f"Class 1 accuracy: {cf_mat[1][1]/n_1:.4f}")
print("Important Note: High accuracy is misleading for imbalanced datasets.\n")

# ------------------------------
# Step 3: Better hypothetical model with probabilities
# ------------------------------
y_proba_2 = np.array(
    np.random.uniform(0, 0.7, n_0).tolist() +  # class 0 probabilities
    np.random.uniform(0.3, 1, n_1).tolist()    # class 1 probabilities
)
y_pred_2 = y_proba_2 > 0.5

print("Model 2 (probabilistic predictions)")
print(f"Accuracy score: {accuracy_score(y, y_pred_2):.4f}")
cf_mat = confusion_matrix(y, y_pred_2)
print("Confusion Matrix:")
print(cf_mat)
print(f"Class 0 accuracy: {cf_mat[0][0]/n_0:.4f}")
print(f"Class 1 accuracy: {cf_mat[1][1]/n_1:.4f}")
print("Important Note: Accuracy is lower but predictions are more balanced.\n")

# ------------------------------
# Step 4: Define ROC curve plotting function
# ------------------------------
def plot_roc_curve(true_y, y_prob, label=None):
    """
    Plots the ROC curve based on the true labels and predicted probabilities
    """
    fpr, tpr, thresholds = roc_curve(true_y, y_prob)
    plt.plot(fpr, tpr, label=label)
    plt.plot([0, 1], [0, 1], 'k--')  # random chance line
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.grid(True)

# ------------------------------
# Step 5: Plot ROC and calculate AUC for Model 1
# ------------------------------
plt.figure(figsize=(8,6))
plot_roc_curve(y, y_proba, label="Model 1")
auc_1 = roc_auc_score(y, y_proba)
print(f"Model 1 AUC score: {auc_1:.4f}")
plt.legend()
plt.show()
print("Important Note: AUC of 0.5 indicates model cannot distinguish between classes.\n")

# ------------------------------
# Step 6: Plot ROC and calculate AUC for Model 2
# ------------------------------
plt.figure(figsize=(8,6))
plot_roc_curve(y, y_proba_2, label="Model 2")
auc_2 = roc_auc_score(y, y_proba_2)
print(f"Model 2 AUC score: {auc_2:.4f}")
plt.legend()
plt.show()
print("Important Note: Higher AUC (closer to 1) means better separation of classes.\n")

# ------------------------------
# Step 7: More confident probabilistic predictions
# ------------------------------
print("Step 7: Evaluating models with more confident probabilities...")
y_prob_1 = np.array(
    np.random.uniform(0.25, 0.5, n//2).tolist() +
    np.random.uniform(0.3, 0.7, n).tolist() +
    np.random.uniform(0.5, 0.75, n//2).tolist()
)
y_prob_2 = np.array(
    np.random.uniform(0, 0.4, n//2).tolist() +
    np.random.uniform(0.3, 0.7, n).tolist() +
    np.random.uniform(0.6, 1, n//2).tolist()
)

print(f"Model 1 accuracy score: {accuracy_score(y, y_prob_1>0.5):.4f}")
print(f"Model 2 accuracy score: {accuracy_score(y, y_prob_2>0.5):.4f}")
print(f"Model 1 AUC score: {roc_auc_score(y, y_prob_1):.4f}")
print(f"Model 2 AUC score: {roc_auc_score(y, y_prob_2):.4f}")

# Plot ROC for both models
plt.figure(figsize=(8,6))
plot_roc_curve(y, y_prob_1, label="Model 1")
plot_roc_curve(y, y_prob_2, label="Model 2")
plt.legend()
plt.show()
print("Important Note: Even if accuracies are similar, model with higher AUC is more reliable for future predictions.")
