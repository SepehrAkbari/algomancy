'''
Eigenvalue of a Matrix.
'''

import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    matrix = np.asarray(matrix, dtype=float)

    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or matrix.size == 0:
        return None

    eign = np.linalg.eigvals(matrix)
    idx = np.lexsort((eign.imag, eign.real))
    return eign[idx]

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5]]
    print(calculate_eigenvalues(matrix))