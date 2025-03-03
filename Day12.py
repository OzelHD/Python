# 1️⃣ Create two NumPy arrays and perform element-wise addition, multiplication, and dot product.
# 2️⃣ Generate a 4x4 random matrix and compute its transpose.
# 3️⃣ (Optional) Implement matrix multiplication using NumPy and compare it to Python’s nested loops.

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([6, 5, 4, 3, 2, 1])

matrix = np.array([[1, 2, 3, 4],
                   [2, 3, 4, 5],
                   [3, 4, 5, 6],
                   [4, 5, 6, 7]])
ranmatrix = np.random.rand(4, 4)

transpose = ranmatrix.T

def manual_matrix_mult(A, B):
    result = [[sum(A[i][k] * B[k][j] for k in range(len(A))) for j in range(len(B[0]))] for i in range(len(A))]
    return np.array(result)

print(f"Array 1: {arr1}\nArray 2: {arr2}\nAddition: {arr1 + arr2}\nMultiplication: {arr1 * arr2}\nDot product: {arr1 @ arr2}\n")
print(f"4x4 Matrix:\n{matrix}\n\nTranspose:\n{transpose}\n")
print(f"Matrix multiplication:\n{matrix @ transpose}\n\nManual Matrix multiplication:\n{manual_matrix_mult(matrix, transpose)}") 