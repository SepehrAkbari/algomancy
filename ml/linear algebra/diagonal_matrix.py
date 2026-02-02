'''
Constructing Diagonal Matrix from Vector.
'''

import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    v = np.asarray(v)
    
    n = v.shape[0]
    D = np.zeros((n, n))
    
    for i in range(n):
        D[i, i] = v[i]
        
    return D


if __name__ == "__main__":
    v = [1, 2, 3]
    print(make_diagonal(v))