'''
GeLU Activation Function.
'''

import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: scalar, list, or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    x = np.atleast_1d(np.asarray(x, dtype=float))
    v_erf = np.vectorize(math.erf)
    return 0.5 * x * (1 + v_erf(x / math.sqrt(2)))

if __name__ == "__main__":
    x = [[-2., -1.],[0., 1.]]
    print(gelu(x))