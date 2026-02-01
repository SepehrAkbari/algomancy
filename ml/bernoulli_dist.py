'''
Bernoulli Distribution.
'''

import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    if p < 0 or p > 1:
        raise ValueError
    
    x = np.asarray(x)
    
    pmf = np.where(x == 1, p, 1 - p)
    mean = p
    variance = p * (1 - p)
    
    return pmf, mean, variance


if __name__ == "__main__":
    x=[0, 1, 0, 1]
    p=0.3
    
    print(bernoulli_pmf_and_moments(x, p))
    
    
    