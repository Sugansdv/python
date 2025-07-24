class InsufficientFundsError(Exception):
    pass

def atm_simulator():
    balance = 1000.0  # Initial balance

    while True:
        print("\n=== ATM Menu ===")
        print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Select option: ")

        try:
            if choice == '1':
                print(f" Current Balance: ₹{balance:.2f}")

            elif choice == '2':
                try:
                    amount = float(input("Enter deposit amount: "))
                    assert amount > 0, " Amount must be positive."
                    balance += amount
                    print(f" Deposited ₹{amount:.2f}")
                except (ValueError, AssertionError) as e:
                    print(e)

            elif choice == '3':
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    assert amount > 0, " Amount must be positive."
                    if amount > balance:
                        raise InsufficientFundsError(" Insufficient funds.")
                    balance -= amount
                    print(f" Withdrawn ₹{amount:.2f}")
                except (ValueError, AssertionError, InsufficientFundsError) as e:
                    print(e)

            elif choice == '4':
                print(" Thank you for using our ATM!")
                break
            else:
                print(" Invalid choice.")

        except Exception as e:
            print(" Unexpected error:", e)

if __name__ == "__main__":
    atm_simulator()
