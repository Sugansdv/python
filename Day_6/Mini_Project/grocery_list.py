#  4. Grocery List Manager

# • Use global for the inventory list
inventory = {}

# • Use **kwargs to add items (item=quantity)
def add_items(**kwargs):
    global inventory
    for item, qty in kwargs.items():
        inventory[item] = inventory.get(item, 0) + qty
    print("Items added to inventory.")

# • Create a function to calculate total items
def total_items():
    return sum(inventory.values())

# • Return all items sorted alphabetically
def get_sorted_items():
    return sorted(inventory.items())

add_items(apple=3, banana=5, mango=2)
print("Total items:", total_items())
print("Sorted inventory:", get_sorted_items())
