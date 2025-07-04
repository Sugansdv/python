# 🧠 Conditional Statements – (41–50)

# Task 41: Ask user for age and print if eligible to vote using if.
print(" Task 41: Voter Eligibility Check (using if)")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote ")

# Task 42: Ask for age, print "Minor" if less than 18, else "Adult" using if-else.
print("\n Task 42: Age Group - Minor or Adult (if-else)")
age = int(input("Enter your age: "))
if age < 18:
    print("You are a Minor ")
else:
    print("You are an Adult ")

# Task 43: Ask for marks and print grades using if-elif-else.
print("\n Task 43: Grading System")
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: Fail")

# Task 44: Ask for temperature and print weather condition.
print("\n Task 44: Temperature Condition")
temp = float(input("Enter temperature (°C): "))
if temp > 35:
    print("Weather: Hot ")
elif 25 <= temp <= 35:
    print("Weather: Warm ")
else:
    print("Weather: Cool ")

# Task 45: Ask for a number and print if even or odd using if-else.
print("\n Task 45: Even or Odd Number")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even ")
else:
    print(f"{num} is Odd ")


# Task 46: Simulate login check with username and password.
print("\n Task 46: Login Simulation")
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login successful ")
else:
    print("Invalid credentials ")

# Task 47: Nested if for rain and umbrella check.
print("\n Task 47: Rain and Umbrella Check (Nested if)")
rain = input("Is it raining? (yes/no): ").lower()
if rain == "yes":
    umbrella = input("Do you have an umbrella? (yes/no): ").lower()
    if umbrella == "yes":
        print("You can go outside with your umbrella ")
    else:
        print("Better stay inside ")
else:
    print("Weather is clear, you can go outside ")

# Task 48: Voting eligibility with age and nationality check.
print("\n Task 48: Voting Eligibility (Age + Nationality)")
age = int(input("Enter your age: "))
nation = input("Enter your nationality: ").lower()
if age >= 18 and nation == "indian":
    print("You are eligible to vote in India ")
else:
    print("Not eligible to vote ")

# Task 49: Simple calculator using if-elif-else
print("\n Task 49: Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (add/sub): ").lower()
if operation == "add":
    print(f"Result = {num1 + num2}")
elif operation == "sub":
    print(f"Result = {num1 - num2}")
else:
    print("Invalid operation ")

# Task 50: Check pass/fail using marks and attendance
print("\n Task 50: Exam Result (Marks + Attendance)")
marks = float(input("Enter your marks: "))
attendance = float(input("Enter your attendance (%): "))
if marks >= 40 and attendance >= 75:
    print("Result: Passed ")
else:
    print("Result: Failed ")
