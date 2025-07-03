## 1. Age Calculator
print("========================================")
print("             Age Calculator             ")
print("========================================")
# 1. Prompt the user to enter their birth year
birth_year = int(input("Enter your birth year: "))

# 2. Calculate their current age
from datetime import datetime
current_year = datetime.now().year
age = current_year - birth_year

# 3. Display the age using an f-string
print(f"You are {age} years old.")

# 4. Use type() to show the type of the age variable
print(f"The type of 'age' variable is: {type(age)}")
