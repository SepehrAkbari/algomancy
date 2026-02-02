'''
Swish Activation Function.
'''

import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x = np.atleast_1d(np.asarray(x, dtype=float))
    sig = 1 / (1 + np.exp(-x))
    return x * sig

if __name__ == "__main__":
    x = [[1, -1], [2, -2]]
    print(swish(x))