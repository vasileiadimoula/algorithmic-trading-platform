import unittest
import numpy as np
from portfolio import portfolio_return, portfolio_volatility, portfolio_sharpe_ratio
class TestPortfolio(unittest.TestCase):
    def test_portfolio_return(self):
        returns = [10,5,-2]
        weights = [0.5, 0.3, 0.2]
        result = portfolio_return(returns , weights)
        expected = 10*0.5 + 5*0.3 + (-2)*0.2
        self.assertAlmostEqual(result, expected)
    def test_invalid_length(self):
        returns = [10, 5, -2]
        weights = [0.5, 0.5]
        with self.assertRaises(ValueError):
           portfolio_return(returns, weights)
    def test_invalid_weights_sum(self):
        returns = [10, 5, -2]
        weights = [0.5, 0.3, 0.3]
        with self.assertRaises(ValueError):
            portfolio_return(returns, weights)
    def test_portfolio_volatility(self):
       weights = [0.6, 0.4]
       covariance_matrix = np.array([
          [0.04, 0.01],
          [0.01, 0.09]
       ])
       result = portfolio_volatility(weights, covariance_matrix)
       expected = np.sqrt(0.6*(0.028) + 0.4*(0.042))
       self.assertAlmostEqual(result, expected)
    def test_portfolio_sharpe_ratio(self):
        returns = [0.1, 0.05]
        weights = [0.6, 0.4]
        covariance_matrix = np.array([
            [0.04, 0.01],
            [0.01, 0.09]
        ])
        risk_free_rate = 0.02
        result = portfolio_sharpe_ratio(
            returns, weights,
            covariance_matrix,
            risk_free_rate)
        expected_return = 0.10*0.6 + 0.05*0.4
        expected_volatility = np.sqrt(0.0336)
        expected_sharpe = (expected_return - risk_free_rate) / expected_volatility
        self.assertAlmostEqual(result, expected_sharpe)
if __name__ == '__main__':
    unittest.main()