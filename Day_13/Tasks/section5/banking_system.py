class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Account:
    def __init__(self, acc_number, customer):
        self.acc_number = acc_number
        self.customer = customer
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: {amount}. New Balance: {self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawn: {amount}. Remaining Balance: {self.balance}"
        return "Insufficient balance!"


class Transaction:
    def __init__(self, account):
        self.account = account
        self.history = []

    def perform(self, type_, amount):
        if type_ == 'deposit':
            result = self.account.deposit(amount)
        elif type_ == 'withdraw':
            result = self.account.withdraw(amount)
        else:
            result = "Invalid transaction type!"
        self.history.append((type_, amount, result))
        print(result)

# Example
cust = Customer("Alice", "alice@example.com")
acc = Account("ACC123", cust)
trans = Transaction(acc)
trans.perform("deposit", 5000)
trans.perform("withdraw", 2000)
trans.perform("withdraw", 4000)
