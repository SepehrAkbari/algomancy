'''
Covariance Matrix. WITHOUT using np.cov
'''

import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X = np.asarray(X)

    if X.shape[0] < 2 or len(X.shape) != 2:
        return None

    X_centered = X - np.mean(X, axis=0)
    
    return (X_centered.T @ X_centered) / (X.shape[0] - 1)


if __name__ == "__main__":
    X = [[1, 2, 5], [2, 3, 6], [3, 4, 1]]
    print(covariance_matrix(X))