# 1. Car Class
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ₹{self.price}")


# 2. BankAccount Class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")


# 3. Student Class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


# 4. Circle Class
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


# 5. Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")


# 6. Laptop Class
class Laptop:
    warranty_period = 2  # Class variable

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


# 7. Movie Class
class Movie:
    movie_count = 0

    def __init__(self, title):
        self.title = title
        Movie.movie_count += 1


# 8. Product Class
class Product:
    category = "Electronics"

    def __init__(self, name, price):
        self.name = name
        self.price = price


# 9. Employee Class with __str__
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: ₹{self.salary}"


# 10. Rectangle Class with __eq__
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __eq__(self, other):
        return self.length == other.length and self.width == other.width


# ======================
# Run tasks
# ======================
if __name__ == "__main__":
    print("TASK 1: Car")
    car1 = Car("Toyota", "Innova", 2200000)
    car2 = Car("Hyundai", "Creta", 1500000)
    car1.display()
    car2.display()

    print("\nTASK 2: BankAccount")
    acc = BankAccount()
    acc.deposit(1000)
    acc.withdraw(500)
    acc.check_balance()

    print("\nTASK 3: Student")
    student = Student("John", 16, "10th")
    student.display()

    print("\nTASK 4: Circle")
    c = Circle(5)
    print("Area:", c.area())
    print("Circumference:", c.circumference())

    print("\nTASK 5: Book")
    book = Book("Python Basics", "Alice")
    book.display_info()

    print("\nTASK 6: Laptop")
    l1 = Laptop("Dell", "XPS")
    print(l1.brand, l1.model, "Warranty:", Laptop.warranty_period, "years")

    print("\nTASK 7: Movie")
    m1 = Movie("Inception")
    m2 = Movie("Interstellar")
    print("Total Movies:", Movie.movie_count)

    print("\nTASK 8: Product")
    p1 = Product("TV", 30000)
    print(p1.name, p1.price, Product.category)

    print("\nTASK 9: Employee")
    emp = Employee(101, "Alice", 50000)
    print(emp)

    print("\nTASK 10: Rectangle")
    r1 = Rectangle(5, 10)
    r2 = Rectangle(5, 10)
    r3 = Rectangle(4, 6)
    print("r1 == r2:", r1 == r2)
    print("r1 == r3:", r1 == r3)
