import unittest
from backtest import simulate_trading
class TestBacktest(unittest.TestCase):
    def test_simulate_trading(self):
        prices = [100, 100, 100, 100, 100, 120]
        signals = ["BUY", "HOLD", "HOLD"]
        final_value, total_return = simulate_trading(
            prices,
            signals,
            long_window=3,
            initial_cash=10000
        )
        self.assertAlmostEqual(final_value, 12000)
        self.assertAlmostEqual(total_return, 20)
if __name__ == "__main__":
    unittest.main()