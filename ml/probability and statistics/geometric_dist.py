'''
Geometric Distribution.
'''

import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    k = np.array(k)
    
    if p < 0 or p > 1 or np.any(k < 1):
        return 0.0, 0.0
    
    pmf = p * ((1 - p) ** (k - 1))
    mean = 1 / p
    
    return pmf, mean

if __name__ == "__main__":
    k = [1, 2, 3]
    p = 0.4
    pmf, mean = geometric_pmf_mean(k, p)
    print(f"PMF: {pmf}\nMean: {mean:.2f}")