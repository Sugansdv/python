import functools

_cache = {}

def cache(func):
    @functools.wraps(func)
    def wrapper(self, symbol):
        if symbol in _cache:
            return _cache[symbol]
        value = func(self, symbol)
        _cache[symbol] = value
        return value
    return wrapper

def print_portfolio(portfolio):
    for symbol, shares in portfolio.stocks.items():
        price = portfolio.get_price(symbol)
        print(f"{symbol}: {shares} shares × ${price:.2f} = ${shares * price:.2f}")
