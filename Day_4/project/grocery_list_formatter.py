# ==== MINI PROJECT 1: GROCERY LIST FORMATTER ====

print("====================")
print("Grocery List Formatter")
print("====================")

# 1: •	Accept a list of grocery items (e.g., milk, eggs, rice).
grocery_items = input("Enter grocery items separated by commas: ").split(',')

# 2: Remove extra spaces and format list
grocery_items = [item.strip().capitalize() for item in grocery_items]

# 3: Print each item with a serial number (starting from 1). Use enumerate() with start=1.
print("\nYour Grocery List:")
for index, item in enumerate(grocery_items, start=1):
    print(f"{index}. {item}")
