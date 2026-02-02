'''
Trace of a Matrix.
'''

import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    A = np.atleast_2d(np.asarray(A))

    if A.shape[0] != A.shape[1] or A.ndim != 2:
        return ValueError

    trace = 0
    for i in range(A.shape[0]):
        trace += A[i,i]

    return trace


if __name__ == "__main__":
    A = [[-1, 0, 2], [3, 5, -3], [0, -2, 4]]
    print(matrix_trace(A))