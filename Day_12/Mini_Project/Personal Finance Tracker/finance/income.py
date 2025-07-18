from datetime import datetime
from utils.file_handler import load_data, save_data

INCOME_FILE = 'data/income.json'

def add_income(amount, source):
    data = load_data(INCOME_FILE)
    income_entry = {
        "amount": amount,
        "source": source,
        "date": datetime.now().isoformat()
    }
    data.append(income_entry)
    save_data(INCOME_FILE, data)
    print("Income added successfully!")

def get_total_income():
    data = load_data(INCOME_FILE)
    return sum(item["amount"] for item in data)
