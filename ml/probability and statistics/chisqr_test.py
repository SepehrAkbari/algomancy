'''
Chi-Square Test for Independence.
'''

import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    C = np.array(C)
    rows, cols = C.sum(axis=1), C.sum(axis=0)
    total = C.sum()
    
    E = np.outer(rows, cols) / total
    chi2_stat = ((C - E) ** 2 / E).sum()
    
    return chi2_stat, E


if __name__ == "__main__":
    C = [[20,30],[40,60]]
    print(chi2_independence(C))