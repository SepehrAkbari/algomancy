'''
Epsilon-Greedy Action Selection.
'''

import numpy as np

def epsilon_greedy(q_values, epsilon, rng=None):
    """
    Returns: action index (int)
    """
    p = rng.random() if rng else np.random.random()

    if p > epsilon:
        a = np.argmax(q_values)
    else:
        a = rng.integers(len(q_values)) if rng else np.random.randint(len(q_values))
    
    return a    


if __name__ == "__main__":
    q_values = [1,2,0.5]
    epsilon = 0.25
    print(epsilon_greedy(q_values, epsilon))