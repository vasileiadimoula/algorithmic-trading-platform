from backtest import backtest, simulate_trading
from market_data import get_stock_data
from risk import (
    daily_return,
    annualized_volatility,
    max_drawdown,
    sharpe_ratio
)
def main():
    ticker = "AAPL"
    period = "1y"
    short_window = 20
    long_window = 50
    initial_cash = 10000
    print(f"Running trading analysis for {ticker}...")
    data = get_stock_data(ticker, period=period)
    prices = data["Close"].tolist()
    signals = backtest(
        prices,
        short_window,
        long_window
    )
    final_value, strategy_return = simulate_trading(
       prices,
       signals,
       long_window,
       initial_cash
    )
    returns = daily_return(prices)
    annual_vol = annualized_volatility(returns)
    drawdown = max_drawdown(prices)
    sharpe = sharpe_ratio(returns)
    print(f"Data points: {len(prices)}")
    print(f"BUY signals: {signals.count('BUY')}")
    print(f"SELL signals: {signals.count('SELL')}")
    print(f"Annualized volatility: {annual_vol * 100:.2f}%")
    print(f"Maximum drawdown: {drawdown:.2f}%")
    print(f"Sharpe ratio: {sharpe:.2f}")
    print(f"Initial capital: ${initial_cash:.2f}")
    print(f"Final value: ${final_value:.2f}")
    print(f"Strategy return: {strategy_return:.2f}%")
if __name__ == "__main__":
    main()