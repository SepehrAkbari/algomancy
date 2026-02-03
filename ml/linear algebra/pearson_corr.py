'''
Pearson Correlation Matrix.
'''

import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    X = np.asarray(X, dtype=float)
    
    if X.ndim != 2 or X.shape[0] < 2:
        return None

    X_centered = X - np.mean(X, axis=0)
    cov_matrix = (X_centered.T @ X_centered) / (X.shape[0] - 1)
    
    std = np.std(X, axis=0, ddof=1)
    std_matrix = np.outer(std, std)
    
    with np.errstate(divide='ignore', invalid='ignore'):
        corr = cov_matrix / std_matrix
    
    np.fill_diagonal(corr, 1.0)
    
    return corr


if __name__ == "__main__":
    X = [[1, 6], [2, 4], [3, 2]]
    print(pearson_correlation(X))
    