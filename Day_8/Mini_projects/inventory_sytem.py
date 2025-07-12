# 4. Inventory System for a Shop
# Description: Manage a shop’s item inventory.

# Use list of products (each product as [name, quantity])
inventory = [
    ["apple", 10],
    ["banana", 5],
    ["milk", 8]
]

# Function to display all items using loops
def display_inventory():
    print("\nCurrent Inventory:")
    for item in inventory:
        print(f"Product: {item[0]}, Quantity: {item[1]}")

# Display initial inventory
display_inventory()

# Add a new product
inventory.append(["bread", 15])
print("\nAdded new product: bread")

# Update quantity of an existing product
product_to_update = "milk"
for item in inventory:
    if item[0] == product_to_update:
        item[1] += 5  # Add 5 more to existing quantity
        print(f"Updated quantity of {product_to_update} to {item[1]}")

# Use `in` to check if a product exists before deleting
product_to_delete = "banana"
found = False
for item in inventory:
    if item[0] == product_to_delete:
        inventory.remove(item)
        print(f"\nDeleted product: {product_to_delete}")
        found = True
        break
if not found:
    print(f"\nProduct '{product_to_delete}' not found in inventory.")

# Final inventory display
display_inventory()
