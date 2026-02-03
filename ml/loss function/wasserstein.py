'''
Wasserstein Critic Loss.
'''

import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    real_scores = np.asarray(real_scores, dtype=float)
    fake_scores = np.asarray(fake_scores, dtype=float)
    
    if real_scores.ndim != 1 or fake_scores.ndim != 1:
        raise ValueError

    l = np.mean(fake_scores) - np.mean(real_scores)
    return float(l)


if __name__ == "__main__":
    real_scores=[2.0, 1.5, 3.0]
    fake_scores=[-1.0, 0.0, 0.5]
    print(wasserstein_critic_loss(real_scores, fake_scores))