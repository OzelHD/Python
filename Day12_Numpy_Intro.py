#   Unlike the other files, this one is purely ChatGPT created. It only serves as a little library in case I forget
#   any syntax and want to have a quick peek ;) - Ozel



import numpy as np

# Creating arrays
a = np.array([1, 2, 3])  # 1D array
b = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array (matrix)

print(a)  # Output: [1 2 3]
print(b)

np.zeros((2, 3))    # 2x3 matrix filled with 0s
np.ones((3, 3))     # 3x3 matrix filled with 1s
np.eye(3)           # Identity matrix (3x3)

np.random.rand(2, 3)  # Random values between 0 and 1 in a 2x3 matrix

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)  # Output: [5 7 9]
print(x * y)  # Output: [4 10 18]
print(x @ y)  # Dot product (1*4 + 2*5 + 3*6 = 32)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A @ B)  # Matrix multiplication
print(np.dot(A, B))  # Same as @ operator
print(A.T)  # Transpose of A
