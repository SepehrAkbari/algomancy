'''
Dot Product.
'''

import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    x = np.array(x)
    y = np.array(y)
    return float(np.dot(x, y))


if __name__ == "__main__":
    x = [1,2,3]
    y = [4,5,6]
    print(dot_product(x, y))