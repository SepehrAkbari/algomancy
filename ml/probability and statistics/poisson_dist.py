'''
Poisson Distribution.
'''

import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    if k < 0:
        return 0.0, 0.0
    
    pmf = (np.exp(-lam) * (lam ** k)) / np.exp(np.sum(np.log(np.arange(1, k+1))))
    cdf = sum((np.exp(-lam) * (lam ** i)) / np.exp(np.sum(np.log(np.arange(1, i+1)))) for i in range(k + 1))
    
    return pmf, cdf
    
    
if __name__ == "__main__":
    lam = 3.0
    k = 2
    pmf, cdf = poisson_pmf_cdf(lam, k)
    print(f"PMF: {pmf:.4f}\nCDF: {cdf:.4f}")