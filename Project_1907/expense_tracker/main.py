from tracker.expense_ops import (
    add_expense, view_expenses, summarize_by_category, monthly_summary, list_categories
)
from tracker.utils.validator import validate_date, validate_amount

def get_input(prompt):
    return input(prompt).strip()

def main():
    expenses = []

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Summary by Category")
        print("4. Monthly Summary")
        print("5. List Categories")
        print("6. Exit")

        choice = get_input("Choose (1-6): ")

        if choice == "1":
            date = get_input("Date (YYYY-MM-DD): ")
            if not validate_date(date):
                print("Invalid date format.")
                continue
            category = get_input("Category: ")
            amount_str = get_input("Amount: ")
            if not validate_amount(amount_str):
                print("Invalid amount.")
                continue
            amount = float(amount_str)
            add_expense(expenses, date, category, amount)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            summarize_by_category(expenses)

        elif choice == "4":
            monthly_summary(expenses)

        elif choice == "5":
            list_categories(expenses)

        elif choice == "6":
            print("Exiting Expense Tracker.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
