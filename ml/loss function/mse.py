'''
Mean Squared Error.
'''

import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)

    res = (y_pred - y_true)
    return np.mean(res ** 2)


if __name__ == "__main__":
    y_pred = [2, 3]
    y_true = [1, 1]
    print(mean_squared_error(y_pred, y_true))