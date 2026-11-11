import numpy as np

def calculate_roll_spread(price_series):
    price_diff = np.diff(price_series)
    cov = np.cov(price_diff[:-1], price_diff[1:])[0, 1]
    return 2.0 * np.sqrt(-cov) if cov < 0 else 0.0

def calculate_kyles_lambda(price_changes, trade_volumes, trade_signs):
    signed_volume = trade_volumes * trade_signs
    cov = np.cov(price_changes, signed_volume)[0, 1]
    var_vol = np.var(signed_volume)
    return cov / var_vol if var_vol != 0 else 0.0
