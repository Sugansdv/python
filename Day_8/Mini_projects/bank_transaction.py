# 20. Bank Transaction Logger
# Description: Track credits and debits.

# Store transactions in a list (+ve = credit, -ve = debit)
transactions = [5000, -1200, 3000, -800, -1000, 2000]

# Display all transactions
print(" All Transactions:")
for t in transactions:
    t_type = "Credit" if t > 0 else "Debit"
    print(f"{t_type}: ₹{abs(t)}")

# Calculate current balance using sum()
balance = sum(transactions)
print(f"\n Current Balance: ₹{balance}")

# Slice to show last 3 transactions
last_three = transactions[-3:]
print("\n Last 3 Transactions:")
for t in last_three:
    t_type = "Credit" if t > 0 else "Debit"
    print(f"{t_type}: ₹{abs(t)}")

# Remove incorrect transaction (e.g., -800 was mistakenly entered)
wrong_txn = -800
if wrong_txn in transactions:
    transactions.remove(wrong_txn)
    print(f"\n Removed incorrect transaction: ₹{abs(wrong_txn)}")

# Recalculate updated balance
updated_balance = sum(transactions)
print(f"\n Updated Balance: ₹{updated_balance}")
