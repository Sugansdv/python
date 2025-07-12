# ATM Machine Simulation
correct_pin = "1234"
balance = 5000
transaction_history = [] 

def login():
    attempts = 3
    while attempts > 0:  
        pin = input("Enter your ATM PIN: ")
        if pin == correct_pin:
            print("Login successful!\n")
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts left: {attempts}")
    print("Too many incorrect attempts. Card blocked.\n")
    return False

def show_menu():  
    print("\n------ ATM Menu ------")
    print("1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

def balance_inquiry():
    print(f"Your current balance is ₹{balance}")

def deposit():
    global balance
    amount = input("Enter amount to deposit: ")
    if amount.isdigit() and int(amount) > 0: 
        amount = int(amount)
        balance += amount
        transaction_history.append(f"Deposited ₹{amount}") 
        print(f"₹{amount} deposited successfully.")
    else:
        print("Invalid amount.")

def withdraw():
    global balance
    amount = input("Enter amount to withdraw: ")
    if amount.isdigit() and int(amount) > 0:  
        amount = int(amount)
        if amount <= balance:
            balance -= amount
            transaction_history.append(f"Withdrew ₹{amount}")  
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")
    else:
        print("Invalid amount.")

def show_transactions():
    if transaction_history:
        print("\n--- Transaction History ---")
        for t in transaction_history:
            print(t)
    else:
        print("No transactions yet.")

if login():
    while True:  
        show_menu()
        choice = input("Select an option (1-5): ")
        if choice == "1":
            balance_inquiry()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            show_transactions()
        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
