'''
Positional Encoding (sin/cos) for Transformer.
'''

import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    pos = np.arange(seq_len)[:, np.newaxis]
    div = np.power(base, np.arange(0, d_model, 2) / d_model)
    angles = pos / div
    
    pe = np.zeros((seq_len, d_model))
    
    pe[:, 0::2] = np.sin(angles)
    pe[:, 1::2] = np.cos(angles[:, :d_model // 2])
    
    return pe.astype(float)
    
def add_positional_encoding(x, base=10000.0):
    """
    Add PE to input x of shape (B, T, d_model); return same shape.
    """
    B, T, d_model = x.shape
    pe = positional_encoding(T, d_model, base)
    return x + pe


if __name__ == "__main__":
    seq_len = 3
    d_model = 4
    print(positional_encoding(seq_len, d_model))