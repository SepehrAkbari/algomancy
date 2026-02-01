'''
ReLU Activation Function.
'''

import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    x = np.atleast_1d(np.asarray(x, dtype=float))
    return np.maximum(0, x)

if __name__ == "__main__":
    x = [[-1, 2], [3, -4]]
    print(relu(x))