from .planner import get_budget
from .tracker import get_expenses_for_month
from math import fsum
from tabulate import tabulate  

def generate_monthly_report(month):
    budget = get_budget(month)
    expenses = get_expenses_for_month(month)
    total_spent = fsum([float(row[2]) for row in expenses]) if expenses else 0

    print("\n===== Monthly Report =====")
    print(f"Month: {month}")
    print(f"Budget: ₹{budget}")
    print(f"Total Spent: ₹{total_spent}")
    print(f"Remaining: ₹{budget - total_spent}\n")

    if expenses:
        table = [[row[0], row[1], row[2], row[3]] for row in expenses]
        headers = ["Date", "Category", "Amount", "Description"]
        print(tabulate(table, headers=headers, tablefmt="grid"))
    else:
        print("No expenses recorded for this month.")
