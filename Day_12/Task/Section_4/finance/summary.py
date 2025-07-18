from tax import calculate_tax
from profit import calculate_profit
from loss import calculate_loss

revenue = 10000
cost = 8000

print("Profit:", calculate_profit(revenue, cost))
print("Tax:", calculate_tax(revenue))
print("Loss:", calculate_loss(cost, revenue))
