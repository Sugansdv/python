from datetime import datetime

class Expense:
    def __init__(self, amount, category, date):
        self.amount = float(amount)
        self.category = category
        self.date = datetime.strptime(date, "%Y-%m-%d")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date.strftime("%Y-%m-%d")
        }

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')} | ₹{self.amount:.2f} | {self.category}"
