from collections import defaultdict

def add_expense(expenses, date, category, amount):
    expenses.append((date, category, amount))
    print(f"Expense of {amount} added to category '{category}' on {date}.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    for date, category, amount in expenses:
        print(f"{date} | {category} | Rs. {amount:.2f}")

def summarize_by_category(expenses):
    summary = defaultdict(float)
    for _, category, amount in expenses:
        summary[category] += amount
    print("\nSummary by Category:")
    for cat, total in summary.items():
        print(f"{cat}: Rs. {total:.2f}")

def monthly_summary(expenses):
    summary = defaultdict(float)
    for date, _, amount in expenses:
        month = date[:7]  # YYYY-MM
        summary[month] += amount
    print("\nMonthly Summary:")
    for month, total in sorted(summary.items()):
        print(f"{month}: Rs. {total:.2f}")

def list_categories(expenses):
    categories = set([cat for _, cat, _ in expenses])
    print("Categories used:", ", ".join(sorted(categories)))
