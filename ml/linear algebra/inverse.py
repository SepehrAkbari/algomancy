'''
Inverse of a Matrix.
'''

import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    A = np.asarray(A)
    
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return None
    
    if abs(np.linalg.det(A)) < 1e-10:
        return None
    
    try:
        A_inv = np.linalg.inv(A)
        
        if np.linalg.norm(A @ A_inv - np.eye(A.shape[0])) > 1e-7:
            return None
            
        return A_inv
        
    except:
        return None
    

if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    print(matrix_inverse(A))