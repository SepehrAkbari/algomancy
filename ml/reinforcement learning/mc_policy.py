'''
Monte Carlo Policy Evaluation.

💡 Hint 1
Process each episode backward to compute returns: Gt=rt+γGt+1.
💡 Hint 2
Use a set to track visited states per episode to ensure first-visit only.
Requirements

Use first-visit: only count first occurrence of each state per episode
Maintain running sum and count of returns per state
Return V as NumPy array of shape (n_states,)
States never visited should have value 0.0
'''

import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):
    """
    Returns: V (NumPy array of shape (n_states,))
    """
    G = np.zeros(n_states)
    N = np.zeros(n_states)
    V = np.zeros(n_states)
    
    for episode in episodes:
        visited = set()
        G_t = 0.0
        for t in reversed(range(len(episode))):
            s, r = episode[t]
            G_t = r + gamma * G_t
            if s not in visited:
                visited.add(s)
                G[s] += G_t
                N[s] += 1
                
    for s in range(n_states):
        if N[s] > 0:
            V[s] = G[s] / N[s]
            
    return V


if __name__ == "__main__":
    episodes = [[(0,1),(1,2),(2,3)]]
    gamma = 1
    n_states = 3
    
    print(mc_policy_evaluation(episodes, gamma, n_states))