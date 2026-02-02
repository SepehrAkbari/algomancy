'''
SELU Activation Function.
'''

import math

def selu(x):
    """
    Apply SELU activation to each element.
    """
    # constant values
    LAM = 1.0507009873554804934193349852946
    ALPHA = 1.6732632423543772848170429916717
    
    vals = []
    for elem in x:
        if elem >= 0:
            vals.append(LAM * elem)
        else:
            vals.append(LAM * ALPHA * (math.exp(elem) - 1))
    return vals


if __name__ == "__main__":
    x = [1.0, -1.0, 0.0, 0.5, 1.5, 2.5]
    print(selu(x))