'''
Sampling from a Replay Buffer.
'''

import random

def replay_buffer_sample(buffer, batch_size, seed):
    """
    Sample a batch of transitions from the replay buffer.
    """
    random.seed(seed)
    return random.sample(buffer, batch_size)


if __name__ == "__main__":
    buffer = [[0, 0, 1.0, 1, 0], [1, 1, 0.5, 2, 0], [2, 0, -1.0, 3, 1], 
              [3, 1, 2.0, 4, 0], [4, 0, 0.0, 0, 1]]
    batch_size = 3
    seed = 42
    
    print(replay_buffer_sample(buffer, batch_size, seed))