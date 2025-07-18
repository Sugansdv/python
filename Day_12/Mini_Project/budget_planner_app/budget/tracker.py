import csv
from datetime import datetime

EXPENSE_FILE = "budget/expenses.csv"

def add_expense(category, amount, description=""):
    date = datetime.now().strftime("%Y-%m-%d")
    with open(EXPENSE_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, description])

def get_expenses_for_month(month):
    expenses = []
    try:
        with open(EXPENSE_FILE, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0].startswith(month):
                    expenses.append(row)
    except FileNotFoundError:
        pass
    return expenses
