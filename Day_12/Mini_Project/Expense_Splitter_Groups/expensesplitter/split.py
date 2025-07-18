from decimal import Decimal, getcontext
from expensesplitter.helper import validate_decimal

getcontext().prec = 2  # For monetary precision

class ExpenseSplitter:
    def __init__(self, members):
        if not members:
            raise ValueError("No group members provided.")
        self.members = members
        self.expenses = []  # list of tuples: (payer, amount, description)

    def add_expense(self, payer, amount, description=""):
        if payer not in self.members:
            raise ValueError(f"{payer} is not a valid group member.")
        amount = validate_decimal(amount)
        self.expenses.append((payer, amount, description))

    def calculate_balances(self):
        total_expense = sum(exp[1] for exp in self.expenses)
        per_person = total_expense / Decimal(len(self.members))
        paid = {m: Decimal('0.00') for m in self.members}

        for payer, amount, _ in self.expenses:
            paid[payer] += amount

        balances = {m: paid[m] - per_person for m in self.members}
        return balances
