def deposit(users, username):
    try:
        amt = float(input("Enter deposit amount: "))
        if amt <= 0:
            print("Amount must be positive.")
            return
        users[username]["balance"] += amt
        users[username]["transactions"].append(("deposit", amt))
        print(f"Deposited ₹{amt:.2f}. New balance: ₹{users[username]['balance']:.2f}")
    except ValueError:
        print("Invalid amount.")

def withdraw(users, username):
    try:
        amt = float(input("Enter withdrawal amount: "))
        if amt <= 0:
            print("Amount must be positive.")
            return
        if users[username]["balance"] - amt < 100:
            print("Insufficient balance. Maintain minimum ₹100.")
            return
        users[username]["balance"] -= amt
        users[username]["transactions"].append(("withdraw", amt))
        print(f"Withdrew ₹{amt:.2f}. New balance: ₹{users[username]['balance']:.2f}")
    except ValueError:
        print("Invalid amount.")

def view_statement(users, username):
    print(f" Statement for {username}:")
    for txn in users[username]["transactions"]:
        print(f" - {txn[0].capitalize()}: ₹{txn[1]:.2f}")
    print(f" Current Balance: ₹{users[username]['balance']:.2f}")

def get_transaction_types(users, username):
    txns = users[username]["transactions"]
    types = {txn[0] for txn in txns}
    print("Transaction Types Used:", ", ".join(types) if types else "None yet.")
