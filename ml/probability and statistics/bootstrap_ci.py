'''
Estimating Mean and Confidence Intervals via Bootstrapping.
'''

import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    if rng is None:
        rng = np.random.default_rng()
    
    x = np.array(x)
    n = len(x)
    
    x_i = rng.choice(x, size=(n_bootstrap, n), replace=True)
    boot_means = np.mean(x_i, axis=1)
    
    
    alpha = 1 - ci
    lower = np.percentile(boot_means, 100 * (alpha / 2) )
    upper = np.percentile(boot_means, 100 * (1 - alpha / 2))
    
    return boot_means, lower, upper


if __name__ == "__main__":
    x = [1.0, 2.0, 3.0, 4.0]
    n_bootstrap = 1000
    ci = 0.90
    
    means, lower, upper = bootstrap_mean(x, n_bootstrap, ci)
    print(f"{means.shape}, {lower}, {upper}")

