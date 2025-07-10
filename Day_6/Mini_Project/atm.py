#5. ATM Simulator
# • Validate PIN using a function
def validate_pin(input_pin):
    return input_pin == "1234"

def atm():
    balance = 1000
    pin = input("Enter your PIN: ")

    if not validate_pin(pin):
        print("Invalid PIN")
        return
    else:
        print("PIN validated successfully.")

    # • Nested functions for deposit, withdrawal
    def deposit():
        nonlocal balance
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposited ₹{amount}. Current balance: ₹{balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw():
        nonlocal balance
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"Withdrew ₹{amount}. Current balance: ₹{balance}")
        else:
            print("Insufficient balance or invalid amount.")

    # • Use pass in change_pin() function placeholder
    def change_pin():
        pass  # Function to be implemented later

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            deposit()
        elif choice == '2':
            withdraw()
        elif choice == '3':
            break
        else:
            print("Invalid option")

    # • Print final balance
    print(f"Final balance: ₹{balance}")

atm()
