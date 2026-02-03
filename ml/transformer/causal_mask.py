'''
Causal mask for Attention in Transformer.
'''

import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    """
    scores: np.ndarray with shape (..., T, T)
    mask_value: float used to mask future positions (e.g., -1e9)
    Return: masked scores (same shape, dtype=float)
    """
    T = scores.shape[-1]
    
    mask = np.triu(np.ones((T, T), dtype=bool), k=1)
    masked_scores = scores.copy().astype(float)
    
    masked_scores[..., mask] = mask_value
    return masked_scores


if __name__ == "__main__":
    scores = np.array([[[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]]])
    print(apply_causal_mask(scores))