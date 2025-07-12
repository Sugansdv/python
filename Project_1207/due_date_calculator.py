# 21. Library Due Date Calculator
# Concepts: string formatting, list, functions.
# • Input book name, borrow date.
# • Calculate due date (assume +7 days).
# • Display summary.

from datetime import datetime, timedelta

records = []

def borrow_book():
    book = input("Enter book name: ")
    date_str = input("Enter borrow date (YYYY-MM-DD): ")
    try:
        borrow_date = datetime.strptime(date_str, "%Y-%m-%d")
        due_date = borrow_date + timedelta(days=7)
        records.append([book, borrow_date.date(), due_date.date()])
    except ValueError:
        print("Invalid date format.\n")

def show_summary():
    print("\n--- Borrowed Books Summary ---")
    for rec in records:
        print(f"Book: {rec[0]} | Borrowed: {rec[1]} | Due: {rec[2]}")
    print()

while True:
    print("1. Borrow Book")
    print("2. Show Summary")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        borrow_book()
    elif choice == "2":
        show_summary()
    elif choice == "3":
        break
    else:
        print("Invalid choice.\n")
