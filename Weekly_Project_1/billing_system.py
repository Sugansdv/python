# Mini Billing System

# Use dictionary: item → price.
items_price = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5,
    "Eraser": 3,
    "Scale": 15,
    "Bag": 600,
    "Water Bottle": 150,
    "Lunch Box": 250
}

# Use list to take user’s selected items.
selected_items = ["Notebook", "Bag", "Pen", "Water Bottle"]

# Use for loop to calculate total.
total = 0
for item in selected_items:
    if item in items_price:
        total += items_price[item]

# If total > 1000 → apply 10% discount.
if total > 1000:
    discount = total * 0.10
    total -= discount
    discount_applied = True
else:
    discount = 0
    discount_applied = False
    
# Use variables, list, dict, float to display result
print("\n========= Mini Billing System =========")
print(f"Selected Items : {selected_items}")
print(f"Total (before discount): ₹{total + discount:.2f}")
if discount_applied:
    print(f"Discount Applied (10%) : ₹{discount:.2f}")
print(f"Final Amount to Pay    : ₹{total:.2f}")
print("=======================================")
