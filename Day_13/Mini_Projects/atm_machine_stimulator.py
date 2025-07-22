# ---------------------- Account Class ----------------------
class Account:
    def __init__(self, account_no, name, pin, balance=0):
        self.account_no = account_no
        self.name = name
        self.__pin = pin              # Encapsulated PIN
        self.__balance = balance      # Encapsulated balance

    def validate_pin(self, pin):
        return self.__pin == pin

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            return True
        return False

# ---------------------- Transaction Class ----------------------
class Transaction:
    def __init__(self, account):
        self.account = account

    def balance_enquiry(self):
        return self.account.get_balance()

    def deposit(self, amount):
        if self.account.deposit(amount):
            return f" Deposited ₹{amount}. New Balance: ₹{self.account.get_balance()}"
        else:
            return " Invalid deposit amount."

    def withdraw(self, *args):
        """
        Overloaded Withdraw Method:
        1 arg → amount
        2 args → pin, amount
        """
        if len(args) == 1:
            amount = args[0]
            return self._withdraw_internal(amount)
        elif len(args) == 2:
            pin, amount = args
            if self.account.validate_pin(pin):
                return self._withdraw_internal(amount)
            else:
                return " Invalid PIN."
        else:
            return " Invalid arguments."

    def _withdraw_internal(self, amount):
        if self.account.withdraw(amount):
            return f" Withdrawn ₹{amount}. New Balance: ₹{self.account.get_balance()}"
        else:
            return "Insufficient balance or invalid amount."

# ---------------------- ATM Class ----------------------
class ATM:
    bank_name = "SBI ATM"

    @staticmethod
    def show_bank_info():
        return f" Welcome to {ATM.bank_name}"

# ---------------------- Test the System ----------------------
if __name__ == "__main__":
    print(ATM.show_bank_info())

    acc1 = Account("123456", "Suganya", pin=4321, balance=1000)
    txn = Transaction(acc1)

    print(txn.balance_enquiry())  # Balance check

    print(txn.deposit(500))       # Deposit ₹500

    print(txn.withdraw(200))      # Withdraw ₹200 (no PIN needed)

    print(txn.withdraw(4321, 1000))  # Withdraw with PIN

    print(txn.withdraw(1234, 100))   # Wrong PIN

    print(txn.withdraw(10000))      # Insufficient funds
