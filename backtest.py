import matplotlib.pyplot as plt
from strategies import crossover_signal
from risk import (
    daily_return,
    annualized_volatility,
    max_drawdown,
    sharpe_ratio
)
def backtest(prices, short_window, long_window):
    signals = []
    for i in range(long_window + 1, len(prices) + 1):
        historical_prices = prices[:i]
        signal = crossover_signal(
            historical_prices,
            short_window,
            long_window
        )
        signals.append(signal)
    return signals
def simulate_trading(
    prices,
    signals,
    long_window,
    initial_cash=10000
):
    cash = initial_cash
    shares = 0
    signal_prices = prices[long_window:]
    for signal, price in zip(signals, signal_prices):
        if signal == "BUY" and shares == 0:
            shares = cash / price
            cash = 0
        elif signal == "SELL" and shares > 0:
            cash = shares * price
            shares = 0
    final_value = cash + shares * prices[-1]
    total_return = (
        (final_value - initial_cash)
        / initial_cash
    ) * 100
    return final_value, total_return
if __name__ == "__main__":
    from market_data import get_stock_data
    data = get_stock_data("AAPL", period="1y")
    prices = data["Close"].tolist()
    short_window = 20
    long_window = 50
    signals = backtest(
        prices,
        short_window,
        long_window
    )
    buy_count = 0
    sell_count = 0
    for signal in signals:
        if signal == "BUY":
            buy_count += 1
        elif signal == "SELL":
            sell_count += 1
    print("BUY signals:", buy_count)
    print("SELL signals:", sell_count)
    initial_cash = 10000
    cash = initial_cash
    shares = 0
    signal_prices = prices[long_window:]
    for signal, price in zip(signals, signal_prices):
        if signal == "BUY" and shares == 0:
            shares = cash / price
            cash = 0
        elif signal == "SELL" and shares > 0:
            cash = shares * price
            shares = 0
    final_value = cash + shares * prices[-1]
    total_return = (
        (final_value - initial_cash)
        / initial_cash
    ) * 100
    buy_hold_return = (
        (prices[-1] - prices[0])
        / prices[0]
    ) * 100
    returns = daily_return(prices)
    annual_vol = annualized_volatility(returns)
    drawdown = max_drawdown(prices)
    sharpe = sharpe_ratio(returns)
    print("\n--- BACKTEST RESULTS ---")
    print(f"Initial capital: ${initial_cash:.2f}")
    print(f"Final value: ${final_value:.2f}")
    print(f"Strategy return: {total_return:.2f}%")
    print(f"Buy & Hold return: {buy_hold_return:.2f}%")
    print(f"Annualized volatility: {annual_vol * 100:.2f}%")
    print(f"Maximum drawdown: {drawdown:.2f}%")
    print(f"Sharpe ratio: {sharpe:.2f}")
    data["MA20"] = data["Close"].rolling(window=short_window).mean()
    data["MA50"] = data["Close"].rolling(window=long_window).mean()
    plt.figure(figsize=(12, 6))
    plt.plot(
       data.index,
       data["Close"],
       label="AAPL Close"
    )
    plt.plot(
       data.index,
       data["MA20"],
       label="MA20"
    )
    plt.plot(
       data.index,
       data["MA50"],
       label="MA50"
    )
    signal_dates = data.index[long_window:]
    for date, signal in zip(signal_dates, signals):
       price = data.loc[date, "Close"]
       if signal == "BUY":
         plt.scatter(
            date,
            price,
            marker="^",
            s=120,
            label="_nolegend_"
         )
       elif signal == "SELL":
          plt.scatter(
            date,
            price,
            marker="v",
            s=120,
            label="_nolegend_"
          )
    plt.title("AAPL Moving Average Crossover Strategy")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.grid(True)
    plt.show()