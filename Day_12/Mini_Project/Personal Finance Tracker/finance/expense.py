from datetime import datetime
from utils.file_handler import load_data, save_data

EXPENSE_FILE = 'data/expense.json'

def add_expense(amount, category):
    data = load_data(EXPENSE_FILE)
    expense_entry = {
        "amount": amount,
        "category": category,
        "date": datetime.now().isoformat()
    }
    data.append(expense_entry)
    save_data(EXPENSE_FILE, data)
    print("Expense added successfully!")

def get_total_expense():
    data = load_data(EXPENSE_FILE)
    return sum(item["amount"] for item in data)
