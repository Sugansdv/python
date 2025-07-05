# Grocery Basket Price Calculator

# Use dictionary: item → price
grocery_items = {
    "Rice": 120,
    "Wheat": 90,
    "Sugar": 45,
    "Milk": 60,
    "Eggs": 70,
    "Oil": 150,
    "Bread": 40,
    "Butter": 80,
    "Fruits": 100,
    "Vegetables": 75
}

# Input: list of selected items 
print("Available items:")
for item in grocery_items:
    print(f"- {item} (₹{grocery_items[item]})")

selected_items = input("\nEnter the items you want to buy (comma-separated): ").split(",")
selected_items = [item.strip().title() for item in selected_items] 

# Use for loop to sum prices
total_price = 0
for item in selected_items:
    if item in grocery_items:
        total_price += grocery_items[item]
    else:
        print(f"Item '{item}' not available in store.")

# If user buys more than 5 items → apply ₹50 off
if len(selected_items) > 5:
    discount = 50
    total_price -= discount
    offer_applied = True
else:
    discount = 0
    offer_applied = False

# Display final bill
print("\n====== Grocery Basket Bill ======")
print(f"Items Purchased     : {selected_items}")
print(f"Total Before Offer  : ₹{total_price + discount}")
if offer_applied:
    print(f"Offer Applied       : -₹{discount}")
print(f"Final Amount to Pay : ₹{total_price}")
print("=================================")
