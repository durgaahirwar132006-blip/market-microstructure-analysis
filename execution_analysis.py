import numpy as np

def almgren_chriss_trajectory(total_shares=100000, num_steps=10, risk_aversion=1e-6, volatility=0.02, eta=1e-5):
    gamma = risk_aversion * (volatility ** 2)
    kappa = np.sqrt(gamma / eta) if eta > 0 else 0
    trajectory = []
    for t in range(num_steps + 1):
        if kappa > 0:
            shares_at_t = total_shares * (np.sinh(kappa * (1.0 - t / num_steps)) / np.sinh(kappa))
        else:
            shares_at_t = total_shares * (1.0 - t / num_steps)
        trajectory.append(shares_at_t)
    return np.array(trajectory)
