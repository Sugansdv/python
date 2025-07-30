from portfolio.tracker import Portfolio
from portfolio.utils import print_portfolio

portfolio = Portfolio()

# Sample interactions
portfolio.add_stock("AAPL", 10)
portfolio.add_stock("MSFT", 5)

print("\n Current Portfolio:")
print_portfolio(portfolio)

print("\n Total Value: ${:.2f}".format(portfolio.total_value()))

portfolio.save("data/portfolio.json")
