import numpy as np
def portfolio_return(returns, weights):
    if len(returns) != len(weights):
        raise ValueError("Returns and weights must have the same length.")
    if not np.isclose(np.sum(weights), 1):
        raise ValueError("Weights must sum to 1.")
    return np.dot(returns, weights)
def portfolio_volatility(weights, covariance_matrix):
    portfolio_variance = np.dot(
    weights,
    np.dot(covariance_matrix, weights)
    )
    return np.sqrt(portfolio_variance)
def portfolio_sharpe_ratio(
    returns,
    weights,
    covariance_matrix,
    risk_free_rate=0
):
    port_return = portfolio_return(returns, weights)
    port_volatility = portfolio_volatility(weights, covariance_matrix)
    if port_volatility == 0:
        raise ValueError("Portfolio volatility cannot be zero.")
    return(port_return - risk_free_rate) / port_volatility