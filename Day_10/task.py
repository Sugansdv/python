# Dictionary Basics

# 1. Create a dictionary with five employee names and their ID numbers.
employees = {
    "Alice": 1001,
    "Bob": 1002,
    "Charlie": 1003,
    "David": 1004,
    "Eve": 1005
}
print(employees)

# 2. Access and print the phone number from a contact dictionary.
contact = {
    "name": "John",
    "phone": "9876543210",
    "email": "john@example.com"
}
print("Phone Number:", contact["phone"])

# 3. Use the get() method to retrieve a value that may not exist in the dictionary.
age = contact.get("age")  # Returns None if key doesn't exist
print("Age:", age)

# With default value
age_with_default = contact.get("age", "Not specified")
print("Age (with default):", age_with_default)

# 4. Add a new key-value pair to a student marks dictionary.
marks = {"Math": 88, "Science": 92}
marks["English"] = 85
print(marks)

# 5. Update an existing student's score in the marks dictionary.
marks["Math"] = 90  # Updating existing score
print("Updated Marks:", marks)

# 6. Delete a key from a dictionary using del.
del marks["Science"]
print("After deletion:", marks)

# 7. Use pop() to remove a key and display the returned value.
removed_score = marks.pop("English")
print("Removed English score:", removed_score)
print("After pop:", marks)

# 8. Use popitem() and explain how it works (removes and returns the last inserted key-value pair).
marks = {"Math": 90, "History": 80}
item = marks.popitem()
print("Popped item:", item)
print("After popitem:", marks)

# 9. Clear all entries in a dictionary using clear() and show the result.
marks.clear()
print("After clear:", marks)  # Output: {}

# 10. Check if a key exists in the dictionary using the in keyword.
employees = {"Alice": 1001, "Bob": 1002}
if "Alice" in employees:
    print("Alice is an employee.")
else:
    print("Alice not found.")

# Dictionary Iteration

# 11. Loop through a dictionary and print all keys.
student_scores = {"Alice": 95, "Bob": 87, "Charlie": 91}

print("Keys:")
for key in student_scores:
    print(key)

# 12. Loop through a dictionary and print all values.
print("Values:")
for value in student_scores.values():
    print(value)

# 13. Loop through both keys and values using .items().
print("Key-Value Pairs:")
for name, score in student_scores.items():
    print(f"{name}: {score}")

# 14. Count how many values in a dictionary are above a certain threshold (e.g., 90).
threshold = 90
count = 0
for score in student_scores.values():
    if score > threshold:
        count += 1

print(f"Number of scores above {threshold}:", count)

# 15. Create a function that returns all keys that have a specific value.
def find_keys_by_value(d, target_value):
    return [key for key, value in d.items() if value == target_value]

# Example usage
result = find_keys_by_value(student_scores, 91)
print("Keys with value 91:", result)

# Dictionary Methods

# 16. Use update() to merge two dictionaries.
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print("Merged Dictionary:", dict1)

# 17. Use setdefault() to add a key only if it doesn't exist.
student = {"name": "Alice"}
student.setdefault("age", 20)  # Adds 'age' if not present
student.setdefault("name", "Bob")  # Won't overwrite existing 'name'
print("After setdefault:", student)

# 18. Use copy() to duplicate a dictionary, then prove they are separate.
original = {"x": 10, "y": 20}
duplicate = original.copy()

duplicate["x"] = 99
print("Original:", original)
print("Duplicate:", duplicate)

# 19. Create a dictionary using dict() constructor from a list of tuples.
tuple_list = [("apple", 3), ("banana", 5), ("cherry", 2)]
fruit_dict = dict(tuple_list)
print("Fruit Dictionary:", fruit_dict)

# 20. Get a list of all keys using .keys() and all values using .values().
print("Keys:", list(fruit_dict.keys()))
print("Values:", list(fruit_dict.values()))

# Practical Use Cases

# 21. Create a shopping cart dictionary: item name as key, quantity as value.
shopping_cart = {
    "Apples": 4,
    "Bananas": 6,
    "Milk": 2,
    "Bread": 1
}
print("Shopping Cart:", shopping_cart)

# 22. Build a grade book dictionary with student names and their grades.
grade_book = {
    "Alice": "A",
    "Bob": "B+",
    "Charlie": "A-",
    "David": "C"
}
print("Grade Book:", grade_book)

# 23. Make a phonebook dictionary and search for a contact.
phonebook = {
    "Alice": "9876543210",
    "Bob": "8765432109",
    "Charlie": "7654321098"
}

search_name = "Charlie"
if search_name in phonebook:
    print(f"{search_name}'s number is {phonebook[search_name]}")
else:
    print(f"{search_name} not found in phonebook.")

# 24. Develop a product inventory system where product ID is the key and stock info is the value.
inventory = {
    101: {"name": "Laptop", "stock": 15, "price": 75000},
    102: {"name": "Mouse", "stock": 50, "price": 500},
    103: {"name": "Keyboard", "stock": 30, "price": 1200}
}

for pid, details in inventory.items():
    print(f"Product ID: {pid}, Name: {details['name']}, Stock: {details['stock']}, Price: ₹{details['price']}")

# 25. Track attendance using a dictionary with dates as keys and list of students as values.
attendance = {
    "2025-07-15": ["Alice", "Bob", "Charlie"],
    "2025-07-16": ["Alice", "David"],
    "2025-07-17": ["Bob", "Charlie", "Eve"]
}

for date, students in attendance.items():
    print(f"Date: {date} → Present: {', '.join(students)}")

# Nested Dictionaries

# 26. Create a nested dictionary for employees: {emp_id: {"name":..., "salary":...}}
employees = {
    101: {"name": "Alice", "salary": 50000},
    102: {"name": "Bob", "salary": 60000},
    103: {"name": "Charlie", "salary": 55000}
}
print("Employees:", employees)

# 27. Access a nested value from the above dictionary.
print("Bob's Salary:", employees[102]["salary"])

# 28. Add a new employee to the nested dictionary.
employees[104] = {"name": "David", "salary": 62000}
print("Added New Employee:", employees[104])

# 29. Update only the salary of a specific employee in the nested dictionary.
employees[101]["salary"] = 52000  # Update Alice's salary
print("Updated Salary for Alice:", employees[101])

# 30. Loop through the nested dictionary and print employee name and salary.
print("Employee Details:")
for emp_id, info in employees.items():
    print(f"ID: {emp_id} → Name: {info['name']}, Salary: ₹{info['salary']}")


# Dictionary Comprehension

# 31. Generate a dictionary of squares: {n: n**2 for n in range(1, 6)}.
squares = {n: n**2 for n in range(1, 6)}
print("Squares Dictionary:", squares)

# 32. Create a dictionary from a list of numbers where values are "even"/"odd".
numbers = [1, 2, 3, 4, 5, 6]
parity = {n: "even" if n % 2 == 0 else "odd" for n in numbers}
print("Even/Odd Dictionary:", parity)

# 33. Convert a list of words into a dictionary with word as key and length as value.
words = ["apple", "banana", "kiwi", "grape"]
word_lengths = {word: len(word) for word in words}
print("Word Length Dictionary:", word_lengths)

# 34. Swap keys and values in a dictionary using comprehension.
original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}
print("Swapped Dictionary:", swapped)

# 35. Filter a dictionary to retain only items with values greater than a threshold.
marks = {"Alice": 92, "Bob": 85, "Charlie": 78, "David": 95}
filtered = {name: score for name, score in marks.items() if score > 90}
print("Filtered (score > 90):", filtered)

# Data Processing

# 36. Count the frequency of each character in a given string using a dictionary.
text = "dictionary"
char_count = {}

for char in text:
    char_count[char] = char_count.get(char, 0) + 1

print("Character Frequency:", char_count)

# 37. Create a word count dictionary from a paragraph.
paragraph = "Python is great and Python is easy to learn"
words = paragraph.lower().split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word Count:", word_count)

# 38. Create a dictionary to store fruit prices and find the most expensive fruit.
fruit_prices = {"Apple": 120, "Banana": 40, "Mango": 150, "Orange": 90}
most_expensive = max(fruit_prices, key=fruit_prices.get)

print("Fruit Prices:", fruit_prices)
print("Most Expensive Fruit:", most_expensive, "→ ₹", fruit_prices[most_expensive])

# 39. Calculate total value of inventory using product price and quantity dictionaries.
product_prices = {"Pen": 10, "Notebook": 50, "Pencil": 5}
product_quantity = {"Pen": 100, "Notebook": 30, "Pencil": 200}

total_value = sum(product_prices[item] * product_quantity[item] for item in product_prices)
print("Total Inventory Value: ₹", total_value)

# 40. Group a list of students by grade into a dictionary.
students = [("Alice", "A"), ("Bob", "B"), ("Charlie", "A"), ("David", "C"), ("Eve", "B")]

grade_groups = {}
for name, grade in students:
    grade_groups.setdefault(grade, []).append(name)

print("Grouped by Grade:", grade_groups)

# Advanced Applications

# 41. Implement a caching system using a dictionary to store function results.
cache = {}

def fib(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
    cache[n] = result
    return result

print("Fibonacci(10):", fib(10))
print("Cache Contents:", cache)

# 42. Simulate a URL shortening service using dictionaries.
url_map = {}
short_counter = 1

def shorten_url(long_url):
    global short_counter
    short_key = f"url{short_counter}"
    url_map[short_key] = long_url
    short_counter += 1
    return short_key

def retrieve_url(short_key):
    return url_map.get(short_key, "Not found")

short = shorten_url("https://example.com/my-long-article")
print("Shortened:", short)
print("Original URL:", retrieve_url(short))

# 43. Build a language translator using a dictionary (English → Tamil).
translator = {
    "hello": "வணக்கம்",
    "thank you": "நன்றி",
    "book": "நூல்",
    "water": "தண்ணீர்"
}

def translate(word):
    return translator.get(word.lower(), "Translation not found")

print("Translate 'hello':", translate("hello"))
print("Translate 'book':", translate("book"))

# 44. Simulate a login system where usernames and passwords are stored in a dictionary.
users = {"alice": "pass123", "bob": "qwerty"}

def login(username, password):
    if users.get(username) == password:
        return "Login successful"
    else:
        return "Invalid username or password"

print(login("alice", "pass123"))  
print(login("bob", "wrongpass"))  

# 45. Develop a movie collection manager where movie title is key and info like (year, genre) is the value.
movies = {
    "Inception": {"year": 2010, "genre": "Sci-Fi"},
    "The Godfather": {"year": 1972, "genre": "Crime"},
    "Parasite": {"year": 2019, "genre": "Thriller"}
}

# Add a movie
movies["Interstellar"] = {"year": 2014, "genre": "Sci-Fi"}

# Display all movies
for title, info in movies.items():
    print(f"{title} → Year: {info['year']}, Genre: {info['genre']}")

# Utility Tools

# 46. Create a dictionary-based simple calculator (keys as operators and values as functions).
def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y if y != 0 else "Error: Divide by zero"

calculator = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

op = '+'
a, b = 10, 5
print(f"{a} {op} {b} =", calculator[op](a, b))

# 47. Build a travel expense tracker using a dictionary where destinations are keys and costs are values.
travel_expenses = {
    "Delhi": 4500,
    "Mumbai": 5200,
    "Chennai": 3800
}

# Add a new expense
travel_expenses["Bangalore"] = 4700

# Calculate total
total = sum(travel_expenses.values())
print("Total Travel Expense: ₹", total)

# 48. Develop a file extension counter: count how many files per extension from a list of filenames.
files = ["data.csv", "image.png", "script.py", "report.pdf", "photo.png", "notes.txt", "archive.zip", "main.py"]

ext_count = {}
for filename in files:
    ext = filename.split(".")[-1]
    ext_count[ext] = ext_count.get(ext, 0) + 1

print("File Extension Count:", ext_count)

# 49. Build a dictionary that maps countries to their capital cities and allow searching.
capitals = {
    "India": "New Delhi",
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}

country = "Japan"
print(f"Capital of {country}:", capitals.get(country, "Not found"))

# 50. Create a quiz app using dictionaries: {question: correct_option} and verify answers.
quiz = {
    "What is the capital of India?": "New Delhi",
    "What is 2 + 2?": "4",
    "Which planet is known as the Red Planet?": "Mars"
}

score = 0
for question, correct in quiz.items():
    print(question)
    answer = input("Your answer: ")
    if answer.strip().lower() == correct.lower():
        print(" Correct!\n")
        score += 1
    else:
        print(f" Wrong. Correct answer: {correct}\n")

print("Your Score:", score, "/", len(quiz))
