import unittest
from strategies import moving_average, moving_average_signal, crossover_signal
class TestStrategies(unittest.TestCase):
    def test_moving_average(self):
        prices = [100, 102, 104, 106, 110]
        result = moving_average(prices, 3)
        expected = (104 + 106 + 110) / 3
        self.assertAlmostEqual(result, expected)
    def test_buy_signal(self):
        prices = [100, 100, 100, 110, 120]
        result = moving_average_signal(prices, 2, 5)
        self.assertEqual(result, "BUY")
    def test_sell_signal(self):
        prices = [100, 120, 130, 90, 100]
        result = moving_average_signal(prices, 2, 5)
        self.assertEqual(result, "SELL")
    def test_hold_signal(self):
        prices = [100, 100, 100, 100, 100]
        result = moving_average_signal(prices, 2, 5)
        self.assertEqual(result, "HOLD")
    def test_buy_crossover(self):
       prices = [120, 130, 140, 80, 90, 300]
       result = crossover_signal(prices, 2, 5)
       self.assertEqual(result, "BUY")
    def test_sell_crossover(self):
       prices = [120, 130, 140, 170, 180, 60]
       result = crossover_signal(prices, 2, 5)
       self.assertEqual(result, "SELL")