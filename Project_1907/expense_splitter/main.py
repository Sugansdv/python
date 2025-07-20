from modules.expense_ops import add_expense
from modules.balance_ops import settle_balances, show_summary

expenses = []
balances = {}

def main():
    print(" Expense Splitter for Roommates")

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. Show Balances")
        print("3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_expense(expenses, balances)
        elif choice == "2":
            show_summary(balances)
            settle_balances(balances)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
