import yfinance as yf
from strategies import  crossover_signal
def get_stock_data(ticker, period="1y"):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data
data = get_stock_data("AAPL")
prices = data["Close"].tolist()
signal = crossover_signal(prices, 20, 50)
print("Crossover signal:", signal)
