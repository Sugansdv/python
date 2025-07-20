from auth.auth import login
from bank.account import deposit, withdraw, view_statement, get_transaction_types

def main():
    print(" Welcome to Simple Banking App")
    users = {
        "user1": {"balance": 1000.0, "transactions": []},
        "user2": {"balance": 500.0, "transactions": []}
    }

    username = login(users)
    if not username:
        return

    while True:
        print("\n Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Statement")
        print("4. Transaction Types")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            deposit(users, username)
        elif choice == "2":
            withdraw(users, username)
        elif choice == "3":
            view_statement(users, username)
        elif choice == "4":
            get_transaction_types(users, username)
        elif choice == "5":
            print("Exiting. Thank you!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
