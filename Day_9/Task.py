# 🔹 1. Tuple Basics
# Task 1.	Create an empty tuple and print its type.
t1 = ()
print(type(t1))

# Task 2.	Create a tuple with integers, strings, and a float and print each item.
t2 = (10, "Hello", 3.14)
for item in t2:
    print(item)

# Task 3.	Create a tuple with only one element and print its type.
t3 = (5,)
print(type(t3))

# Task 4.	Convert a list of numbers [1, 2, 3, 4, 5] to a tuple.
lst = [1, 2, 3, 4, 5]
t4 = tuple(lst)
print(t4)

# Task 5.	Convert the string "Python" into a tuple of characters.
t5 = tuple("Python")
print(t5)

# 🔹 2. Tuple Indexing and Slicing
# Task 6.	Access the first and last elements of a tuple.
t6 = (1, 2, 3, 4, 5)
print(t6[0], t6[-1])

# Task 7.	Slice a tuple to get the middle 3 elements.
t7 = (1, 2, 3, 4, 5)
print(t7[1:4])

# Task 8.	Reverse a tuple using slicing.
t8 = (1, 2, 3, 4, 5)
print(t8[::-1])

# Task 9.	Access every second element from a tuple using slicing.
t9 = (1, 2, 3, 4, 5, 6)
print(t9[::2])

# Task 10.	Get a sub-tuple using negative indexing and slicing.
t10 = (1, 2, 3, 4, 5, 6)
print(t10[-4:-1])

# 🔹 3. Tuple Immutability
# Task 11.	Attempt to change a tuple element and handle the resulting error.
try:
    t11 = (1, 2, 3)
    t11[0] = 10
except TypeError as e:
    print(e)

# Task 12.	Show how to replace a value in a tuple by converting it to a list and back.
t12 = (1, 2, 3)
lst12 = list(t12)
lst12[1] = 20
t12 = tuple(lst12)
print(t12)

# Task 13.	Add a new value to a tuple (simulate by tuple concatenation).
t13 = (1, 2, 3)
t13 = t13 + (4,)
print(t13)

# Task 14.	Remove an item from a tuple (simulate by list conversion).
t14 = (1, 2, 3)
lst14 = list(t14)
lst14.remove(2)
t14 = tuple(lst14)
print(t14)

# Task 15.	Demonstrate that tuples cannot be deleted partially (e.g., del tuple[0]).
try:
    t15 = (1, 2, 3)
    del t15[0]
except TypeError as e:
    print(e)

# 🔹 4. Tuple Operations
# Task 16.	Concatenate two tuples.
t16a = (1, 2)
t16b = (3, 4)
print(t16a + t16b)

# Task 17.	Repeat a tuple 3 times using the * operator.
t17 = (1, 2)
print(t17 * 3)

# Task 18.	Check if an item exists in a tuple using in.
t18 = (1, 2, 3)
print(2 in t18)

# Task 19.	Find the length of a tuple using len().
t19 = (1, 2, 3, 4)
print(len(t19))

# Task 20.	Count the number of times an element occurs in a tuple.
t20 = (1, 2, 2, 3, 2)
print(t20.count(2))

# 🔹 5. Tuple Functions and Methods
# Task 21.	Use the count() method to count element occurrences.
t21 = (1, 2, 2, 3)
print(t21.count(2))

# Task 22.	Use the index() method to find the position of an item.
t22 = (10, 20, 30)
print(t22.index(20))

# Task 23.	Use max() and min() on a tuple of numbers.
t23 = (5, 10, 3, 8)
print(max(t23), min(t23))

# Task 24.	Use sum() to find the total of tuple items.
t24 = (1, 2, 3, 4)
print(sum(t24))

# Task 25.	Sort a tuple using sorted() (returns a list).
t25 = (5, 2, 9, 1)
print(sorted(t25))

# 🔹 6. Iteration and Looping with Tuples
# Task 26.	Iterate over a tuple using a for loop and print all elements.
t26 = (1, 2, 3)
for i in t26:
    print(i)

# Task 27.	Iterate with enumerate() to print index and value.
t27 = ('a', 'b', 'c')
for index, value in enumerate(t27):
    print(index, value)

# Task 28.	Use a while loop to iterate through a tuple.
t28 = (10, 20, 30)
i = 0
while i < len(t28):
    print(t28[i])
    i += 1

# Task 29.	Print all even numbers from a tuple.
t29 = (1, 2, 4, 5, 6)
for i in t29:
    if i % 2 == 0:
        print(i)

# Task 30.	Count how many strings start with “A” in a tuple of names.
t30 = ("Alice", "Bob", "Andrew", "Eve")
count = sum(1 for name in t30 if name.startswith("A"))
print(count)

# 🔹 7. Nested Tuples
# Task 31.	Create a tuple of tuples and access inner elements.
t31 = ((1, 2), (3, 4))
print(t31[1][0])

# Task 32.	Print all sub-tuples from a nested tuple.
t32 = ((1, 2), (3, 4), (5, 6))
for sub in t32:
    print(sub)

# Task 33.	Sum all numbers from a tuple of tuples like ((1,2), (3,4)).
t33 = ((1, 2), (3, 4))
total = sum(sum(sub) for sub in t33)
print(total)

# Task 34.	Flatten a nested tuple of integers using a loop.
t34 = ((1, 2), (3, 4), (5, 6))
flat = []
for sub in t34:
    flat.extend(sub)
print(tuple(flat))

# Task 35.	Access the second element of the third sub-tuple.
t35 = ((1, 2), (3, 4), (5, 6))
print(t35[2][1])

# 🔹 8. Tuple Packing and Unpacking
# Task 36.	Pack multiple values into a tuple and print.
t36 = 1, "Hello", 3.14
print(t36)

# Task 37.	Unpack a tuple into individual variables.
a, b, c = (10, 20, 30)
print(a, b, c)

# Task 38.	Use unpacking to swap two variables.
x, y = 5, 10
x, y = y, x
print(x, y)

# Task 39.	Use * to unpack remaining values from a tuple.
a, *b = (1, 2, 3, 4)
print(a, b)

# Task 40.	Unpack nested tuples into individual values.
((a1, b1), (a2, b2)) = ((1, 2), (3, 4))
print(a1, b1, a2, b2)

# 🔹 9. Tuple Use in Functions
# Task 41.	Write a function that returns multiple values as a tuple.
def stats():
    return 10, 20, 30
print(stats())

# Task 42.	Pass a tuple as an argument to a function and print elements.
def show(t):
    for i in t:
        print(i)
show((1, 2, 3))

# Task 43.	Write a function to calculate average of numbers using tuple input.
def average(t):
    return sum(t) / len(t)
print(average((10, 20, 30)))

# Task 44.	Return both min and max from a tuple using a function.
def min_max(t):
    return min(t), max(t)
print(min_max((5, 2, 9, 1)))

# Task 45.	Write a function to merge two tuples.
def merge(t1, t2):
    return t1 + t2
print(merge((1, 2), (3, 4)))

# 🔹 10. Real-Life Tuple Applications
# Task 46.	Store coordinates (latitude, longitude) as tuples and display them.
location = (12.9716, 77.5946)
print("Coordinates:", location)

# Task 47.	Create a phone book with names and numbers stored as tuples in a list.
phone_book = [("Alice", "1234"), ("Bob", "5678")]
for name, number in phone_book:
    print(f"{name}: {number}")

# Task 48.	Represent RGB values of an image pixel using a tuple.
rgb = (255, 0, 128)
print("RGB:", rgb)

# Task 49.	Store exam results (student_name, score) as tuples and print top scorer.
results = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
top = max(results, key=lambda x: x[1])
print("Top Scorer:", top)

# Task 50.	Use a tuple to represent an immutable configuration (host, port, debug_mode).
config = ("localhost", 8080, False)
print("Configuration:", config)
