# 12. Bank Account Simulation
# Description: Simulate basic banking operations.
# Requirements:
# - Structure: {account_number: {"name": ..., "balance": ...}}
# - Deposit, withdraw operations
# - Use get() to avoid account not found error
# - Flag low-balance accounts (<1000) using comprehension

accounts = {
    1001: {"name": "Alice", "balance": 2500},
    1002: {"name": "Bob", "balance": 800},
    1003: {"name": "Charlie", "balance": 1200}
}

def deposit(account_number, amount):
    account = accounts.get(account_number)
    if account:
        account["balance"] += amount
        print(f"Deposited ₹{amount} to {account['name']}'s account.")
    else:
        print("Account not found.")

def withdraw(account_number, amount):
    account = accounts.get(account_number)
    if account:
        if account["balance"] >= amount:
            account["balance"] -= amount
            print(f"Withdrew ₹{amount} from {account['name']}'s account.")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")

def flag_low_balance(threshold=1000):
    low_balance_accounts = {acc: data for acc, data in accounts.items() if data["balance"] < threshold}
    print(f"\nAccounts with balance < ₹{threshold}:")
    for acc, data in low_balance_accounts.items():
        print(f"{acc}: {data['name']} → ₹{data['balance']}")

deposit(1002, 500)
withdraw(1003, 300)
withdraw(1004, 100)  
flag_low_balance()
