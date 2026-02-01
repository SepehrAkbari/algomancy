'''
Simple CNN step implementation.
'''

import numpy as np

def conv2d(x, W, b):
    """
    Simple 2D convolution layer forward pass.
    Valid padding, stride=1.
    """
    N, C_in, H, W_in = x.shape
    C_out, _, KH, KW = W.shape
    
    H_out = H - KH + 1
    W_out = W_in - KW + 1
    
    y = np.zeros((N, C_out, H_out, W_out))
    
    for n in range(N):
        for c_out in range(C_out):
            for h in range(H_out):
                for w in range(W_out):
                    y[n, c_out, h, w] = np.sum(
                        x[n, :, h:h+KH, w:w+KW] * W[c_out, :, :, :]
                    ) + b[c_out]
    return y


if __name__ == "__main__":
    x = np.ones((1,1,3,3))
    W = np.ones((1,1,2,2))
    b = [0]
    
    print(conv2d(x, W, b))
    
    
    
    