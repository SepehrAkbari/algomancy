'''
Expected Value for Discrete Random Variables.
'''

import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    if not np.isclose(np.sum(p), 1):
        raise ValueError
    
    x = np.asarray(x)
    p = np.asarray(p)
    return np.sum(x * p)