'''
Discounted Returns.
'''

def discount_returns(rewards, gamma):
    """
    Compute the discounted return at every timestep.
    """
    T = len(rewards)
    G = [0] * T
    
    G[T - 1] = rewards[T - 1]
    for t in reversed(range(T - 1)):
        G[t] = rewards[t] + gamma * G[t + 1]
    
    return G
    

if __name__ == "__main__":
    rewards = [1, 1, 1]
    gamma = 1.0
    print(discount_returns(rewards, gamma))
    
