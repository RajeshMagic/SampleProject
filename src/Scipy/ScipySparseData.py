import numpy as np
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt

print("============================")
print("     SciPy Sparse Data Demo ")
print("============================\n")

# ---------------------------------------------------------------
# 1. What is Sparse Data?
# ---------------------------------------------------------------
print("[INFO] Sparse data is a dataset where most elements are zero.\n")

# Example sparse vs dense array
sparse_arr = np.array([1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0])
dense_arr = np.array([1, 2, 3, 4, 5, 6])

print("Sparse Array Example:", sparse_arr)
print("Dense Array Example:", dense_arr)

# Visualization: sparse vs dense
plt.figure(figsize=(8,3))
plt.subplot(1,2,1)
plt.title("Sparse Array")
plt.stem(range(len(sparse_arr)), sparse_arr)
plt.subplot(1,2,2)
plt.title("Dense Array")
plt.stem(range(len(dense_arr)), dense_arr)
plt.show()

# ---------------------------------------------------------------
# 2. CSR Matrix Creation
# ---------------------------------------------------------------
print("============================")
print("     CSR Matrix Creation    ")
print("============================")

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
csr = csr_matrix(arr)
print("CSR Matrix from array:")
print(csr)

print("\n[IMPORTANT NOTE] The CSR format only stores non-zero values and their positions, saving memory.")

# ---------------------------------------------------------------
# 3. Sparse Matrix Methods
# ---------------------------------------------------------------
print("\n============================")
print("     Sparse Matrix Methods  ")
print("============================")

arr2 = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr2)
print("Original Matrix:\n", arr2)

# (a) Viewing stored data
print("\nStored non-zero values:", mat.data)

# (b) Counting non-zeros
print("Non-zero element count:", mat.count_nonzero())

# (c) Eliminating zeros
mat_elim = csr_matrix(arr2)
mat_elim.eliminate_zeros()
print("\nMatrix after eliminate_zeros():")
print(mat_elim)

# (d) Eliminating duplicates
mat_dup = csr_matrix(arr2)
mat_dup.sum_duplicates()
print("\nMatrix after sum_duplicates():")
print(mat_dup)

# (e) Converting CSR -> CSC
mat_csc = csr_matrix(arr2).tocsc()
print("\nConverted to CSC format:")
print(mat_csc)

# ---------------------------------------------------------------
# 4. Visualization of Sparse Matrix
# ---------------------------------------------------------------
print("\n[INFO] Visualizing sparse matrix with non-zero values highlighted.")

plt.figure(figsize=(5,5))
plt.spy(csr_matrix(arr2), markersize=100)
plt.title("Sparse Matrix Visualization (non-zeros)")
plt.show()

# ---------------------------------------------------------------
# End of Demo
# ---------------------------------------------------------------
print("\n============================")
print(" End of Sparse Data Demo ")
print("============================")