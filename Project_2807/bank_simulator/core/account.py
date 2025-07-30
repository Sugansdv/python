import json
import os
from core.decorators import audit

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []
        self.load_account()

    def save_account(self):
        with open(f"data/accounts.json", "w") as f:
            json.dump({self.name: {"balance": self.balance, "transactions": self.transactions}}, f, indent=2)

    def load_account(self):
        if os.path.exists("data/accounts.json"):
            with open("data/accounts.json", "r") as f:
                data = json.load(f)
                if self.name in data:
                    self.balance = data[self.name]["balance"]
                    self.transactions = data[self.name]["transactions"]

    @audit
    def deposit(self, amount):
        self.balance += amount
        self.save_account()
        return f"${amount} deposited."

    @audit
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        self.save_account()
        return f"${amount} withdrawn."

    @audit
    def transfer(self, amount, target_account):
        if amount > self.balance:
            raise ValueError("Insufficient balance for transfer.")
        self.withdraw(amount)
        target_account.deposit(amount)
        self.save_account()
        target_account.save_account()
        return f"${amount} transferred to {target_account.name}."

    def apply_interest(self):
        if self.balance > 1000:
            interest = self.balance * 0.02
            self.deposit(interest)
            return f"Interest of ${interest:.2f} applied."

    def display_transactions(self):
        for t in self.transactions:
            print(f"{t['timestamp']} - {t['action']} - ${t['amount']}")

    def filter_transactions(self, type_):
        return (t for t in self.transactions if t["action"] == type_)
