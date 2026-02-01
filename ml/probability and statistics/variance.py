'''
Sample Variance and Standard Deviation by Bessel's Correction.
'''

import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    x = np.asarray(x)
    n = len(x)
    
    if n < 2:
        raise ValueError
    
    s2 = np.sum((x - np.mean(x)) ** 2) / (n - 1)
    s = np.sqrt(s2)
    
    return s2, s
    
    
if __name__ == "__main__":
    data = [10, 12, 23, 23, 16, 23, 21, 16]
    variance, std_dev = sample_var_std(data)
    print(f"S^2: {variance:.2f}\nS: {std_dev:.2f}")