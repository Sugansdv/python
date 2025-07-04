# 🪪 Identity Operators Tasks (27–30)

# Task 27: Compare two identical lists using is and print if they refer to the same memory.
print(" Task 27: Compare Identical Lists Using is")
list1 = [1, 2, 3]
list2 = list1  # Both point to same object
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list1 is list2  →  {list1 is list2}") 

# Task 28: Compare two different but equal lists using is not.
print("\n Task 28: Compare Equal but Separate Lists Using is not")
list3 = [1, 2, 3]
list4 = [1, 2, 3]
print(f"list3 == list4  →  {list3 == list4}")  
print(f"list3 is not list4  →  {list3 is not list4}")  

# Task 29: Show that a = b means both a is b is True (same memory) only for non-mutable objects.
print("\n Task 29: Identity with Non-Mutable Objects (Integers)")
a = 100
b = 100
print(f"a = {a}, b = {b}")
print(f"a is b  →  {a is b}") 

print("\n🔹 Mutable Example")
x = [10]
y = [10]
print(f"x == y  →  {x == y}")      
print(f"x is y  →  {x is y}")     

# Task 30: Create three variables, two referencing the same list and one different, compare using is, is not.
print("\n🔹 Task 30: Three List Variables Identity Comparison")
a = [1, 2, 3]
b = a          
c = [1, 2, 3]    

print(f"a is b  →  {a is b}")       
print(f"a is c  →  {a is c}")      
print(f"b is not c  →  {b is not c}")

