## 1. Setup, Introduction, and print()

# 1. Print "Hello, Python!" to the output.
print("Hello, Python!")

# 2. Print your name and age using a single print() statement.
print("Name: Suganya, Age: 25")

# 3. Use print() to display three favorite fruits, separated by commas (using sep).
print("Mango", "Strawberry", "Pineapple", sep=", ")

# 4. Print "Python is fun" three times, all on the same line, using the end parameter.
print("Python is fun", end=" ")
print("Python is fun", end=" ")
print("Python is fun")

# 5. Use print() and f-strings to display: My favorite number is 42.
favorite_number = 42
print(f"My favorite number is {favorite_number}.")

# 6. Print the result of 5 + 7 using print().
print(5 + 7)

# 7. Write a comment in Python explaining what the print() function does.
# The print() function outputs text or variables to the console.

# 8. Combine print() with variables to display a message.
name = "Suganya"
course = "Python Full Stack"
print(f"{name} is enrolled in the {course} course.")

# 9. Use print() to show the output: Apple | Banana | Cherry (use sep).
print("Apple", "Banana", "Cherry", sep=" | ")

# 10. Print your city and country, each on a separate line, in a single print() call.
print("Madurai\nIndia")

## 2. Variables and Data Types
# 11. Create a variable called name and assign your first name. Print it.
name = "Suganya"
print(name)

# 12. Create a variable age and assign your age. Print it.
age = 25
print(age)

# 13. Create a float variable price, assign a value, and print it.
price = 199.99
print(price)

# 14. Define a boolean variable is_student and print its value.
is_student = True
print(is_student)

# 15. Make a list of three favorite colors and print the second color.
favorite_colors = ["Blue", "Green", "Pink"]
print(favorite_colors[1])  

# 16. Create a tuple called coordinates with two numbers and print both values.
coordinates = (12.5, 45.8)
print(coordinates[0], coordinates[1])

# 17. Define a dictionary with keys "brand" and "year" for a car. Print both values.
car = {"brand": "Toyota", "year": 2020}
print(car["brand"], car["year"])

# 18. Create a set of three unique numbers and print the set.
unique_numbers = {5, 10, 15}
print(unique_numbers)

# 19. Change the value of a variable after assigning it. Print before and after.
course = "Python"
print("Before:", course)
course = "Full Stack Python"
print("After:", course)

# 20. Assign a string to a variable, then print its type using type().
language = "Python"
print(type(language))  


## 3. Data Types: Examples
# 21. Assign an integer to a variable and print it.
my_integer = 100
print(my_integer)

# 22. Assign a float to a variable and print it.
my_float = 3.14
print(my_float)

# 23. Assign a string with your favorite quote and print it.
favorite_quote = "Believe you can and you're halfway there."
print(favorite_quote)

# 24. Assign True to a boolean variable and print it.
is_learning = True
print(is_learning)

# 25. Create a list of five subjects and print the last subject.
subjects = ["Math", "Science", "English", "History", "Computer"]
print(subjects[-1])

# 26. Make a tuple of three city names and print the first one.
cities = ("Chennai", "Mumbai", "Bangalore")
print(cities[0])  

# 27. Store information about a student (name, grade) in a dictionary and print it.
student_info = {"name": "Suganya", "grade": "A+"}
print(student_info)

# 28. Add duplicate values to a set and print the set.
my_set = {1, 2, 2, 3, 3, 3}
print(my_set) 

# 29. Store different data types in a list and print each with its type using a loop.
mixed_list = [42, 3.5, "Hello", True]
for item in mixed_list:
    print(item, "is of type", type(item))

# 30. Use a variable to store a value, then use type() to print its data type.
value = "Python Programming"
print("The type of value is:", type(value))

## 4. input() and f-strings
# 31. Ask the user for their name using input(), then greet them.
name = input("What is your name? ")
print(f"Hello, {name}!")

# 32. Ask for two numbers (as input), add them, and print the result.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"The sum is: {num1 + num2}")

# 33. Use input() to get a user's age, then print how old they'll be next year.
age = int(input("Enter your age: "))
print(f"Next year you will be {age + 1} years old.")

# 34. Ask the user for their favorite color and print a message using f-string.
color = input("What is your favorite color? ")
print(f"{color} is a beautiful choice!")

# 35. Get the user's city and country with input(), then print a formatted message.
city = input("Enter your city: ")
country = input("Enter your country: ")
print(f"You live in {city}, {country}.")

# 36. Ask for a price and a discount, calculate the discounted price, and print it using f-string.
price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))
discounted_price = price - (price * discount / 100)
print(f"The discounted price is: ₹{discounted_price:.2f}")

# 37. Use input() to get three hobbies, store them in a list, and print the list.
hobby1 = input("Enter your first hobby: ")
hobby2 = input("Enter your second hobby: ")
hobby3 = input("Enter your third hobby: ")
hobbies = [hobby1, hobby2, hobby3]
print("Your hobbies are:", hobbies)

# 38. Ask the user for their name and age, then print: "Alice is 25 years old." (replace with inputs)
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"{name} is {age} years old.")

# 39. Write a program that asks for two numbers, multiplies them, and prints the answer with f-string.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 * num2
print(f"The result of multiplication is: {result}")

# 40. Use input() to get a string, then print its type using type().
text = input("Enter any text: ")
print(f"The type of input is: {type(text)}")

## 5. type() Function and Data Type Checks
# 41. Create a variable with a value, then print its type using type().
value = 123
print(f"Value: {value}, Type: {type(value)}")

# 42. Use type() to check the type of user input.
user_input = input("Enter something: ")
print(f"Type of input: {type(user_input)}")

# 43. Store a number as string using input(), then convert it to int and print both types.
number_str = input("Enter a number: ")
number_int = int(number_str)
print(f"Original (string): {number_str}, Type: {type(number_str)}")
print(f"Converted (int): {number_int}, Type: {type(number_int)}")

# 44. Make a list with different data types and print each value with its type (using a loop).
mixed_list = [42, 3.14, "Python", True, [1, 2]]
for item in mixed_list:
    print(f"{item} -> {type(item)}")

# 45. Use type() to confirm that True is of type bool.
print(f"Type of True is: {type(True)}")

# 46. Ask the user for their birth year, convert it to int, and print its type.
birth_year = int(input("Enter your birth year: "))
print(f"Birth year type: {type(birth_year)}")

# 47. Create a tuple and print the type of the tuple.
my_tuple = (10, 20, 30)
print(f"Tuple: {my_tuple}, Type: {type(my_tuple)}")

# 48. Make a set, then print the set and its type.
my_set = {1, 2, 3}
print(f"Set: {my_set}, Type: {type(my_set)}")

# 49. Use type() to determine the data type of a value inside a dictionary.
person = {"name": "Alice", "age": 30}
print(f"Type of 'name': {type(person['name'])}")
print(f"Type of 'age': {type(person['age'])}")

# 50. Ask for a number, print its type, then convert it to float and print the new type.
num = input("Enter a number: ")
print(f"Original type: {type(num)}")
num_float = float(num)
print(f"After conversion to float: {type(num_float)}")


