import numpy as np
def calculate_return(initial_value, final_value):
    if initial_value ==0:
        raise ValueError("Initial value cannot be zero.")
    return (final_value - initial_value)/initial_value 
def daily_return(prices):
    if len(prices) <2:
        raise ValueError("At least two prices are required to calculate daily return.")
    returns =[]
    for i in range(1, len(prices)):
        daily_returns = calculate_return(prices[i-1], prices[i])
        returns.append(daily_returns)
    return returns
def volatility(returns):
    if len(returns) < 2:
        raise ValueError("At least two returns are required.")
    return np.std(returns, ddof=1)
def annualized_volatility(returns):
    daily_volatility = volatility(returns)
    return daily_volatility * np.sqrt(252) 
def max_drawdown(prices):
    peak = prices[0]
    max_drawdown = 0
    for price in prices:
        if price > peak:
            peak = price
        drawdown = (price- peak) / peak * 100
        if drawdown < max_drawdown:
            max_drawdown = drawdown
    return max_drawdown
def sharpe_ratio(returns,risk_free_rate=0):
        result = (np.mean(returns) - risk_free_rate) / volatility(returns)
        return result