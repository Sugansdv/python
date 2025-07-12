# 11. Simple Banking System
# Concepts: while, list (transactions), functions.
# • Options: deposit, withdraw, check balance.
# • Store transactions as list of strings.
# • Print transaction history.

balance = 0
transactions = []

def deposit():
    global balance
    amount = input("Enter amount to deposit: ")
    if amount.isdigit() and int(amount) > 0:
        amount = int(amount)
        balance += amount
        transactions.append(f"Deposited ₹{amount}")
    else:
        print("Invalid amount.\n")

def withdraw():
    global balance
    amount = input("Enter amount to withdraw: ")
    if amount.isdigit() and int(amount) > 0:
        amount = int(amount)
        if amount <= balance:
            balance -= amount
            transactions.append(f"Withdrew ₹{amount}")
        else:
            print("Insufficient balance.\n")
    else:
        print("Invalid amount.\n")

def check_balance():
    print(f"Current Balance: ₹{balance}")

def show_transactions():
    print("\n--- Transaction History ---")
    for t in transactions:
        print(t)
    print()

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        check_balance()
    elif choice == "4":
        show_transactions()
    elif choice == "5":
        break
    else:
        print("Invalid option.\n")
