'''
3D Vector Normalization.
'''

import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    v = np.asarray(v, dtype=float)
    
    if v.shape == (3,):
        v = v.reshape(1, 3)
    elif len(v.shape) != 2 or v.shape[1] != 3:
        raise ValueError
    
    norms = np.linalg.norm(v, axis=1, keepdims=True)
    norms = np.where(norms < 1e-10, 1, norms)
    v_norm = v / norms

    if v.shape == (3,):
        v_norm = v_norm.reshape(3,)
        
    return v_norm

if __name__ == "__main__":
    v = [[0, 0, 0], [1, 2, 2]]
    print(normalize_3d(v))

