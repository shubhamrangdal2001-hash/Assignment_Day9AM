# matrix_ops.py
# Matrix operations module using plain Python lists


def matrix_add(A, B):
    """
    Adds two matrices element-wise.
    Returns the resulting matrix.
    """
    # Check if dimensions match
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")
    result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return result


def matrix_transpose(matrix):
    """
    Returns the transpose of a matrix.
    Uses zip(*matrix) with nested list comprehension.
    """
    # zip(*matrix) groups columns together
    return [list(row) for row in zip(*matrix)]


def matrix_multiply(A, B):
    """
    Multiplies two matrices using dot product logic.
    Handles dimension mismatch gracefully.
    """
    # Number of columns in A must equal rows in B
    if len(A[0]) != len(B):
        raise ValueError(
            f"Dimension mismatch: A has {len(A[0])} columns but B has {len(B)} rows."
        )
    result = [
        [sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*B)]
        for row_a in A
    ]
    return result


def print_matrix(matrix, label="Matrix"):
    """Helper to print a matrix nicely."""
    print(f"\n{label}:")
    for row in matrix:
        print(" ", row)


# ---- Testing ----
if __name__ == "__main__":
    # Test with 2x2 matrices
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]

    print("=" * 40)
    print("Test 1: 2x2 Matrices")
    print("=" * 40)
    print_matrix(a, "Matrix A")
    print_matrix(b, "Matrix B")
    print_matrix(matrix_add(a, b), "A + B")
    print_matrix(matrix_transpose(a), "Transpose of A")
    print_matrix(matrix_multiply(a, b), "A x B")

    # Test with 3x3 matrices
    c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    d = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    print("\n" + "=" * 40)
    print("Test 2: 3x3 Matrices")
    print("=" * 40)
    print_matrix(c, "Matrix C")
    print_matrix(d, "Matrix D")
    print_matrix(matrix_add(c, d), "C + D")
    print_matrix(matrix_transpose(c), "Transpose of C")
    print_matrix(matrix_multiply(c, d), "C x D")

    # Test dimension mismatch
    print("\n" + "=" * 40)
    print("Test 3: Dimension Mismatch (should raise error)")
    print("=" * 40)
    try:
        e = [[1, 2, 3]]
        f = [[1, 2], [3, 4]]
        matrix_multiply(e, f)
    except ValueError as err:
        print(f"  Caught error: {err}")
