#List Creation & Basic Operations (Tasks 1–10)
# # Task 1: Create a list of 5 student names and print it.
students = ["Dharun", "Vishwa", "Sugan", "Santoz", "Manoj"]
print("Task 1 - Student List:", students)

# Task 2: Create a list with mixed data types (int, float, string, bool) and display each element.
mixed_list = [42, 3.14, "Hello", True]
print("\nTask 2 - Mixed Data Type List:")
for item in mixed_list:
    print(item)

# Task 3: Write a program to accept 5 numbers from the user and store them in a list.
numbers = []
print("\nTask 3 - Enter 5 numbers:")
for _ in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)
print("Task 3 - User Entered Numbers:", numbers)

# Task 4: Create an empty list and dynamically append 3 user inputs.
user_inputs = []
print("\nTask 4 - Enter 3 values:")
for _ in range(3):
    val = input("Enter value: ")
    user_inputs.append(val)
print("Task 4 - User Inputs:", user_inputs)

# Task 5: Write a program to create a list of 10 even numbers using a for loop.
even_numbers = []
for i in range(2, 22, 2):
    even_numbers.append(i)
print("\nTask 5 - Even Numbers List:", even_numbers)

# Task 6: Create two lists, one with integers and one with strings, then print them together.
int_list = [1, 2, 3]
str_list = ["one", "two", "three"]
print("\nTask 6 - Integer List:", int_list)
print("Task 6 - String List:", str_list)

# Task 7: Create a list of fruits and print only the first and last items using indexing.
fruits = ["apple", "banana", "cherry", "mango", "grape"]
print("\nTask 7 - First Fruit:", fruits[0])
print("Task 7 - Last Fruit:", fruits[-1])

# Task 8: Use negative indexing to print the second-last item in a list.
print("Task 8 - Second-Last Fruit:", fruits[-2])

# Task 9: Write a program to count the total number of elements in a list using len().
print("\nTask 9 - Total Fruits:", len(fruits))

# Task 10: Check and print the data type of a created list.
print("Task 10 - Data Type of 'fruits' List:", type(fruits))

#Accessing & Indexing Tasks (11–15)
# Task 11: Access and print each element of a list using a for loop with indexing.
colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
print("Task 11 - Accessing elements using indexing:")
for i in range(len(colors)):
    print(f"Index {i}: {colors[i]}")

# Task 12: Print every alternate item from a list using slicing.
print("\nTask 12 - Alternate items using slicing:")
print(colors[::2])  # Prints elements at index 0, 2, 4...

# Task 13: Create a list of cities and print the third character of the second city.
cities = ["Delhi", "Chennai", "Mumbai", "Kolkata"]
print("\nTask 13 - Third character of second city:")
print(cities[1][2])  # 'Chennai' => index 2 of string is 'e'

# Task 14: Write a program to reverse a list using slicing.
print("\nTask 14 - Reversed list:")
print(colors[::-1])

# Task 15: Access the last element of a list using both positive and negative indexing.
print("\nTask 15 - Last element using positive indexing:", colors[len(colors) - 1])
print("Task 15 - Last element using negative indexing:", colors[-1])

#Adding Elements to Lists (Tasks 16–20)
# Task 16: Start with an empty list and use append() to add 5 elements.
numbers = []
print("Task 16 - Appending 5 elements:")
for i in range(5):
    numbers.append(i + 1)
print("List after append:", numbers)

# Task 17: Insert an element at the 3rd position in a list.
print("\nTask 17 - Insert at 3rd position (index 2):")
numbers.insert(2, 99)
print("List after insert:", numbers)

# Task 18: Use extend() to add multiple elements to an existing list.
print("\nTask 18 - Using extend() to add multiple elements:")
extra = [6, 7, 8]
numbers.extend(extra)
print("List after extend:", numbers)

# Task 19: Take user input for a name and add it to an existing list of students.
students = ["Sugan", "Dharun", "Vishwa"]
new_name = input("\nTask 19 - Enter a new student name to add: ")
students.append(new_name)
print("Updated student list:", students)

# Task 20: Add all elements from one list into another using += and extend().
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using +=
list1_copy = list1.copy()
list1_copy += list2
print("\nTask 20 - List after += :", list1_copy)

# Using extend()
list1_copy2 = list1.copy()
list1_copy2.extend(list2)
print("Task 20 - List after extend():", list1_copy2)

#Updating List Items (Tasks 21–25)
# Task 21: Change the first element of a list to uppercase.
names = ["Sugan", "Dharun", "Vishwa"]
names[0] = names[0].upper()
print("Task 21 - Updated names list:", names)

# Task 22: Modify the price of a product in a list of prices (e.g., change index 2 value to 999).
prices = [199, 299, 499, 699]
prices[2] = 999
print("\nTask 22 - Updated prices list:", prices)

# Task 23: Update all odd numbers in a list by multiplying them by 2.
numbers = [1, 2, 3, 4, 5, 6]
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers[i] *= 2
print("\nTask 23 - Odd numbers doubled:", numbers)

# Task 24: Replace a fruit in a list with a new fruit.
fruits = ["apple", "banana", "mango", "grape"]
fruits[1] = "orange"  # Replacing 'banana' with 'orange'
print("\nTask 24 - Updated fruit list:", fruits)

# Task 25: Update the value of a nested list item (list[1][2] = 'done').
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
nested_list[1][2] = 'done'
print("\nTask 25 - Updated nested list:", nested_list)

#Removing Elements (Tasks 26–30)
# Task 26: Use remove() to delete a specific value from a list.
colors = ["red", "blue", "green", "yellow"]
colors.remove("green")  # Removes first occurrence of "green"
print("Task 26 - After remove('green'):", colors)

# Task 27: Use pop() without index to remove the last item and print the updated list.
colors.pop()  # Removes the last item
print("\nTask 27 - After pop() (last item removed):", colors)

# Task 28: Use pop(index) to remove the 2nd element in a list.
fruits = ["apple", "banana", "cherry", "date"]
fruits.pop(1)  # Removes "banana"
print("\nTask 28 - After pop(1) (2nd item removed):", fruits)

# Task 29: Use del to remove an element at index 3.
numbers = [10, 20, 30, 40, 50]
del numbers[3]  # Removes item at index 3, which is 40
print("\nTask 29 - After del index 3:", numbers)

# Task 30: Use clear() to delete all elements and print the empty list.
items = ["pen", "book", "eraser"]
items.clear()
print("\nTask 30 - After clear():", items)

#Looping Through Lists (Tasks 31–35)
# Task 31: Iterate through a list and print all elements in uppercase.
fruits = ["apple", "banana", "cherry", "mango"]
print("Task 31 - Elements in uppercase:")
for fruit in fruits:
    print(fruit.upper())

# Task 32: Write a program to find and print all odd numbers in a list.
numbers = [10, 15, 22, 33, 40, 55]
print("\nTask 32 - Odd numbers in the list:")
for num in numbers:
    if num % 2 != 0:
        print(num)

# Task 33: Print the square of each number in a list using a loop.
print("\nTask 33 - Squares of each number:")
for num in numbers:
    print(f"{num}² = {num ** 2}")

# Task 34: Use enumerate() to print the index and value of each item.
print("\nTask 34 - Index and value using enumerate():")
for index, value in enumerate(fruits):
    print(f"Index {index}: {value}")

# Task 35: Count how many times the word 'apple' appears in a list using a loop.
more_fruits = ["apple", "banana", "apple", "cherry", "apple", "grape"]
count = 0
for fruit in more_fruits:
    if fruit == "apple":
        count += 1
print(f"\nTask 35 - 'apple' appears {count} times in the list.")

#Nested Lists (Tasks 36–40)
# Task 36: Create a nested list for students with name and marks (e.g., ["John", 85]).
students = [
    ["Dharun", 85],
    ["Vishwa", 90],
    ["Sugan", 78]
]
print("Task 36 - Nested student list:", students)

# Task 37: Access and print the name of the 2nd student from the nested list.
print("\nTask 37 - Name of 2nd student:", students[1][0])

# Task 38: Update the marks of the first student in a nested list.
students[0][1] = 95  # Changing John's marks from 85 to 95
print("Task 38 - Updated first student marks:", students[0])

# Task 39: Iterate over a nested list and print all names and marks neatly.
print("\nTask 39 - All students and their marks:")
for name, mark in students:
    print(f"Name: {name}, Marks: {mark}")

# Task 40: Add a new student to the nested list using append().
students.append(["David", 88])
print("\nTask 40 - List after adding a new student:", students)

#Concatenation, Repetition, Slicing (Tasks 41–45)
# Task 41: Concatenate two lists of numbers and print the result.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Task 41 - Concatenated list:", combined)

# Task 42: Repeat a list of strings 3 times using *.
words = ["hi", "bye"]
repeated = words * 3
print("\nTask 42 - Repeated list:", repeated)

# Task 43: Slice a list to get the first 3 elements.
colors = ["red", "green", "blue", "yellow", "purple"]
first_three = colors[:3]
print("\nTask 43 - First 3 elements:", first_three)

# Task 44: Slice a list to get all elements except the first and last.
middle = colors[1:-1]
print("Task 44 - All except first and last:", middle)

# Task 45: Merge a list of numbers with a list of strings and display the final list.
nums = [100, 200, 300]
labels = ["low", "medium", "high"]
merged = nums + labels
print("\nTask 45 - Merged number and string list:", merged)

#Membership & Conditional Checks (Tasks 46–50)
# Task 46: Ask the user for a fruit name and check if it exists in the list using in.
fruits = ["apple", "banana", "cherry", "grape"]
fruit_name = input("Task 46 - Enter a fruit name: ")
if fruit_name in fruits:
    print(f"{fruit_name} is in the list.")
else:
    print(f"{fruit_name} is not in the list.")

# Task 47: Remove an element only if it exists in the list.
item_to_remove = "banana"
if item_to_remove in fruits:
    fruits.remove(item_to_remove)
    print(f"\nTask 47 - '{item_to_remove}' removed. Updated list:", fruits)
else:
    print(f"\nTask 47 - '{item_to_remove}' not found in the list.")

# Task 48: Write a program that counts how many times a specific element appears.
colors = ["red", "blue", "red", "green", "red"]
count_red = 0
for color in colors:
    if color == "red":
        count_red += 1
print(f"\nTask 48 - 'red' appears {count_red} times in the list.")

# Task 49: Check if a number entered by the user exists in a list of marks.
marks = [75, 85, 90, 60, 95]
user_mark = int(input("\nTask 49 - Enter a mark to search: "))
if user_mark in marks:
    print(f"{user_mark} is present in the list.")
else:
    print(f"{user_mark} is not present in the list.")

# Task 50: Ask the user for an item and print whether it is present or not in the list.
items = ["pen", "pencil", "eraser", "sharpener"]
search_item = input("\nTask 50 - Enter an item to search: ")
if search_item in items:
    print(f"{search_item} is available in the list.")
else:
    print(f"{search_item} is not available in the list.")
