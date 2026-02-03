'''
TD Value Update (Single Step).
'''

import numpy as np

def td_value_update(V, s, r, s_next, alpha, gamma):
    """
    Returns: updated value function V_new
    """
    V = np.asarray(V)
    V_next = V.copy()
    
    td_target = r + gamma * V[s_next]
    td_error = td_target - V[s]
    
    V_next[s] += alpha * td_error
    return V_next


if __name__ == "__main__":
    V = [0.2,0.8]
    s = 0
    r = 0
    s_next = 1
    alpha = 1.0
    gamma = 0.5
    
    print(td_value_update(V, s, r, s_next, alpha, gamma))