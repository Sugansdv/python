
print("=======================================")
print("             Simple ATM Simulation              ")
print("=======================================\n")

# Input: initial balance
balance = float(input("Enter initial account balance: ₹"))

# Choose operation
print("\nSelect transaction type:")
print("1. Deposit")
print("2. Withdraw")
choice = input("Enter 1 or 2: ")

# Deposit operation
if choice == "1":
    deposit = float(input("Enter amount to deposit: ₹"))
    balance += deposit  # Assignment operator +=
    print(f"\n ₹{deposit} deposited successfully.")
    print(f" Updated Balance: ₹{balance}")

# Withdraw operation
elif choice == "2":
    withdraw = float(input("Enter amount to withdraw: ₹"))
    if withdraw <= balance:  # Comparison operator
        balance -= withdraw  # Assignment operator -=
        print(f"\n ₹{withdraw} withdrawn successfully.")
        print(f" Updated Balance: ₹{balance}")
    else:
        print("\n Insufficient balance for this withdrawal.")

# Invalid option
else:
    print("\n Invalid transaction type selected.")

# Final balance shown using f-string
print("\n Final Account Balance:", f"₹{balance}")
print("=======================================")
