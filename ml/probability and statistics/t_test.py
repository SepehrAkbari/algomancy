'''
One-Sample T-Test.
'''

import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    x = np.array(x)
    n = len(x)
    x_bar = np.mean(x)
    
    s2 = np.sum((x - x_bar) ** 2) / (n - 1)
    s = np.sqrt(s2)
    
    return (x_bar - mu0) / (s / np.sqrt(n))


if __name__ == "__main__":
    x = [2.1, 2.4, 1.9, 2.6, 2.0]
    mu0 = 2.0
    print(t_test_one_sample(x, mu0))