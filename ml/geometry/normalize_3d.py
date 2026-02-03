'''
3D Vector Normalization.
'''

import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    v = np.asarray(v, dtype=float)
    
    if v.ndim == 1:
        if v.shape[0] != 3: 
            raise ValueError
        v_hat = v.reshape(1, 3)
    elif v.ndim == 2:
        if v.shape[1] != 3: 
            raise ValueError
        v_hat = v
    else:
        raise ValueError

    norms = np.linalg.norm(v_hat, axis=1, keepdims=True)
    
    mask = (norms > 1e-10).flatten()
    
    res = np.zeros_like(v_hat)
    res[mask] = v_hat[mask] / norms[mask]
    
    return res.reshape(v.shape)


if __name__ == "__main__":
    v = [[0, 0, 0], [1, 2, 2]]
    print(normalize_3d(v))

