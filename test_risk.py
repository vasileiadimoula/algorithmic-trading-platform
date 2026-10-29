import unittest
from risk import (
    calculate_return,
    daily_return,
    sharpe_ratio,
    volatility,
    annualized_volatility,
    max_drawdown
)
class TestRisk(unittest.TestCase):
    def test_calculate_return(self):
        result = calculate_return(100, 110)
        self.assertAlmostEqual(result, 0.10)
    def test_daily_return(self):
        result = daily_return([100, 110, 121])
        self.assertEqual(result, [0.1, 0.1])
    def test_volatility(self):
        returns = [1, 2, 3, 4]
        result = volatility(returns)
        expected = 1.2909944487358056
        self.assertAlmostEqual(result, expected)
    def test_annualized_volatility(self):
        returns = [1,2,3,4]
        result = annualized_volatility(returns)
        expected = 1.2909944487358056 * (252 ** 0.5)
        self.assertAlmostEqual(result, expected)
    def test_max_drawdown(self):
        result = max_drawdown([100,120,90,110])
        self.assertAlmostEqual(result, -25.0)
    def test_sharpe_ratio(self):
        returns =[1, 2, 3, 4]
        result = sharpe_ratio(returns)
        expected =  2.5 / 1.2909944487358056
        self.assertAlmostEqual(result, expected)
if __name__ == '__main__':
    unittest.main()