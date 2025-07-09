## Basic While Loop Tasks (1–10)
# Task 1: Print numbers from 1 to 10 using a while loop
print("Task 1:")
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1

print("\n" + "-"*40)

# Task 2: Print even numbers from 2 to 20 using a while loop
print("Task 2:")
i = 2
while i <= 20:
    print(i, end=" ")
    i += 2

print("\n" + "-"*40)

# Task 3: Print the reverse numbers from 10 to 1
print("Task 3:")
i = 10
while i >= 1:
    print(i, end=" ")
    i -= 1

print("\n" + "-"*40)

# Task 4: Ask the user to enter a number and print all numbers up to that number
print("Task 4:")
limit = int(input("Enter a number: "))
i = 1
while i <= limit:
    print(i, end=" ")
    i += 1

print("\n" + "-"*40)

# Task 5: Calculate the sum of numbers from 1 to 50 using while
print("Task 5:")
i = 1
total = 0
while i <= 50:
    total += i
    i += 1
print("Sum from 1 to 50:", total)

print("-"*40)

# Task 6: Find the factorial of a number using a while loop
print("Task 6:")
num = int(input("Enter a number to find factorial: "))
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print(f"Factorial of {num} is {fact}")

print("-"*40)

# Task 7: Print all multiples of 3 between 1 and 30
print("Task 7:")
i = 1
while i <= 30:
    if i % 3 == 0:
        print(i, end=" ")
    i += 1

print("\n" + "-"*40)

# Task 8: Take user input until they type "stop"
print("Task 8:")
while True:
    text = input("Type something (or 'stop' to end): ")
    if text.lower() == "stop":
        break
    print("You typed:", text)

print("-"*40)

# Task 9: Count from 100 down to 50 in steps of 5
print("Task 9:")
i = 100
while i >= 50:
    print(i, end=" ")
    i -= 5

print("\n" + "-"*40)

# Task 10: Take 5 inputs from user and store them in a list using a while loop
print("Task 10:")
inputs = []
i = 0
while i < 5:
    value = input(f"Enter value {i+1}: ")
    inputs.append(value)
    i += 1
print("Collected inputs:", inputs)

## Infinite While Loop Tasks (11–15)

#  Task 11: Create a while True loop that prints "Welcome!" infinitely (Manually stop it).
# while True:
#     print("Welcome!")

# Task 12: Create a login simulation that keeps asking for a correct password until it's matched.
print("Task 12: Login Simulation")
correct_password = "python123"
while True:
    user_input = input("Enter password: ")
    if user_input == correct_password:
        print("Login successful!")
        break
    else:
        print("Incorrect password, try again.")

print("-" * 40)

# Task 13: Simulate a menu-based app using an infinite loop (while True) with exit option.
print("Task 13: Menu-based App")
while True:
    print("\nMenu:")
    print("1. Greet")
    print("2. Help")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Hello! Have a great day.")
    elif choice == "2":
        print("This is a simple menu-based app using while loop.")
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")

print("-" * 40)

# Task 14: Continuously ask for a number until the user enters a negative number.
print("Task 14: Ask Until Negative Number")
while True:
    num = int(input("Enter a number (negative to stop): "))
    if num < 0:
        print("Negative number entered. Exiting loop.")
        break
    else:
        print(f"You entered: {num}")

print("-" * 40)

# Task 15: Simulate an ATM system using an infinite loop with options: check balance, deposit, withdraw, exit.
print("Task 15: ATM Simulation")
balance = 1000  
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Your balance is: ₹{balance}")
    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))
        balance += amount
        print(f"₹{amount} deposited. New balance: ₹{balance}")
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount > balance:
            print("Insufficient funds!")
        else:
            balance -= amount
            print(f"₹{amount} withdrawn. Remaining balance: ₹{balance}")
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")


## While with continue Statement (16–25)
# Task 16: Print odd numbers from 1 to 20 using continue.
print("Task 16: Odd numbers from 1 to 20")
i = 1
while i <= 20:
    if i % 2 == 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1

print("\n" + "-"*40)

# Task 17: Ask the user to enter 5 numbers. Skip the number if it is negative using continue.
print("Task 17: Skip negative numbers from user input")
count = 0
while count < 5:
    num = int(input(f"Enter number {count+1}: "))
    if num < 0:
        print("Negative number skipped.")
        continue
    print(f"You entered: {num}")
    count += 1

print("-"*40)

# Task 18: Print numbers from 1 to 10, but skip 5 using continue.
print("Task 18: Skip number 5")
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i, end=" ")
    i += 1

print("\n" + "-"*40)

# Task 19: Print all numbers from 1 to 20 except those divisible by 3.
print("Task 19: Skip numbers divisible by 3")
i = 1
while i <= 20:
    if i % 3 == 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1

print("\n" + "-"*40)

# Task 20: Ask the user to enter 10 words. Skip if the word is less than 3 characters.
print("Task 20: Skip short words (<3 characters)")
i = 0
while i < 10:
    word = input(f"Enter word {i+1}: ")
    if len(word) < 3:
        print("Word too short, skipped.")
        continue
    print(f"Accepted word: {word}")
    i += 1

print("-"*40)

# Task 21: Print only vowels from the string "python programming" using while and continue.
print("Task 21: Vowels in 'python programming'")
text = "python programming"
i = 0
while i < len(text):
    if text[i] not in "aeiou":
        i += 1
        continue
    print(text[i], end=" ")
    i += 1

print("\n" + "-"*40)

# Task 22: Count how many odd numbers exist between 1 and 100.
print("Task 22: Count odd numbers between 1 and 100")
i = 1
count = 0
while i <= 100:
    if i % 2 == 0:
        i += 1
        continue
    count += 1
    i += 1
print("Total odd numbers:", count)

print("-"*40)

# Task 23: Keep asking user for numbers and print only if it's a multiple of 5.
print("Task 23: Print only multiples of 5 (Type 0 to stop)")
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    if num % 5 != 0:
        continue
    print(f"{num} is a multiple of 5")

print("-"*40)

# Task 24: Skip printing numbers divisible by both 2 and 3 from 1 to 30.
print("Task 24: Skip numbers divisible by both 2 and 3")
i = 1
while i <= 30:
    if i % 2 == 0 and i % 3 == 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1

print("\n" + "-"*40)

# Task 25: Skip even numbers and print the cube of odd numbers between 1 and 20.
print("Task 25: Cube of odd numbers between 1 and 20")
i = 1
while i <= 20:
    if i % 2 == 0:
        i += 1
        continue
    print(f"{i}³ = {i**3}")
    i += 1

##While with break Statement (26–35)
# Task 26: Print numbers from 1 to 10 and break the loop if number is 6.
print("Task 26: Break if number is 6")
i = 1
while i <= 10:
    if i == 6:
        print("Breaking loop at", i)
        break
    print(i, end=" ")
    i += 1

print("\n" + "-"*40)

# Task 27: Ask the user to enter numbers. Break the loop when user enters 0.
print("Task 27: Break when user enters 0")
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        print("Zero entered. Loop stopped.")
        break
    print("You entered:", num)

print("-"*40)

# Task 28: Create a simple password checker. Break the loop if the correct password is entered.
print("Task 28: Password Checker")
correct_password = "open123"
while True:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access granted.")
        break
    print("Wrong password, try again.")

print("-"*40)

# Task 29: Print numbers from 1 to 100. Break the loop when a number divisible by 17 is found.
print("Task 29: Break when number divisible by 17 is found")
i = 1
while i <= 100:
    if i % 17 == 0:
        print(f"Found {i} divisible by 17. Breaking...")
        break
    print(i, end=" ")
    i += 1

print("\n" + "-"*40)

# Task 30: Keep asking for user input until they type "exit" (use break to stop).
print("Task 30: Stop when user types 'exit'")
while True:
    text = input("Type something (or 'exit' to stop): ")
    if text.lower() == "exit":
        print("Exiting...")
        break
    print("You typed:", text)

print("-"*40)

# Task 31: Simulate a game loop: “Press q to quit”.
print("Task 31: Game Loop - Press 'q' to quit")
while True:
    choice = input("Press any key (q to quit): ")
    if choice.lower() == 'q':
        print("Game exited.")
        break
    print(f"You pressed: {choice}")

print("-"*40)

# Task 32: Ask the user 10 questions, stop early if any answer is empty using break.
print("Task 32: Stop if any answer is empty")
i = 1
while i <= 10:
    ans = input(f"Answer question {i}: ")
    if ans.strip() == "":
        print("Empty answer. Ending early.")
        break
    i += 1

print("-"*40)

# Task 33: Simulate 3 login attempts. Break the loop if login is successful.
print("Task 33: 3 Login Attempts")
password = "admin"
attempts = 0
while attempts < 3:
    entered = input("Enter password: ")
    if entered == password:
        print("Login successful!")
        break
    else:
        print("Incorrect password.")
    attempts += 1
if attempts == 3:
    print("Maximum attempts reached.")

print("-"*40)

# Task 34: Print the multiplication table of 5, but stop if the product exceeds 30.
print("Task 34: Table of 5 until product > 30")
i = 1
while True:
    product = 5 * i
    if product > 30:
        print(f"Product exceeded 30 at 5 x {i} = {product}. Breaking.")
        break
    print(f"5 x {i} = {product}")
    i += 1

##While with pass Statement (36–40)
# Task 36: Loop through 1 to 5 and use pass when number is 3.
print("Task 36: Use pass when number is 3")
i = 1
while i <= 5:
    if i == 3:
        pass  
    print(i)
    i += 1

print("-" * 40)

#  Task 37: Simulate a placeholder loop for future features.
print("Task 37: Placeholder loop for future features")
i = 0
while i < 3:
    pass  
    print(f"Step {i+1}: Feature coming soon...")
    i += 1

print("-" * 40)

# Task 38: Create a loop where you skip logic for even numbers using pass.
print("Task 38: Skip logic for even numbers using pass")
i = 1
while i <= 10:
    if i % 2 == 0:
        pass  
    else:
        print(f"Odd number: {i}")
    i += 1

print("-" * 40)

# Task 39: Use a loop that prints numbers 1 to 5 and uses pass when number is 2 or 4.
print("Task 39: Use pass for 2 and 4")
i = 1
while i <= 5:
    if i == 2 or i == 4:
        pass 
    print(i)
    i += 1

print("-" * 40)

# Task 40: Create a loop that runs without errors using pass as a placeholder for missing logic.
print("Task 40: Loop with placeholder logic using pass")
i = 1
while i <= 3:
    pass
    print(f"Loop running... step {i}")
    i += 1

# Task 41: Print numbers from 1 to 3. Use else to print "Loop Finished".
print("Task 41: Loop with else - Print 1 to 3")
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop Finished")

print("-" * 40)

# Task 42: Ask the user to enter 3 numbers. Use else to say “All numbers entered successfully”.
print("Task 42: Input 3 numbers with while-else")
count = 0
while count < 3:
    try:
        num = int(input(f"Enter number {count + 1}: "))
        count += 1
    except:
        print("Invalid input.")
else:
    print("All numbers entered successfully")

print("-" * 40)

# Task 43: Run a loop to print even numbers till 10. Use break to exit early. Ensure else doesn’t run.
print("Task 43: Break early, else should not run")
i = 2
while i <= 10:
    print(i)
    if i == 6:
        print("Breaking early at", i)
        break
    i += 2
else:
    print("Loop finished normally") 

print("-" * 40)

#  Task 44: Print numbers from 1 to 5. If loop finishes without break, print “Nice job!”.
print("Task 44: Finish without break")
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Nice job!")  

print("-" * 40)

# Task 45: Create a password checker with 3 attempts. If successful, print inside else.
print("Task 45: Password Checker with 3 attempts and else")
correct_password = "sugan@123"
attempts = 0

while attempts < 3:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password.")
    attempts += 1
else:
    print("Too many failed attempts. Try later.")

##Logical/Practical Looping Use-Cases (46–50)
# Task 46: Ask the user to input 5 student names using while and store them in a list.
print("Task 46: Collect 5 student names")
students = []
i = 0
while i < 5:
    name = input(f"Enter name of student {i+1}: ")
    if name.strip() == "":
        print("Empty name, try again.")
        continue
    students.append(name)
    i += 1
print("Student List:", students)

print("-" * 40)

# Task 47: Create a menu-driven loop for a to-do list app (add, view, remove, exit).
print("Task 47: To-Do List App")
todo_list = []

while True:
    print("\nMenu:\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task to add: ")
        todo_list.append(task)
        print("Task added.")
    elif choice == "2":
        print("Your Tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    elif choice == "3":
        if not todo_list:
            print("No tasks to remove.")
            continue
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
        try:
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(todo_list):
                removed = todo_list.pop(index)
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a valid number.")
    elif choice == "4":
        print("Exiting To-Do App.")
        break
    else:
        print("Invalid choice. Try again.")

print("-" * 40)

#  Task 48: Ask the user to enter age of 5 people. Print how many are adults (age ≥ 18).
print("Task 48: Count number of adults")
count = 0
adults = 0
while count < 5:
    try:
        age = int(input(f"Enter age of person {count+1}: "))
        if age >= 18:
            adults += 1
        count += 1
    except:
        print("Invalid input. Try again.")
print("Number of adults (18+):", adults)

print("-" * 40)

# Task 49: Create a quiz loop: keep asking until the user gets the correct answer.
print("Task 49: Quiz Loop")
question = "What is the capital of France? "
correct_answer = "paris"

while True:
    answer = input(question).strip().lower()
    if answer == correct_answer:
        print("Correct! Well done.")
        break
    else:
        print("Incorrect. Try again.")

print("-" * 40)

#  Task 50: Build a basic number guessing game.
import random
print("Task 50: Number Guessing Game")
secret = random.randint(1, 10)
while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == secret:
            print(" Correct! You guessed it.")
            break
        else:
            print(" Wrong guess. Try again.")
    except:
        print("Please enter a valid number.")


