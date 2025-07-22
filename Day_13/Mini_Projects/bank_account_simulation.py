class Account:
    def __init__(self, account_no, holder_name, initial_balance=0):
        self.account_no = account_no
        self.holder_name = holder_name
        self.__balance = initial_balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount} into {self.holder_name}'s account.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount} from {self.holder_name}'s account.")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

    def transfer(self, target_account, amount):
        if 0 < amount <= self.__balance:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"Transferred ₹{amount} to {target_account.holder_name}.")
        else:
            print("Transfer failed: Check balance or amount.")

    def __str__(self):
        return f"Account[{self.account_no}] - {self.holder_name}"


class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount > 20000:
            print("Savings Account limit: Cannot withdraw more than ₹20,000 at once.")
        else:
            super().withdraw(amount)


class CurrentAccount(Account):
    def withdraw(self, amount):
        if amount > 100000:
            print("Current Account limit: Cannot withdraw more than ₹1,00,000 at once.")
        else:
            super().withdraw(amount)


class Transaction:
    def __init__(self, txn_type, amount, source, target=None):
        self.txn_type = txn_type
        self.amount = amount
        self.source = source
        self.target = target

    def execute(self):
        if self.txn_type == "deposit":
            self.source.deposit(self.amount)
        elif self.txn_type == "withdraw":
            self.source.withdraw(self.amount)
        elif self.txn_type == "transfer" and self.target:
            self.source.transfer(self.target, self.amount)
        else:
            print("Invalid transaction.")


# ----------- Demo ----------
if __name__ == "__main__":
    # Create accounts
    acc1 = SavingsAccount("SA001", "Dharun", 30000)
    acc2 = CurrentAccount("CA001", "Vishwa", 150000)

    print(acc1)
    print(acc2)

    # Transactions
    txn1 = Transaction("deposit", 5000, acc1)
    txn2 = Transaction("withdraw", 22000, acc1)  
    txn3 = Transaction("withdraw", 18000, acc1)
    txn4 = Transaction("transfer", 10000, acc2, acc1)

    for txn in [txn1, txn2, txn3, txn4]:
        txn.execute()

    # Final balances
    print(f"\n{acc1.holder_name}'s Balance: ₹{acc1.get_balance()}")
    print(f"{acc2.holder_name}'s Balance: ₹{acc2.get_balance()}")
