## 52.Matrix multiplication using nested loop.
# Define the matrices A and B
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Initialize the result matrix C with zeros
C = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Perform matrix multiplication
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

# Print the result matrix C
print("Result of matrix multiplication:")
for row in C:
    print(row)
