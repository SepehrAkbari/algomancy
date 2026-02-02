'''
Leaky ReLU Activation Function.
'''

import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    x = np.atleast_1d(np.asarray(x, dtype=float))
    return np.where(x >= 0, x, alpha * x)

if __name__ == "__main__":
    x = [-2, -1, 0, 1, 2]
    a = 0.1
    print(leaky_relu(x, alpha=a))