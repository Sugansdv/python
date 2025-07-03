 ## 3. Grocery List
print("========================================")
print("               Grocery List             ")
print("========================================")
# 1. Let the user input three grocery items
item1 = input("Enter first grocery item: ")
item2 = input("Enter second grocery item: ")
item3 = input("Enter third grocery item: ")

# 2. Store them in a list
grocery_list = [item1, item2, item3]

# 3. Print the items, separated by commas using sep
print("\n Your Grocery List:")
print(*grocery_list, sep=", ")

# 4. Show the type of the list variable
print(f"\n Type of grocery_list is: {type(grocery_list)}")
