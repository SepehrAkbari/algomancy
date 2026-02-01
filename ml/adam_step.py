'''
Adam optimizer step implementation.
'''

import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    m_new = beta1 * m + (1 - beta1) * grad
    v_new = beta2 * v + (1 - beta2) * (grad ** 2)

    m_hat = m_new / (1 - beta1 ** t)
    v_hat = v_new / (1 - beta2 ** t)

    param_new = param - lr * m_hat / (np.sqrt(v_hat) + eps)
    
    return param_new, m_new, v_new


if __name__ == "__main__":
    param = np.array([1.0, 2.0])
    grad = np.array([0.1, 0.2])
    m = np.zeros_like(param)
    v = np.zeros_like(param)
    t = 1

    param_new, m_new, v_new = adam_step(param, grad, m, v, t)
    print("Updated parameters:", param_new)
    print("Updated first moment:", m_new)
    print("Updated second moment:", v_new)