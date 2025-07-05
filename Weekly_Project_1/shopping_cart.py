# Simple Shopping Cart

# Use a dictionary for products and price
products = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5,
    "Eraser": 3,
    "Scale": 15,
    "Bag": 500,
    "Water Bottle": 120
}

# User selected list
selected_items = ["Notebook", "Pen", "Bag"]

# Use loop to calculate total
total = 0
for item in selected_items:
    if item in products:
        total += products[item]

# Print total bill
print("\n======= Shopping Cart Summary =======")
print(f"Items Purchased : {selected_items}")
print(f"Total Bill      : ₹{total}")
print("=====================================")
