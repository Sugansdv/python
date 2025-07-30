import csv
import os
from tracker.expense import Expense
from tracker.validator import validate_input

class ExpenseManager:
    def __init__(self, filepath="data/expenses.csv"):
        self.filepath = filepath
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        self.expenses.append(Expense(row["amount"], row["category"], row["date"]))
                    except:
                        continue

    def save_expenses(self):
        with open(self.filepath, "w", newline="") as file:
            fieldnames = ["amount", "category", "date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow(expense.to_dict())

    @validate_input
    def add_expense(self, amount, category, date):
        self.expenses.append(Expense(amount, category, date))
