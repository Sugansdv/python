# 9. Restaurant Menu Display System
# Goal: Store menu items and prices.
# Requirements:
# • Menu item as tuple: (item_id, item_name, price)
# • Store multiple tuples in a list.
# • Use for loop to display formatted menu.
# • Find expensive item using max() and a lambda.
# • Enforce immutability to prevent price tampering.

# List of menu items
menu = [
    (1, "Pasta", 250.0),
    (2, "Pizza", 400.0),
    (3, "Burger", 180.0),
    (4, "Fries", 120.0),
    (5, "Steak", 750.0)
]

# Display formatted menu
print("Restaurant Menu:\n")
for item_id, item_name, price in menu:
    print(f"{item_id}. {item_name:<10} - ₹{price:.2f}")

# Find the most expensive item
most_expensive = max(menu, key=lambda item: item[2])
print(f"\n Most Expensive Item: {most_expensive[1]} (₹{most_expensive[2]:.2f})")
