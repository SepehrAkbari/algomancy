'''
Euclidean Distance.
'''

import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    x = np.array(x)
    y = np.array(y)
    return float(np.sqrt(np.sum((x - y) ** 2)))


if __name__ == "__main__":
    x = [1,2,3]
    y = [4,5,6]
    print(euclidean_distance(x, y))