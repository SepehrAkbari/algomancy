'''
Mean, Median, and Mode.
'''

import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    freq = Counter(x)
    return np.mean(x), np.median(x), freq.most_common(1)[0][0]

if __name__ == "__main__":
    data = [1, 2, 2, 3, 4]
    print(mean_median_mode(data))