# 6. Expense Tracker with Categories
# Concepts: list, string formatting, functions, while.
# • User enters expenses (amount + category).
# • Store in list of dicts or nested lists.
# • Show total, category-wise total using functions.
# • Menu-driven loop.

expenses = []

def add_expense():
    category = input("Enter category (e.g., Food, Travel): ")
    amount = input("Enter amount: ")
    if amount.replace('.', '', 1).isdigit():
        expenses.append({"category": category, "amount": float(amount)})

def show_all_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. ₹{exp['amount']:.2f} - {exp['category']}")
    print()

def show_totals():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expenses: ₹{total:.2f}")
    categories = {}
    for exp in expenses:
        cat = exp["category"]
        categories[cat] = categories.get(cat, 0) + exp["amount"]
    print("--- Category-wise Totals ---")
    for cat, amt in categories.items():
        print(f"{cat}: ₹{amt:.2f}")
    print()

while True:
    print("1. Add Expense")
    print("2. Show All Expenses")
    print("3. Show Totals")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_all_expenses()
    elif choice == "3":
        show_totals()
    elif choice == "4":
        break
    else:
        print("Invalid choice.\n")
