# 21. Student class with private attributes and getter/setter
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    def set_name(self, name):
        self.__name = name

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks!")

# 22. BankAccount with private balance
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

# 23. UserProfile with encapsulated email, phone, validation in setters
class UserProfile:
    def __init__(self, email, phone):
        self.__email = email
        self.__phone = phone

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if "@" in email and "." in email:
            self.__email = email
        else:
            print("Invalid email format")

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        if phone.isdigit() and len(phone) == 10:
            self.__phone = phone
        else:
            print("Invalid phone number")

# 24. Employee class with private salary
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Salary must be positive")

# 25. Locker system with private PIN
class Locker:
    def __init__(self, pin):
        self.__pin = pin

    def change_pin(self, old_pin, new_pin):
        if self.__pin == old_pin:
            if len(str(new_pin)) == 4 and str(new_pin).isdigit():
                self.__pin = new_pin
                print("PIN changed successfully.")
            else:
                print("New PIN must be a 4-digit number.")
        else:
            print("Incorrect old PIN!")


# =======================
# Run tasks
# =======================
if __name__ == "__main__":
    print("TASK 21: Student Class with Encapsulation")
    s1 = Student("Alice", 85)
    print("Name:", s1.get_name())
    print("Marks:", s1.get_marks())
    s1.set_marks(92)
    print("Updated Marks:", s1.get_marks())

    print("\nTASK 22: BankAccount Encapsulation")
    acc = BankAccount(1000)
    acc.deposit(500)
    acc.withdraw(300)
    print("Current Balance:", acc.get_balance())

    print("\nTASK 23: UserProfile with Validation")
    user = UserProfile("test@example.com", "9876543210")
    print("Email:", user.get_email())
    print("Phone:", user.get_phone())
    user.set_email("invalid_email")  # should fail
    user.set_phone("12345")         # should fail

    print("\nTASK 24: Employee with Private Salary")
    emp = Employee("Bob", 40000)
    print("Name:", emp.name)
    print("Salary:", emp.get_salary())
    emp.set_salary(45000)
    print("Updated Salary:", emp.get_salary())

    print("\nTASK 25: Locker PIN System")
    locker = Locker(1234)
    locker.change_pin(1111, 5678)  # Incorrect old pin
    locker.change_pin(1234, 56789) # Invalid new pin
    locker.change_pin(1234, 5678)  # Success
