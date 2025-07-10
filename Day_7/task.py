#Creating and Accessing Strings (1–10)
# 1. Create a string using single quotes, double quotes, and triple quotes
s1 = 'Hello'
s2 = "World"
s3 = '''Python'''
print(s1, s2, s3)

# 2. Create a multiline quote using triple quotes and print it
multiline = '''This is a
multiline string
using triple quotes.'''
print(multiline)

# 3. Access the first and last characters from a string using positive and negative indexing
text = "Programming"
print("First character:", text[0])
print("Last character:", text[-1])

# 4. Write a program to print every character in a string using a for loop
word = "Python"
for char in word:
    print(char)

# 5. Slice a string to extract only the middle 3 characters
s = "Learning"
mid_index = len(s) // 2
middle_chars = s[mid_index - 1:mid_index + 2]
print("Middle 3 characters:", middle_chars)

# 6. Access and print every second character from a string using slicing
s = "Technology"
print("Every second character:", s[::2])

# 7. Print all vowels in a given string using indexing and conditions
input_str = "Beautiful Day"
vowels = "aeiouAEIOU"
for ch in input_str:
    if ch in vowels:
        print(ch, end=' ')
print()

# 8. Extract the domain from an email like "user@gmail.com" using slicing
email = "user@gmail.com"
domain = email[email.index("@")+1:]
print("Domain:", domain)

# 9. Check whether the first and last characters of a string are the same
s = "radar"
if s[0] == s[-1]:
    print("First and last characters are the same.")
else:
    print("First and last characters are different.")

# 10. Print the reverse of a string using slicing
original = "Python"
reversed_str = original[::-1]
print("Reversed string:", reversed_str)

#SECTION 2: Immutability and Modification (11–15)
# 11. Try to modify a single character in a string (to understand immutability)
s = "hello"
# s[0] = 'H'  # This will raise an error: strings are immutable
# TypeError: 'str' object does not support item assignment

# 12. Write code to change the first character of a string using slicing and concatenation
s = "hello"
s_modified = 'H' + s[1:]
print("Modified string:", s_modified)

# 13. Replace a character in the middle of a string by reconstructing it
s = "python"
mid_index = len(s) // 2
s_replaced = s[:mid_index] + 'X' + s[mid_index+1:]
print("After replacing middle character:", s_replaced)

# 14. Create a function that replaces all vowels in a string with '*'
def replace_vowels_with_star(s):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in s:
        if ch in vowels:
            result += '*'
        else:
            result += ch
    return result

print("Replaced vowels:", replace_vowels_with_star("Beautiful Day"))

# 15. Create a function that returns a new string by replacing all occurrences of 'a' with '@'
def replace_a_with_at(s):
    return s.replace('a', '@')

print("After replacing 'a' with '@':", replace_a_with_at("Have a great day"))

#SECTION 3: Deleting and Updating Strings (16–20)
# 11. Try to modify a single character in a string (to understand immutability)
s = "hello"
# s[0] = 'H'  # This will raise an error: strings are immutable
# Uncommenting the above line will cause: TypeError: 'str' object does not support item assignment

# 12. Write code to change the first character of a string using slicing and concatenation
s = "hello"
s_modified = 'H' + s[1:]
print("Modified string:", s_modified)

# 13. Replace a character in the middle of a string by reconstructing it
s = "python"
mid_index = len(s) // 2
s_replaced = s[:mid_index] + 'X' + s[mid_index+1:]
print("After replacing middle character:", s_replaced)

# 14. Create a function that replaces all vowels in a string with '*'
def replace_vowels_with_star(s):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in s:
        if ch in vowels:
            result += '*'
        else:
            result += ch
    return result

print("Replaced vowels:", replace_vowels_with_star("Beautiful Day"))

# 15. Create a function that returns a new string by replacing all occurrences of 'a' with '@'
def replace_a_with_at(s):
    return s.replace('a', '@')

print("After replacing 'a' with '@':", replace_a_with_at("Have a great day"))

#SECTION 4: Common String Methods (21–35)
# 21. Use len() to count the characters in a string
text = "Hello World"
print("Length of string:", len(text))

# 22. Convert a string to lowercase using .lower()
print("Lowercase:", text.lower())

# 23. Convert a string to uppercase using .upper()
print("Uppercase:", text.upper())

# 24. Remove leading and trailing whitespaces using .strip()
msg = "   Hello Python   "
print("Stripped string:", msg.strip())

# 25. Use .replace() to change "bad" to "good" in a sentence
sentence = "This is a bad example."
print("Modified sentence:", sentence.replace("bad", "good"))

# 26. Split a comma-separated string into a list using .split(',')
csv = "apple,banana,grape"
fruits = csv.split(',')
print("List:", fruits)

# 27. Join a list of words with - using .join()
words = ['Python', 'is', 'fun']
joined = '-'.join(words)
print("Joined string:", joined)

# 28. Count how many times "a" appears in "banana" using .count()
word = "banana"
print("Count of 'a':", word.count('a'))

# 29. Use .find() to get the first index of the letter 'o' in "Google"
print("First index of 'o':", "Google".find('o'))

# 30. Create a program to convert 'Python is FUN' to 'python-is-fun'
text = "Python is FUN"
converted = text.lower().replace(" ", "-")
print("Converted string:", converted)

# 31. Write a function that counts vowels and consonants in a string
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v = c = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return v, c

v, c = count_vowels_consonants("Python is Fun!")
print("Vowels:", v, "Consonants:", c)

# 32. Use .replace() to remove all spaces from a string
s = "Python is powerful"
print("No spaces:", s.replace(" ", ""))

# 33. Use .split() and a for loop to print each word on a new line
s = "Split this sentence into words"
for word in s.split():
    print(word)

# 34. Print the middle character of a string (if odd length)
s = "Python"
if len(s) % 2 != 0:
    mid_char = s[len(s)//2]
    print("Middle character:", mid_char)
else:
    print("String has even length")

# 35. Write a function that returns the first and last characters combined
def first_last_combined(s):
    if len(s) >= 2:
        return s[0] + s[-1]
    elif len(s) == 1:
        return s[0] * 2
    else:
        return ""

print("Combined first and last:", first_last_combined("hello"))

#SECTION 5: Concatenation and Repetition (36–40)
# 36. Concatenate first name and last name with a space in between
first_name = "Dharun"
last_name = "Vishwa"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# 37. Write a program that asks for a name and prints it 3 times using *
name = input("Enter your name: ")
print(name * 3)

# 38. Create a sentence by joining five different words using +
word1 = "Learning"
word2 = "Python"
word3 = "is"
word4 = "fun"
word5 = "everyday"
sentence = word1 + " " + word2 + " " + word3 + " " + word4 + " " + word5 + "."
print("Sentence:", sentence)

# 39. Use .join() to combine a list of characters into a word
chars = ['H', 'e', 'l', 'l', 'o']
word = ''.join(chars)
print("Combined word:", word)

# 40. Take user input for a name and print “Welcome <name>” using string concatenation
user_name = input("Enter your name: ")
print("Welcome " + user_name)

#SECTION 6: String Formatting (41–50)
# 41. Use f-string to print “My name is John and I am 30 years old.”
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")

# 42. Use .format() to insert 2 numbers and print their sum
a = 10
b = 20
print("The sum of {} and {} is {}".format(a, b, a + b))

# 43. Use % formatting to display the price of a product: "%s costs ₹%.2f"
product = "Pen"
price = 15.5
print("%s costs ₹%.2f" % (product, price))

# 44. Create a function that takes name and marks and prints a result using all 3 formatting methods
def print_result(name, marks):
    # f-string
    print(f"{name} scored {marks} marks.")
    # .format()
    print("{} scored {} marks.".format(name, marks))
    # % formatting
    print("%s scored %d marks." % (name, marks))

print_result("Alice", 92)

# 45. Format a list of products and their prices into a formatted table using f-strings
products = [("Pen", 10), ("Notebook", 45.5), ("Pencil", 5)]
print("Product     | Price")
print("---------------------")
for p, price in products:
    print(f"{p:<10} | ₹{price:>6.2f}")

# 46. Ask for user input (name, age) and print using .format()
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello {}, you are {} years old.".format(name, age))

# 47. Print temperature conversion: "Temperature is 35°C or 95°F" using f-string
celsius = 35
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature is {celsius}°C or {fahrenheit}°F")

# 48. Format a sentence where the price changes dynamically: "The discounted price is ₹999"
price = 999
print(f"The discounted price is ₹{price}")

# 49. Write a function that accepts employee details and formats them using f-string
def employee_info(name, role, salary):
    print(f"Employee: {name}, Role: {role}, Salary: ₹{salary:.2f}")

employee_info("Dharun", "Manager", 75000)

# 50. Create a dynamic weather report sentence using all formatting styles
def weather_report(city, temp_c, condition):
    # f-string
    f_style = f"Weather in {city}: {temp_c}°C, {condition}"
    # .format()
    format_style = "Weather in {}: {}°C, {}".format(city, temp_c, condition)
    # % formatting
    percent_style = "Weather in %s: %d°C, %s" % (city, temp_c, condition)
    
    print("F-string:", f_style)
    print(".format():", format_style)
    print("% formatting:", percent_style)

weather_report("Chennai", 36, "Sunny")
