from modules.cred_ops import add_account, update_account, delete_account, search_accounts
from modules.utils import generate_password

accounts = {}

def main():
    print(" Welcome to Password Manager")

    while True:
        print("\nMenu:")
        print("1. Add Account")
        print("2. Update Account")
        print("3. Delete Account")
        print("4. Search Account")
        print("5. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_account(accounts)
        elif choice == "2":
            update_account(accounts)
        elif choice == "3":
            delete_account(accounts)
        elif choice == "4":
            search_accounts(accounts)
        elif choice == "5":
            print("Exiting Password Manager.")
            break
        else:
            print(" Invalid option.")
            
if __name__ == "__main__":
    main()
