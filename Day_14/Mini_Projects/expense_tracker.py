import csv
import os
from datetime import datetime
from collections import defaultdict

EXPENSE_DIR = "expenses"
os.makedirs(EXPENSE_DIR, exist_ok=True)

def get_monthly_file(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    filename = f"expenses_{date_obj.strftime('%Y-%m')}.csv"
    return os.path.join(EXPENSE_DIR, filename)

def add_expense():
    category = input("Enter category (e.g. Food, Travel, Bills): ").strip()
    amount = input("Enter amount: ").strip()
    date = input("Enter date (YYYY-MM-DD): ").strip()

    try:
        float(amount)
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(" Invalid amount or date format.")
        return

    file_path = get_monthly_file(date)
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Date", "Category", "Amount"])
        writer.writerow([date, category, amount])

    print(" Expense added successfully.")

def summarize_expenses(month):
    file_path = os.path.join(EXPENSE_DIR, f"expenses_{month}.csv")
    if not os.path.exists(file_path):
        print(f" No data for month: {month}")
        return

    total = 0
    by_category = defaultdict(float)

    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            amt = float(row["Amount"])
            total += amt
            by_category[row["Category"]] += amt

    print(f"\n Summary for {month}")
    print("-" * 30)
    print(f"Total Expenses: ₹{total:.2f}")
    print("By Category:")
    for cat, amt in by_category.items():
        print(f"  {cat}: ₹{amt:.2f}")
    print("-" * 30)

def main():
    while True:
        print("\n Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            month = input("Enter month (YYYY-MM): ").strip()
            summarize_expenses(month)
        elif choice == "3":
            print(" Exiting Expense Tracker.")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
