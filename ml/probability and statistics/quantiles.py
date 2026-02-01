'''
Percentiles with Linear Interpolation.
'''

import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    x = np.sort(x)
    n = len(x)
    p = np.array(q) / 100.0
    
    r = p * (n - 1)
    
    i = r.astype(int)
    d = r - i
    
    i_next = np.clip(i + 1, 0, n - 1)
    
    return x[i] + d * (x[i_next] - x[i])

if __name__ == "__main__":
    x = [1,2,3,4]
    q = [25,50,75]
    print(percentiles(x, q))