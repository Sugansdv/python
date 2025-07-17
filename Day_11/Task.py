# 1. Create a set of favorite fruits and print it.
favorite_fruits = {"apple", "banana", "mango", "orange"}
print("Favorite Fruits Set:", favorite_fruits)

# 2. Convert a list with duplicate values into a unique set.
fruit_list = ["apple", "banana", "apple", "cherry", "banana", "mango"]
unique_fruits = set(fruit_list)
print("Unique Fruits Set:", unique_fruits)

# 3. Check if a given item exists in a set using the `in` keyword.
fruit_to_check = "mango"
if fruit_to_check in unique_fruits:
    print(f"{fruit_to_check} exists in the set.")
else:
    print(f"{fruit_to_check} does not exist in the set.")

# 4. Create a set from a string and print all unique characters.
sample_string = "hello world"
unique_chars = set(sample_string)
print("Unique characters in the string:", unique_chars)

# 5. Iterate through a set and print each element.
print("Iterating through the favorite fruits set:")
for fruit in favorite_fruits:
    print(fruit)

# 6. Create an empty set and add five movie names using add().
movies = set()
movies.add("Inception")
movies.add("The Matrix")
movies.add("Interstellar")
movies.add("The Dark Knight")
movies.add("Parasite")
print("Movie Set:", movies)

# 7. Add multiple subjects to a set using update() from a list.
subjects = {"Math", "English"}
new_subjects = ["Science", "History", "Computer"]
subjects.update(new_subjects)
print("Subjects Set:", subjects)

# 8. Add multiple letters from a string into a set using update().
letters = set()
letters.update("hello")
print("Letters Set from 'hello':", letters)
# 9. Remove a specific city from a set using remove().
cities = {"New York", "London", "Paris", "Tokyo"}
cities.remove("Paris")  # Will raise KeyError if "Paris" not found
print("Cities after removing 'Paris':", cities)

# 10. Try to remove an element using discard() and avoid an error if not present.
cities.discard("Berlin")  # No error even if "Berlin" is not in the set
print("Cities after trying to discard 'Berlin':", cities)

# 11. Remove a random item from a set using pop() and print it.
removed_city = cities.pop()
print("Randomly removed city:", removed_city)
print("Cities after pop():", cities)

# 12. Clear all elements from a set using clear() and check if it is empty.
cities.clear()
print("Cities after clear():", cities)
print("Is the set empty?", len(cities) == 0)

# 13. Find the union of two sets of programming languages.
languages1 = {"Python", "Java", "C++"}
languages2 = {"Ruby", "JavaScript", "Python"}
all_languages = languages1.union(languages2)
print("Union of languages:", all_languages)

# 14. Find the intersection of two sets of sports.
sports1 = {"Cricket", "Football", "Tennis"}
sports2 = {"Tennis", "Basketball", "Football"}
common_sports = sports1.intersection(sports2)
print("Common sports (intersection):", common_sports)

# 15. Find the difference between set A and set B (A - B).
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
diff_A_B = A.difference(B)
print("Difference (A - B):", diff_A_B)

# 16. Find the symmetric difference (items in either set, but not both).
sym_diff = A.symmetric_difference(B)
print("Symmetric Difference:", sym_diff)

# 17. Perform chained operations like (A | B) - (A & B) on two sets.
result = (A | B) - (A & B)  # Same as symmetric difference
print("Chained operation (A | B) - (A & B):", result)

# 18. Check if a set of backend skills is a subset of full-stack skills.
backend_skills = {"Python", "Django"}
fullstack_skills = {"HTML", "CSS", "JavaScript", "Python", "Django", "React"}
print("Is backend a subset of full-stack?", backend_skills.issubset(fullstack_skills))

# 19. Verify if a set of developers is a superset of testers.
developers = {"Alice", "Bob", "Charlie", "David"}
testers = {"Bob", "Charlie"}
print("Are developers a superset of testers?", developers.issuperset(testers))

# 20. Determine if two sets of colors are disjoint (no common elements).
primary_colors = {"red", "blue", "yellow"}
secondary_colors = {"green", "orange", "purple"}
print("Are primary and secondary colors disjoint?", primary_colors.isdisjoint(secondary_colors))

# 21. Use multiple sets to test all subset-superset combinations.
setA = {1, 2}
setB = {1, 2, 3}
setC = {4, 5}

print("A ⊆ B:", setA.issubset(setB))        # True
print("B ⊇ A:", setB.issuperset(setA))     # True
print("A ⊆ C:", setA.issubset(setC))       # False
print("B ⊇ C:", setB.issuperset(setC))     # False
print("A and C disjoint?", setA.isdisjoint(setC))  # True

# 22. Real-life case of issubset(): Required courses completion check.
required_courses = {"Math", "English", "Computer Science"}
student_courses = {"English", "Math", "Computer Science", "Physics"}

has_completed_requirements = required_courses.issubset(student_courses)
print("Has the student completed all required courses?", has_completed_requirements)

# 23. Create a backup of a set using copy() and show that modifying the copy doesn’t affect the original.
original_set = {"apple", "banana", "cherry"}
backup_set = original_set.copy()  # Create a shallow copy

# Modify the copied set
backup_set.add("mango")
backup_set.remove("banana")

# Print both sets
print("Original Set:", original_set)
print("Modified Copy:", backup_set)

# Demonstrate that the original is unchanged
print("Is original set unchanged?", original_set == {"apple", "banana", "cherry"})

# 24. Create a frozenset of vowels and demonstrate immutability.
vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
print("Frozen Set of Vowels:", vowels)

# Trying to modify it directly will raise an error
# vowels.add('y')  #  Not allowed

# 25. Try to add an element to a frozenset and catch the error gracefully.
try:
    vowels.add('y')  # This will raise an AttributeError
except AttributeError as e:
    print("Error caught:", e)

# 26. Use a frozenset as a key in a dictionary for caching purposes.
# Frozenset is hashable so it can be used as a key
cache = {}
params = frozenset(["user_id", "timestamp", "auth_token"])
cache[params] = "Cached Response"

print("Cache Dictionary:", cache)
print("Access using frozenset key:", cache[params])

# 27. Generate a set of even numbers from 1 to 20 using set comprehension.
even_numbers = {x for x in range(1, 21) if x % 2 == 0}
print("Even numbers (1 to 20):", even_numbers)

# 28. Generate a set of unique lowercase characters from a sentence using set comprehension.
sentence = "Set Comprehension is Powerful!"
lowercase_chars = {ch for ch in sentence.lower() if ch.isalpha()}
print("Unique lowercase letters:", lowercase_chars)

# 29. Create a set of squares for numbers 1 to 10 using set comprehension.
squares = {x ** 2 for x in range(1, 11)}
print("Squares from 1 to 10:", squares)

# 30. Use a set comprehension to filter out vowels from a sentence.
text = "Python is an amazing language!"
vowels = {'a', 'e', 'i', 'o', 'u'}
consonants = {ch for ch in text.lower() if ch.isalpha() and ch not in vowels}
print("Consonants in sentence:", consonants)

# 31. Find allowed users using set difference.
registered_users = {"alice", "bob", "charlie", "david"}
blocked_users = {"bob", "david"}
allowed_users = registered_users - blocked_users
print("Allowed Users:", allowed_users)

# 32. Students enrolled in both Python and Java (intersection).
python_students = {"john", "lisa", "derek", "nina"}
java_students = {"nina", "lisa", "mike"}
common_students = python_students & java_students
print("Students in both Python and Java:", common_students)

# 33. New stock listings (difference).
previous_stocks = {"AAPL", "GOOGL", "AMZN", "TSLA"}
current_stocks = {"AAPL", "GOOGL", "AMZN", "TSLA", "NFLX", "NVDA"}
new_listings = current_stocks - previous_stocks
print("New Stock Listings:", new_listings)

# 34. Users logged in either yesterday or today (union).
yesterday_logins = {"anna", "bob", "carla"}
today_logins = {"carla", "daniel", "eric"}
active_users = yesterday_logins | today_logins
print("Users who logged in either day:", active_users)

# 35. Users who changed passwords on only one day (symmetric difference).
day1 = {"user1", "user2", "user3"}
day2 = {"user2", "user4"}
changed_once = day1 ^ day2
print("Changed password on only one day:", changed_once)

# 36. Detect duplicate product SKUs in a list.
product_skus = ["sku101", "sku102", "sku103", "sku101", "sku104", "sku102"]
duplicates = {sku for sku in product_skus if product_skus.count(sku) > 1}
print("Duplicate SKUs:", duplicates)

# 37. Create a set from a CSV column and count unique entries.
# Simulating with list of names instead of reading a real CSV file.
csv_names_column = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Diana"]
unique_names = set(csv_names_column)
print("Unique names count:", len(unique_names))

# 38. Unique tag manager system for blog posts.
tags_post1 = {"react", "web", "frontend"}
tags_post2 = {"python", "backend", "web"}
all_tags = tags_post1 | tags_post2
print("All unique tags:", all_tags)

# 39. Check if required permissions are covered by default permissions.
required_permissions = {"read", "write"}
default_permissions = {"read", "write", "execute"}
is_covered = required_permissions.issubset(default_permissions)
print("Permissions covered?", is_covered)
import random

# 40. Create two sets from random numbers and apply all operations.
set1 = set(random.sample(range(1, 20), 10))
set2 = set(random.sample(range(10, 30), 10))
print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# 41. Contact manager that stores unique email addresses.
emails = set()
emails.update(["alice@example.com", "bob@example.com", "alice@example.com", "carol@example.com"])
print("Unique emails:", emails)

# 42. Check which players earned all major trophies.
required_trophies = {"World Cup", "Champions League", "Ballon d'Or"}
player_achievements = {
    "Messi": {"Champions League", "Ballon d'Or", "World Cup"},
    "Ronaldo": {"Champions League", "Ballon d'Or"},
    "Mbappe": {"World Cup"}
}
for player, trophies in player_achievements.items():
    print(f"{player} has all trophies?", required_trophies.issubset(trophies))

# 43. Track unique IPs from a server log.
server_log = ["192.168.0.1", "10.0.0.5", "192.168.0.1", "172.16.0.2", "10.0.0.5"]
unique_ips = set(server_log)
print("Unique IPs:", unique_ips)

# 44. Extract unique hashtags from a list of tweets.
tweets = [
    "Learning Python is fun! #python #coding",
    "Explore data with #pandas and #python!",
    "#AI and #ML are the future. #python",
]
hashtags = set()
for tweet in tweets:
    hashtags.update({word for word in tweet.split() if word.startswith("#")})
print("Unique Hashtags:", hashtags)

# 45. Track unique book titles from multiple libraries using update().
library1 = {"1984", "To Kill a Mockingbird", "Pride and Prejudice"}
library2 = {"Pride and Prejudice", "The Great Gatsby", "Moby Dick"}
library3 = {"War and Peace", "1984", "The Catcher in the Rye"}
all_books = set()
all_books.update(library1, library2, library3)
print("All Unique Book Titles:", all_books)

# 46. Validate if all required modules are installed.
required_modules = {"numpy", "pandas", "matplotlib"}
installed_modules = {"numpy", "pandas", "matplotlib", "seaborn"}
print("All required modules installed?", required_modules.issubset(installed_modules))
import string

# 47. Try removing a non-existent item using remove() and handle the exception.
colors = {"red", "blue", "green"}
try:
    colors.remove("yellow")  # Will raise KeyError
except KeyError as e:
    print("Tried to remove 'yellow':", e)

# 48. Explain the difference between remove() and discard() using a test set.
test_set = {"apple", "banana", "cherry"}
# discard() – no error if item not found
test_set.discard("mango")  #  Safe, no error
print("After discard('mango'):", test_set)

# remove() – throws error if item not found
try:
    test_set.remove("mango")  #  Raises KeyError
except KeyError:
    print("remove('mango') caused KeyError")

# 49. Create a set from a list with mixed datatypes and remove all integers using set comprehension.
mixed_list = [1, "apple", 3.14, "banana", 42, "cherry", 100]
mixed_set = set(mixed_list)
non_integers = {item for item in mixed_set if not isinstance(item, int)}
print("Set without integers:", non_integers)

# 50. Create a set of characters from a multiline text, excluding punctuation.
multiline_text = """
Python is amazing.
Sets are powerful!
Use them wisely...
"""
clean_chars = {char.lower() for char in multiline_text if char.isalpha()}
print("Unique letters (no punctuation):", clean_chars)
