'''
Sigmoid function vectorized implementation.
'''

import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.asarray(x, dtype=float)
    return 1 / (1 + np.exp(-x))


if __name__ == "__main__":
    x = [[0, 2, -2], [1, -1, 0]]
    print("Sigmoid output:\n", sigmoid(x))