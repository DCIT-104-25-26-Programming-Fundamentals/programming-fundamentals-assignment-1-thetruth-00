# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_matrix(matrix):
    """Displays a matrix in a neat, aligned grid format."""
    for row in matrix:
        print(" ".join(f"{num:>5}" for num in row))
    print()  # Add an empty line after the matrix for better readability


def transpose_matrix(matrix):
    """Computes and returns the transpose of a matrix."""
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed


def add_matrices(matrixA, matrixB):
    """Computes and returns the element-wise sum of two matrices."""
    rows = len(matrixA)
    cols = len(matrixA[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrixA[i][j] + matrixB[i][j]
    return result


def multiply_matrices(matrixA, matrixB):
    """Computes and returns the product of two matrices (A x B)."""
    rowsA = len(matrixA)
    colsA = len(matrixA[0])
    colsB = len(matrixB[0])
    
    result = [[0] * colsB for _ in range(rowsA)]
    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                # Fixed typo: must use matrixA and matrixB with index 'k'
                result[i][j] += matrixA[i][k] * matrixB[k][j]
    return result


def get_matrix_input(name, rows, cols):
    """Helper function to read a matrix from the user row by row."""
    print(f"\nEntering data for Matrix {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"  Enter row {i + 1}: ")
            row = [int(x) for x in row_input.split()]
            if len(row) == cols:
                matrix.append(row)
                break
            print(f"  Error: Row must contain exactly {cols} values. Try again.")
    return matrix


# =============================================================================
# MAIN PROGRAM DRIVER
# =============================================================================
if __name__ == "__main__":
    print("--- PART A: TRANSPOSE A MATRIX ---")
    rA = int(input("Enter number of rows for Matrix A: "))
    cA = int(input("Enter number of columns for Matrix A: "))
    matrixA = get_matrix_input("A", rA, cA)
    
    print("\nOriginal Matrix A:")
    print_matrix(matrixA)
    
    print("Transposed Matrix A:")
    transposedA = transpose_matrix(matrixA)
    print_matrix(transposedA)

    print("--- PART B: ADD TWO MATRICES ---")
    print(f"To add, Matrix B must also be {rA}x{cA}.")
    matrixB = get_matrix_input("B", rA, cA)
    
    print("\nMatrix B:")
    print_matrix(matrixB)
    
    print("Matrix A + Matrix B:")
    sum_result = add_matrices(matrixA, matrixB)
    print_matrix(sum_result)

    print("--- PART C: MULTIPLY TWO MATRICES ---")
    print(f"To multiply A * B, Matrix B must have {cA} rows.")
    rB = cA
    cB = int(input(f"Enter number of columns for Matrix B: "))
    matrixB_mult = get_matrix_input("B (for multiplication)", rB, cB)
    
    print("\nMatrix A:")
    print_matrix(matrixA)
    print("Matrix B:")
    print_matrix(matrixB_mult)
    
    print("Matrix Product (A x B):")
    product_result = multiply_matrices(matrixA, matrixB_mult)
    print_matrix(product_result)