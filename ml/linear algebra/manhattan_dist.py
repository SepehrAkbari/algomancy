'''
Manhattan Distance.
'''

import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    x = np.array(x)
    y = np.array(y)
    return float(np.sum(np.abs(x - y)))


if __name__ == "__main__":
    x = [1,2,3]
    y = [2,4,6]
    print(manhattan_distance(x, y))