'''
Tabular Q-learning (Single Update).
'''

import numpy as np

def q_learning_update(Q, s, a, r, s_next, alpha, gamma):
    """
    Returns: updated Q-table Q_new
    """
    Q = np.asarray(Q)  
    Q_next = Q.copy()
    
    td_target = r + gamma * np.max(Q[s_next])
    td_error = td_target - Q[s][a]
    
    Q_next[s][a] += alpha * td_error
    return Q_next
    
    
if __name__ == "__main__":
    Q = [[0,0],[0.5,1]]
    s = 0
    a = 1
    r = 1
    s_next = 1
    alpha = 0.5
    gamma = 0.9
    
    print(q_learning_update(Q, s, a, r, s_next, alpha, gamma))
    