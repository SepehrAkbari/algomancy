'''
Cosine Similarity.
'''

import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a = np.asarray(a)
    b = np.asarray(b)

    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)

    if a_norm == 0 or b_norm == 0:
        return 0.0
    else:
        return float(np.dot(a, b)) / (a_norm * b_norm)
    

if __name__ == "__main__":
    a=[1,2,3]
    b=[2,4,6]
    print(cosine_similarity(a, b))