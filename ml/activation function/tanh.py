'''
Tanh Activation Function.
'''

import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x = np.atleast_1d(np.asarray(x, dtype=float))
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

if __name__ == "__main__":
    x = [[0, 1], [-1, 2]]
    print(tanh(x))