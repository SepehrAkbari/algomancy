'''
Transpose of a Matrix.
'''

import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.asarray(A)
    n, m = A.shape
    T = np.zeros((m, n))

    for row in range(n):
        for col in range(m):
            T[col, row] = A[row, col]

    return T


if __name__ == "__main__":
    A = [[1, 3, 5], [3, 6, -5]]
    print(matrix_transpose(A))