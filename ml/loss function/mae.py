'''
Mean Absolute Error.
'''

import numpy as np

def mean_absolute_error(y_pred, y_true):
    """
    Returns: float MAE
    """
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)

    res = (y_pred - y_true)
    return np.mean(np.abs(res))

if __name__ == "__main__":
    y_pred = [2, 3]
    y_true = [1, 1]
    print(mean_absolute_error(y_pred, y_true))