import yfinance as yf
import json
import os
from portfolio.utils import cache

class Portfolio:
    def __init__(self):
        self.stocks = {}  # {"AAPL": 10}

    def add_stock(self, symbol, shares):
        symbol = symbol.upper()
        self.stocks[symbol] = self.stocks.get(symbol, 0) + shares

    @cache
    def get_price(self, symbol):
        try:
            stock = yf.Ticker(symbol)
            price = stock.info['regularMarketPrice']
            if price is None:
                raise ValueError("Price not available.")
            return price
        except Exception as e:
            print(f" Error fetching {symbol}: {e}")
            return 0

    def total_value(self):
        total = 0
        for symbol, shares in self.stocks.items():
            price = self.get_price(symbol)
            total += price * shares
        return total

    def save(self, path):
        with open(path, 'w') as f:
            json.dump(self.stocks, f)

    def load(self, path):
        if os.path.exists(path):
            with open(path, 'r') as f:
                self.stocks = json.load(f)
