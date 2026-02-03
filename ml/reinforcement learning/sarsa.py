'''
SARSA Update.
'''

def sarsa_update(q_table, state, action, reward, next_state, next_action, alpha, gamma):
    """
    Perform one SARSA update and return the updated Q-table.
    """
    q_new = []
    for row in q_table:
        q_new.append(row.copy())
    
    td_target = reward + gamma * q_table[next_state][next_action]
    td_error = td_target - q_table[state][action]
    
    q_new[state][action] += float(alpha * td_error)
    return q_new


if __name__ == "__main__":
    q_table = [[1, 2], [3, 4]]
    state = 0
    action = 0
    alpha = 0.5
    gamma = 0.9
    reward = 5.0
    next_state = 1
    next_action = 1
    
    print(sarsa_update(q_table, state, action, reward, 
                       next_state, next_action, alpha, gamma))