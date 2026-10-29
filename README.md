# Algorithmic Trading Platform
A Python-based quantitative finance project for analyzing market data, generating algorithmic trading signals, backtesting trading strategies, and evaluating portfolio risk and performance.

## Features
- Downloads historical stock market data using Yahoo Finance
- Calculates short-term and long-term moving averages
- Generates BUY, SELL, and HOLD signals
- Detects moving-average crossover events
- Backtests trading strategies on historical market data
- Simulates portfolio performance
- Compares strategy performance with Buy & Hold
- Calculates financial risk metrics
- Visualizes stock prices, moving averages, and trading signals
- Includes automated unit tests

## Trading Strategy
The project implements a Moving Average Crossover strategy.
Two moving averages are calculated:
- Short moving average: 20 trading days
- Long moving average: 50 trading days
A BUY signal is generated when the short moving average crosses above the long moving average.
A SELL signal is generated when the short moving average crosses below the long moving average.

## Risk Analysis
The platform calculates:
- Daily returns
- Annualized volatility
- Maximum drawdown
- Sharpe ratio
These metrics provide information about the risk and historical behavior of the analyzed asset.

## Backtesting
The backtesting engine processes historical prices chronologically to avoid using future information when generating signals.
It simulates trading with an initial portfolio value and reports:
- Initial capital
- Final portfolio value
- Strategy return
- Buy & Hold return
- Number of BUY and SELL signals

## Visualization
The project generates a chart containing:
- Historical stock price
- 20-day moving average
- 50-day moving average
- BUY/SELL crossover markers

## Project Structure
```text
algorithmic-trading-platform/
├── main.py
├── market_data.py
├── strategies.py
├── backtest.py
├── risk.py
├── portfolio.py
├── test_backtest.py
├── test_strategies.py
├── test_risk.py
├── test_portfolio.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation
Clone the repository and install the dependencies:
```bash
pip install -r requirements.txt
```
Run the application:
```bash
python3 main.py
```
Run the test suite:
```bash
python3 -m unittest
```

## Technologies
Python, NumPy, Pandas, Matplotlib, yfinance, unittest

## Purpose
This project was developed as a practical exploration of Python software development, quantitative finance, algorithmic trading concepts, financial mathematics, testing, and modular application design.

## Disclaimer
This project is intended for educational and portfolio purposes only. It does not constitute financial advice or a production trading system.