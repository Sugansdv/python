import csv
from datetime import datetime

BUDGET_FILE = "budget/budget.csv"

def set_budget(month, amount):
    with open(BUDGET_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([month, amount])

def get_budget(month):
    try:
        with open(BUDGET_FILE, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == month:
                    return float(row[1])
    except FileNotFoundError:
        pass
    return 0.0
