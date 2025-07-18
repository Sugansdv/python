import math
import random
import datetime
import calendar
import os
import os.path
import platform
import sys
import time
import statistics

# 11. math module
def math_operations():
    print("\n11. Math Module")
    print("Square root of 16:", math.sqrt(16))
    print("2 raised to power 3:", math.pow(2, 3))
    print("Factorial of 5:", math.factorial(5))

# 12. random module
def random_game():
    print("\n12. Random Number Game")
    number = random.randint(1, 10)
    guess = 5  # Hardcoded guess for example
    print(f"Random number: {number}, Your guess: {guess}")
    print("Correct!" if guess == number else "Try again!")

# 13. datetime module
def current_time_once():
    print("\n13. Current Time (one-time)")
    now = datetime.datetime.now()
    print("Time now:", now.strftime("%H:%M:%S"))

# 14. calendar module
def show_calendar():
    print("\n14. Calendar of Current Month")
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    print(calendar.month(year, month))

# 15. os module
def list_files():
    print("\n15. Files in Current Directory")
    print(os.listdir('.'))

# 16. os.path module
def file_check_write():
    print("\n16. File Check Before Writing")
    filename = "testfile.txt"
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("Hello, file created!")
        print("File created and written.")
    else:
        print("File already exists.")

# 17. platform module
def system_info():
    print("\n17. Platform Information")
    print("OS:", platform.system())
    print("Processor:", platform.processor())
    print("Python Version:", platform.python_version())

# 18. sys module
def show_args():
    print("\n18. Command-line Arguments")
    print("Arguments passed:", sys.argv)

# 19. time module
def delay_demo():
    print("\n19. Time Delay Demo")
    print("Message 1")
    time.sleep(1)
    print("Message 2 after 1 second")

# 20. statistics module
def stats_calc():
    print("\n20. Statistics Module")
    numbers = [1, 2, 2, 3, 4, 4, 4, 5]
    print("Mean:", statistics.mean(numbers))
    print("Median:", statistics.median(numbers))
    print("Mode:", statistics.mode(numbers))

# Call all functions
if __name__ == "__main__":
    math_operations()
    random_game()
    current_time_once()
    show_calendar()
    list_files()
    file_check_write()
    system_info()
    show_args()
    delay_demo()
    stats_calc()
