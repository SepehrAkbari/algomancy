'''
ELU Activation Function.
'''

import math

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    vals = []
    for elem in x:
        if elem >= 0:
            vals.append(elem)
        else:
            vals.append(alpha * (math.exp(elem) - 1))
    return vals


if __name__ == "__main__":
    x = [1.0, -1.0, 0.0, 2.0, -0.5]
    alpha = 1.0
    print(elu(x, alpha))