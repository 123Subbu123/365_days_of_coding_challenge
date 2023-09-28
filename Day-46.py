## 53.Python program to divide two matrix
import numpy as np

# Define two matrices A and B
A = np.array([[2, 4], [6, 8]])
B = np.array([[1, 2], [3, 4]])

# Check if matrix B is invertible
if np.linalg.det(B) != 0:
    # Calculate the inverse of matrix B
    B_inv = np.linalg.inv(B)

    # Perform matrix division: A / B
    result = np.dot(A, B_inv)
    print("Result of matrix division A / B:")
    print(result)
else:
    print("Matrix B is not invertible. Division is not possible.")
