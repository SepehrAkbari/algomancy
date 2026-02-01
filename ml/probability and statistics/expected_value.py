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


if __name__ == "__main__":
    x = [1,2,3,4]
    p = [0.1,0.2,0.3,0.4]
    print(expected_value_discrete(x, p))