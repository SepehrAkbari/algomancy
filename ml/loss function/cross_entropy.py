'''
Cross-Entropy Loss.
'''

import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    if not np.allclose(np.sum(y_pred, axis=1, keepdims=True), 1):
        raise ValueError
    
    p = y_pred[np.arange(len(y_true)), y_true]
    if np.all(p > 0):
        loss = -1 * np.log(p)
    else:
        raise ValueError
    
    return np.mean(loss)


if __name__ == "__main__":
    y_true = [1, 0, 1]
    y_pred = [[0.2, 0.8], [0.6, 0.4], [0.49, 0.51]]
    print(cross_entropy_loss(y_true, y_pred))