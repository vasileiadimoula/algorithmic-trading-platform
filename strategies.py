import numpy as np
def moving_average(prices, window):
    if window <= 0:
        raise ValueError("Window must be greater than zero.")
    if len(prices) < window:
        raise ValueError("Not enough prices for this window.")
    return np.mean(prices[-window:])
def moving_average_signal(prices, short_window, long_window):
    short_ma = moving_average(prices, short_window)
    long_ma = moving_average(prices, long_window)
    if short_ma > long_ma:
        return "BUY"
    elif short_ma < long_ma:
        return "SELL"
    else:
        return "HOLD"
def crossover_signal(prices, short_window, long_window):
    current_short_ma = moving_average(prices, short_window)
    current_long_ma = moving_average(prices, long_window)
    previous_prices = prices[:-1]
    previous_short_ma = moving_average(previous_prices, short_window)
    previous_long_ma = moving_average(previous_prices, long_window)
    if previous_short_ma <= previous_long_ma and current_short_ma > current_long_ma:
        return "BUY"
    elif previous_short_ma >= previous_long_ma and current_short_ma < current_long_ma:
        return "SELL"
    else:
        return "HOLD"
    
    