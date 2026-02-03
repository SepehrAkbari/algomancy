'''
Advantage of Time Steps.
'''

import numpy as np

def compute_advantage(states, rewards, V, gamma):
    """
    Returns: A (NumPy array of advantages)
    """
    V = np.asarray(V)
    A = np.zeros(len(states))
    
    G_t = 0.0
    for t in reversed(range(len(states))):
        G_t = rewards[t] + gamma * G_t
        A[t] = G_t - V[states[t]]
    
    return A


if __name__ == "__main__":
    states = [0,1,2]
    rewards = [1,2,3]
    V = [0.5,1,1.5]
    gamma = 1
    
    print(compute_advantage(states, rewards, V, gamma))
