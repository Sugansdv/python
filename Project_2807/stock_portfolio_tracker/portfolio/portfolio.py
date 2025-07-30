import json
import os
import yfinance as yf
from .cache import cache

class Portfolio:
    def __init__(self, file_path="data/portfolio.json"):
        self.file_path = file_path
        self.stocks = self.load_portfolio()

    def add_stock(self, symbol, shares):
        self.stocks[symbol.upper()] = self.stocks.get(symbol.upper(), 0) + shares
        self.save_portfolio()

    def remove_stock(self, symbol):
        if symbol.upper() in self.stocks:
            del self.stocks[symbol.upper()]
            self.save_portfolio()

    def save_portfolio(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, 'w') as f:
            json.dump(self.stocks, f)

    def load_portfolio(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                return json.load(f)
        return {}

    @cache
    def get_price(self, symbol):
        try:
            stock = yf.Ticker(symbol)
            return stock.history(period="1d")['Close'][-1]
        except Exception as e:
            print(f" Failed to fetch price for {symbol}: {e}")
            return 0

    def get_total_value(self):
        total = 0
        for symbol, shares in self.stocks.items():
            price = self.get_price(symbol)
            value = price * shares
            print(f"{symbol}: {shares} shares × ₹{price:.2f} = ₹{value:.2f}")
            total += value
        return total
