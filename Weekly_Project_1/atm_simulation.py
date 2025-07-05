# ATM Simulation

# Set initial balance as a variable
balance = 1000.0

# Allow 3 operations in a for loop: deposit, withdraw, check balance
for i in range(3):
    print("\n--- ATM Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"₹{amount:.2f} deposited successfully.")
    
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        
# Use condition to check if withdrawal is valid
        if amount <= balance:
            balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")
        else:
            print("Insufficient balance. Withdrawal denied.")
    
    elif choice == "3":
        print(f"Your current balance is: ₹{balance:.2f}")
    
    else:
        print("Invalid choice. Please try again.")

print("\nThank you for using the ATM!")
