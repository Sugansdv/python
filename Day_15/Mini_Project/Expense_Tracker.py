# Task 16 - Expense Tracker App

class InvalidCategoryError(Exception):
    pass

def expense_tracker():
    categories = ["food", "transport", "utilities", "entertainment"]
    expenses = []
    total = 0

    try:
        while True:
            desc = input("Enter expense description (or 'done' to stop): ")
            if desc.lower() == 'done':
                break

            try:
                amount = float(input("Enter expense amount: "))
            except ValueError:
                print("Invalid amount! Please enter a number.")
                continue

            category = input("Enter category (food, transport, utilities, entertainment): ").lower()
            if category not in categories:
                raise InvalidCategoryError(f"'{category}' is not a valid category!")

            expenses.append((desc, amount, category))
            total += amount

    except InvalidCategoryError as e:
        print("Error:", e)
    finally:
        print("\n--- Expense Summary ---")
        for desc, amount, cat in expenses:
            print(f"{desc} - ₹{amount:.2f} [{cat}]")
        print("Total Spent: ₹", total)

expense_tracker()
