"""
Machine Learning - Cross Validation Demonstration
This script demonstrates:
1. K-Fold Cross Validation
2. Stratified K-Fold Cross Validation
3. Leave-One-Out (LOO) Cross Validation
4. Leave-P-Out (LPO) Cross Validation
5. Shuffle Split Cross Validation
"""

# ------------------------------
# Step 1: Import required modules
# ------------------------------
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import (KFold, StratifiedKFold, LeaveOneOut, LeavePOut,
                                     ShuffleSplit, cross_val_score)
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------
# Step 2: Load dataset
# ------------------------------
print("Step 2: Load Iris dataset...")
X, y = datasets.load_iris(return_X_y=True)
print(f"Dataset shape: X={X.shape}, y={y.shape}")
print("Important Note: Iris dataset has 150 observations and 3 classes.\n")

# ------------------------------
# Step 3: Initialize classifier
# ------------------------------
clf = DecisionTreeClassifier(random_state=42)

# ------------------------------
# Step 4: K-Fold Cross Validation
# ------------------------------
print("Step 4: K-Fold Cross Validation (k=5)")
k_folds = KFold(n_splits=5)
scores_kfold = cross_val_score(clf, X, y, cv=k_folds)
print("K-Fold CV Scores: ", scores_kfold)
print("Average K-Fold CV Score: ", scores_kfold.mean())
print("Number of CV Scores used in Average: ", len(scores_kfold), "\n")

# ------------------------------
# Step 5: Stratified K-Fold
# ------------------------------
print("Step 5: Stratified K-Fold Cross Validation (k=5)")
sk_folds = StratifiedKFold(n_splits=5)
scores_skfold = cross_val_score(clf, X, y, cv=sk_folds)
print("Stratified K-Fold CV Scores: ", scores_skfold)
print("Average Stratified K-Fold CV Score: ", scores_skfold.mean())
print("Number of CV Scores used in Average: ", len(scores_skfold), "\n")

# ------------------------------
# Step 6: Leave-One-Out (LOO)
# ------------------------------
print("Step 6: Leave-One-Out Cross Validation")
loo = LeaveOneOut()
scores_loo = cross_val_score(clf, X, y, cv=loo)
print("Average LOO CV Score: ", scores_loo.mean())
print("Number of CV Scores used in Average (should equal number of observations): ", len(scores_loo), "\n")

# ------------------------------
# Step 7: Leave-P-Out (LPO)
# ------------------------------
print("Step 7: Leave-P-Out Cross Validation (p=2)")
lpo = LeavePOut(p=2)
scores_lpo = cross_val_score(clf, X, y, cv=lpo)
print("Average LPO CV Score: ", scores_lpo.mean())
print("Number of CV Scores used in Average: ", len(scores_lpo), "\n")

# ------------------------------
# Step 8: Shuffle Split
# ------------------------------
print("Step 8: Shuffle Split Cross Validation (train_size=0.6, test_size=0.3, n_splits=5)")
ss = ShuffleSplit(train_size=0.6, test_size=0.3, n_splits=5, random_state=42)
scores_ss = cross_val_score(clf, X, y, cv=ss)
print("Shuffle Split CV Scores: ", scores_ss)
print("Average Shuffle Split CV Score: ", scores_ss.mean())
print("Number of CV Scores used in Average: ", len(scores_ss), "\n")

# ------------------------------
# Step 9: Visualization of CV Scores
# ------------------------------
methods = ['K-Fold', 'Stratified K-Fold', 'LOO', 'LPO', 'ShuffleSplit']
average_scores = [scores_kfold.mean(), scores_skfold.mean(), scores_loo.mean(), scores_lpo.mean(), scores_ss.mean()]

plt.figure(figsize=(10,6))
plt.bar(methods, average_scores, color='skyblue', edgecolor='k')
plt.ylim([0.8, 1])
plt.ylabel("Average CV Score")
plt.title("Comparison of Cross Validation Methods")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
print("Important Note: This bar plot compares the average CV scores across different CV methods.")
print("Observation: Stratified methods generally perform better on imbalanced datasets.\n")
