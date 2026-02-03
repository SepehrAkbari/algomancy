'''
Huber Loss.
'''

import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)

    res = (y_pred - y_true)

    l = np.where(np.abs(res) <= delta, 0.5 * (res ** 2), delta * (np.abs(res) - 0.5 * delta))
    return np.mean(l)


if __name__ == "__main__":
    y_true=[1, 2, 3]
    y_pred=[1.5, 1.7, 2.5]
    delta=1.0
    print(huber_loss(y_true, y_pred, delta))