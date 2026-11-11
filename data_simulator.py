import numpy as np
import pandas as pd

def generate_lob_data(num_ticks=1000, initial_price=100.0, seed=42):
    np.random.seed(seed)
    returns = np.random.normal(loc=0.0001, scale=0.001, size=num_ticks)
    mid_prices = initial_price * np.exp(np.cumsum(returns))
    half_spreads = np.random.uniform(0.01, 0.05, size=num_ticks)
    bids = mid_prices - half_spreads
    asks = mid_prices + half_spreads
    df = pd.DataFrame({'mid_price': mid_prices, 'bid_price': bids, 'ask_price': asks})
    return df
