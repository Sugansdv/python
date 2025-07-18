from budget import planner, tracker, report
from datetime import datetime

def main():
    while True:
        print("\n--- Budget Planning App ---")
        print("1. Set Monthly Budget")
        print("2. Add Expense")
        print("3. Generate Monthly Report")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            month = input("Enter month (YYYY-MM): ")
            amount = float(input("Enter budget amount: "))
            planner.set_budget(month, amount)
            print("Budget set successfully.")
        elif choice == '2':
            category = input("Enter category (e.g. Food, Rent): ")
            amount = float(input("Enter amount: "))
            desc = input("Enter description (optional): ")
            tracker.add_expense(category, amount, desc)
            print("Expense added.")
        elif choice == '3':
            month = input("Enter month (YYYY-MM): ")
            report.generate_monthly_report(month)
        else:
            break

if __name__ == "__main__":
    main()
