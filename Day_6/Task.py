##Basic Function Definition and Calling 
# Task 1: Define a function greet() that prints “Welcome to Python!”.
def greet():
    print("Welcome to Python!")

print("--- Task 1 ---")
greet()

# Task 2: Write a function add(a, b) that returns the sum of two numbers.
def add(a, b):
    return a + b

print("\n--- Task 2 ---")
print("Sum:", add(5, 3))

# Task 3: Define a function is_even(num) that returns True if the number is even.
def is_even(num):
    return num % 2 == 0

print("\n--- Task 3 ---")
print("Is 4 even?", is_even(4))

# Task 4: Create a function cube(n) that returns the cube of a number.
def cube(n):
    return n ** 3

print("\n--- Task 4 ---")
print("Cube of 3:", cube(3))


# Task 5: Write a function hello(name) that prints "Hello, <name>".
def hello(name):
    print(f"Hello, {name}")
    
print("\n--- Task 5 ---")
hello("Alice")

# Task 6: Define a function with no code yet using pass.
def future_function():
    pass

print("\n--- Task 6 ---")
future_function()  # No output

# Task 7: Create a function that takes two numbers and prints which is greater using if.
def compare(a, b):
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    else:
        print("Both numbers are equal")
    

print("\n--- Task 7 ---")
compare(10, 20)

# Task 8: Write a function square_area(side) to return the area of a square.
def square_area(side):
    return side * side


print("\n--- Task 8 ---")
print("Area of square with side 4:", square_area(4))

# Task 9: Create a menu-based function with options (view, add, exit) using if-else.
def menu():
    print("1. View")
    print("2. Add")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        print("Viewing records...")
    elif choice == "2":
        print("Adding a new record...")
    elif choice == "3":
        print("Exiting...")
    else:
        print("Invalid choice!")

print("\n--- Task 9 ---")
menu()

# Task 10: Call a function multiple times in a loop to show reusability.
def repeat_message():
    print("This is a reusable function.")

print("\n--- Task 10 ---")
for _ in range(3):
    repeat_message()

# Functions with Parameters and Return Values (11–15)
# Task 11: Define a function divide(a, b) and return the quotient. Handle divide-by-zero.
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
print("--- Task 11 ---")
print("Divide 10 by 2:", divide(10, 2))
print("Divide 10 by 0:", divide(10, 0))

# Task 12: Create a function full_name(fname, lname) that returns a full name.
def full_name(fname, lname):
    return f"{fname} {lname}"

print("\n--- Task 12 ---")
print("Full Name:", full_name("John", "Doe"))

# Task 13: Write a function that takes age as input and returns if the user is eligible to vote.
def is_eligible_to_vote(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

print("\n--- Task 13 ---")
print("Age 20:", is_eligible_to_vote(20))
print("Age 16:", is_eligible_to_vote(16))

# Task 14: Create a function calc_discount(price, discount_percent) that returns the final price.
def calc_discount(price, discount_percent):
    discount = price * (discount_percent / 100)
    final_price = price - discount
    return final_price

print("\n--- Task 14 ---")
print("Final Price after 20% discount on ₹1000:", calc_discount(1000, 20))

# Task 15: Write a function to calculate and return the average of 3 numbers.
def average_of_three(a, b, c):
    return (a + b + c) / 3

print("\n--- Task 15 ---")
print("Average of 5, 10, 15:", average_of_three(5, 10, 15))

#Global vs Local Variables (16–20)
# Task 16: Create a global variable x = 100, and print it inside a function.
x = 100  # Global variable

def show_global():
    print("Global x inside function:", x)
print("--- Task 16 ---")
show_global()

# Task 17: Create a function with a local variable and show that it's not accessible outside.
def local_scope():
    y = 50  # Local variable
    print("Local y inside function:", y)
    
print("\n--- Task 17 ---")
local_scope()
# print(y)  # Uncommenting this will cause an error: NameError: name 'y' is not defined

# Task 18: Use both a global and a local variable in the same function and print both.
def mixed_scope():
    a = 10  # Local variable
    print("Global x:", x)
    print("Local a:", a)

print("\n--- Task 18 ---")
mixed_scope()

# Task 19: Modify a global variable inside a function using the global keyword.
count = 0

def increment():
    global count
    count += 1
    print("Updated global count:", count)
print("\n--- Task 19 ---")
print("Before increment, count =", count)
increment()
print("After increment, count =", count)

# Task 20: Show that a variable with the same name inside a function doesn’t affect the global one.
msg = "Hello, World!"  # Global variable

def shadow_variable():
    msg = "Local Message"
    print("Inside function (local msg):", msg)

print("\n--- Task 20 ---")
print("Global msg before function call:", msg)
shadow_variable()
print("Global msg after function call:", msg)

#Recursion Tasks (21–25)
# Task 21: Write a recursive function to calculate factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print("--- Task 21 ---")
print("Factorial of 5:", factorial(5))

# Task 22: Create a recursive function to calculate the nth Fibonacci number.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\n--- Task 22 ---")
print("7th Fibonacci number:", fibonacci(7))

# Task 23: Use recursion to reverse a string.
def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

print("\n--- Task 23 ---")
print("Reversed 'hello':", reverse_string("hello"))

# Task 24: Use recursion to sum all elements in a list.
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

print("\n--- Task 24 ---")
print("Sum of [1, 2, 3, 4, 5]:", sum_list([1, 2, 3, 4, 5]))

# Task 25: Write a recursive function that counts down from a number to 1.
def countdown(n):
    if n <= 0:
        return
    print(n)
    countdown(n - 1)

print("\n--- Task 25 ---")
print("Countdown from 5:")
countdown(5)

#*args and **kwargs Tasks (26–30)
# Task 26: Write a function add_numbers(*args) that returns the sum of all arguments.
def add_numbers(*args):
    return sum(args)
print("--- Task 26 ---")
print("Sum:", add_numbers(1, 2, 3, 4, 5))

# Task 27: Create a function that prints all positional arguments received via *args.
def print_args(*args):
    print("Positional arguments:")
    for arg in args:
        print(arg)

print("\n--- Task 27 ---")
print_args("Apple", "Banana", "Cherry")

# Task 28: Create a function student_info(**kwargs) to print student data.
def student_info(**kwargs):
    print("Student Information:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print("\n--- Task 28 ---")
student_info(name="Dharun", age=20, course="Python")

# Task 29: Combine *args and **kwargs in one function and display both.
def display_all(*args, **kwargs):
    print("Positional arguments (*args):")
    for arg in args:
        print(arg)
    print("Keyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print("\n--- Task 29 ---")
display_all(10, 20, name="Vishwa", city="Madurai")

# Task 30: Write a function that accepts an unknown number of keyword arguments and filters only those with integer values.
def filter_integers(**kwargs):
    int_values = {key: value for key, value in kwargs.items() if isinstance(value, int)}
    return int_values

print("\n--- Task 30 ---")
result = filter_integers(name="Dharun", age=25, score=88, city="Paris", height=5.9)
print("Filtered integer keyword arguments:", result)

#Lambda Functions (31–35)
# Task 31: Write a lambda function to add two numbers.
add = lambda a, b: a + b
print("--- Task 31 ---")
print("Add 5 + 3:", add(5, 3))

# Task 32: Create a lambda to return the square of a number.
square = lambda x: x ** 2
print("\n--- Task 32 ---")
print("Square of 6:", square(6))

# Task 33: Use lambda with sorted() to sort a list of tuples by second value.
pairs = [(1, 5), (2, 1), (4, 3), (3, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("\n--- Task 33 ---")
print("Sorted by second value:", sorted_pairs)

# Task 34: Replace a normal function with a lambda version.
# Normal Function
def cube(x):
    return x ** 3

# Lambda version
cube_lambda = lambda x: x ** 3
print("\n--- Task 34 ---")
print("Cube of 3 (lambda):", cube_lambda(3))

# Task 35: Use a lambda function inside another function (function returning lambda).
def power_function(n):
    return lambda x: x ** n

square_fn = power_function(2)
cube_fn = power_function(3)
print("\n--- Task 35 ---")
print("5 squared using returned lambda:", square_fn(5))
print("2 cubed using returned lambda:", cube_fn(2))

#Built-in Functions: map(), filter(), reduce() (36–40)
from functools import reduce  # Required for reduce()

# Task 36: Use map() and lambda to square every element in a list.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("--- Task 36 ---")
print("Squared list:", squared)

# Task 37: Use filter() to remove all odd numbers from a list.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("\n--- Task 37 ---")
print("Even numbers only:", even_numbers)

# Task 38: Use map() to convert a list of strings to uppercase.
words = ["apple", "banana", "cherry"]
uppercase_words = list(map(str.upper, words))
print("\n--- Task 38 ---")
print("Uppercase words:", uppercase_words)

# Task 39: Use reduce() to calculate the product of a list.
product = reduce(lambda x, y: x * y, numbers)
print("\n--- Task 39 ---")
print("Product of list:", product)

# Task 40: Use filter() to return words longer than 5 characters from a list.
more_words = ["hello", "elephant", "sky", "umbrella", "tree"]
long_words = list(filter(lambda word: len(word) > 5, more_words))
print("\n--- Task 40 ---")
print("Words longer than 5 characters:", long_words)

# First-Class Functions (41–45)
# Task 41: Assign a function to a variable and call it using the new name.
def greet():
    return "Hello from the greet function!"

new_greet = greet  # Assigning to new variable
print("--- Task 41 ---")
print(new_greet())

# Task 42: Create a function that takes another function as an argument.
def shout(text):
    return text.upper()

def call_func(func, value):
    return func(value)

print("\n--- Task 42 ---")
print(call_func(shout, "hello world"))

# Task 43: Write a function that returns another function.
def outer():
    def inner():
        return "I am the inner function!"
    return inner

print("\n--- Task 43 ---")
result_func = outer()
print(result_func())  # Calling the returned function

# Task 44: Pass a lambda function as an argument to another function.
def apply_operation(func, x):
    return func(x)

print("\n--- Task 44 ---")
print(apply_operation(lambda n: n * n, 7))  # Passing lambda to square a number

# Task 45: Write a function that takes two numbers and a function (like add, subtract) and applies it.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculator(a, b, operation):
    return operation(a, b)

print("\n--- Task 45 ---")
print("Add:", calculator(10, 5, add))
print("Subtract:", calculator(10, 5, subtract))

#Inner Functions (46–47)
# Task 46: Write a function with a nested function inside that prints a message.
def outer_function():
    def inner_function():
        print("Hello from the inner function!")
    inner_function()

print("--- Task 46 ---")
outer_function()

# Task 47: Write a function that uses an inner function to double a number, and return the result.
def double_number(n):
    def inner():
        return n * 2
    return inner()

print("\n--- Task 47 ---")
print("Double of 5:", double_number(5))

# OOP: self and Class-based Function (48–49)
# Task 48: Create a class Person with attributes and a method greet() that uses self.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

print("--- Task 48 ---")
person1 = Person("Alice", 25)
person1.greet()

# Task 49: Create a class Calculator with methods add, subtract, using self.
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

print("\n--- Task 49 ---")
calc = Calculator(10, 4)
print("Addition:", calc.add())
print("Subtraction:", calc.subtract())

#Real-World Project-Based Function (50)
# Task 50: Billing App with functions and advanced concepts

# Global list to store items as (name, price) tuples
cart = []

# Function to add item to the cart
def add_item(*args):
    global cart
    for item in args:
        name, price = item
        cart.append((name, price))
    print(f"{len(args)} item(s) added to cart.")

# Function to get the total price of all items
def get_total():
    total = sum(price for _, price in cart)
    return total

# Function to apply discount using lambda
def apply_discount(percent):
    global cart
    discount_func = lambda price: price - (price * percent / 100)
    cart = [(name, round(discount_func(price), 2)) for name, price in cart]
    print(f"{percent}% discount applied to all items.")

print("--- Task 50: Billing App ---")
add_item(("Milk", 40), ("Bread", 30), ("Eggs", 50))
print("Cart items:", cart)

total_before = get_total()
print("Total before discount:", total_before)

apply_discount(10)

print("Cart after discount:", cart)
total_after = get_total()
print("Total after discount:", total_after)

