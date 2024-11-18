import math

# Function to perform QR decomposition using Gram-Schmidt orthogonalization
def qr_decompose(matrix):
    size = len(matrix)
    Q = [[0.0] * size for _ in range(size)]
    R = [[0.0] * size for _ in range(size)]
    
    for col in range(size):
        v = [matrix[row][col] for row in range(size)]
        for prev_col in range(col):
            R[prev_col][col] = sum(Q[row][prev_col] * matrix[row][col] for row in range(size))
            v = [v[row] - R[prev_col][col] * Q[row][prev_col] for row in range(size)]
        R[col][col] = math.sqrt(sum(v[row] ** 2 for row in range(size)))
        for row in range(size):
            Q[row][col] = v[row] / R[col][col] if R[col][col] != 0 else 0.0
    return Q, R

# Matrix multiplication implementation
def multiply_matrices(mat1, mat2):
    size = len(mat1)
    result = [[0.0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            result[i][j] = sum(mat1[i][k] * mat2[k][j] for k in range(size))
    return result

# Transpose a given matrix
def matrix_transpose(mat):
    size = len(mat)
    return [[mat[j][i] for j in range(size)] for i in range(size)]

# QR algorithm to find the Schur decomposition of a matrix
def qr_algorithm(matrix, max_steps=100):
    size = len(matrix)
    Q_cumulative = [[1.0 if i == j else 0.0 for j in range(size)] for i in range(size)]
    current_matrix = [row[:] for row in matrix]
    
    for _ in range(max_steps):
        Q, R = qr_decompose(current_matrix)
        current_matrix = multiply_matrices(R, Q)
        Q_cumulative = multiply_matrices(Q_cumulative, Q)
    
    return Q_cumulative, current_matrix

# Schur decomposition using QR algorithm
def schur_decompose(matrix):
    orthogonal, triangular = qr_algorithm(matrix)
    return orthogonal, triangular

# Collects input matrix from the user
def collect_matrix():
    size = int(input("Enter the size of the square matrix: "))
    print(f"Provide the {size}x{size} matrix row by row:")
    mat = []
    for row in range(size):
        entries = list(map(float, input(f"Row {row + 1}: ").split()))
        if len(entries) != size:
            raise ValueError("Each row must have the correct number of elements.")
        mat.append(entries)
    return mat

# Main execution flow
if __name__ == "__main__":
    try:
        user_matrix = collect_matrix()
        Q, T = schur_decompose(user_matrix)
        
        print("\nOrthogonal Matrix Q:")
        for row in Q:
            print(["{:.4f}".format(val) for val in row])
        
        print("\nUpper Triangular Matrix T:")
        for row in T:
            print(["{:.4f}".format(val) for val in row])
        
        eigenvalues = [T[i][i] for i in range(len(T))]
        print("\nEigenvalues:")
        print(["{:.4f}".format(eigenvalue) for eigenvalue in eigenvalues])
    
    except ValueError as err:
        print(f"Input Error: {err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

