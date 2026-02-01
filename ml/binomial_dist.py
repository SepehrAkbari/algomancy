'''
Binomial Distribution.
'''

import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    if k < 0 or k > n:
        return 0.0, 0.0
    
    pmf = comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    cdf = sum(comb(n, i) * (p ** i) * ((1 - p) ** (n - i)) for i in range(k + 1))
    
    return pmf, cdf


if __name__ == "__main__":
    n = 5
    p = 0.5
    k = 2
    pmf, cdf = binomial_pmf_cdf(n, p, k)
    print(f"PMF: {pmf}\nCDF: {cdf}")