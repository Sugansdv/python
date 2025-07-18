from finance.income import add_income
from finance.expense import add_expense
from finance.summary import show_summary

def main():
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                amount = float(input("Enter income amount: ₹"))
                source = input("Enter income source: ")
                add_income(amount, source)
            except ValueError:
                print("Invalid amount.")
        elif choice == '2':
            try:
                amount = float(input("Enter expense amount: ₹"))
                category = input("Enter expense category: ")
                add_expense(amount, category)
            except ValueError:
                print("Invalid amount.")
        elif choice == '3':
            show_summary()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
