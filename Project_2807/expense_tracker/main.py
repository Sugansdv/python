from tracker.manager import ExpenseManager
from tracker.utils import date_range_generator, unique_categories

def print_menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View by Category")
    print("3. View by Month")
    print("4. Show Expenses > Amount")
    print("5. View by Date Range")
    print("6. Show Unique Categories")
    print("7. Exit")

def main():
    manager = ExpenseManager()

    while True:
        print_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            amt = input("Amount: ")
            cat = input("Category: ")
            date = input("Date (YYYY-MM-DD): ")
            manager.add_expense(amount=amt, category=cat, date=date)

        elif choice == "2":
            cat = input("Enter category: ")
            for e in manager.expenses:
                if e.category.lower() == cat.lower():
                    print(e)

        elif choice == "3":
            month = input("Enter month (YYYY-MM): ")
            for e in manager.expenses:
                if e.date.strftime("%Y-%m") == month:
                    print(e)

        elif choice == "4":
            limit = float(input("Enter minimum amount: "))
            for e in manager.expenses:
                if e.amount > limit:
                    print(e)

        elif choice == "5":
            start = input("Start date (YYYY-MM-DD): ")
            end = input("End date (YYYY-MM-DD): ")
            for e in date_range_generator(manager.expenses, start, end):
                print(e)

        elif choice == "6":
            print("Categories:", unique_categories(manager.expenses))

        elif choice == "7":
            manager.save_expenses()
            print("Expenses saved. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
