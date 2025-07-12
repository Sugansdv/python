# 9. Restaurant Menu System
# Description: Dynamic menu manager.

# Use a list to store dish names and prices (nested lists: [dish_name, price])
menu = [
    ["Pizza", 250],
    ["Burger", 120],
    ["Pasta", 180],
    ["Fries", 90]
]

# Function to display the current menu
def display_menu():
    print("\n Current Menu:")
    for dish in menu:
        print(f"- {dish[0]}: ₹{dish[1]}")

# Display initial menu
display_menu()

# Add new dishes
menu.append(["Sandwich", 100])
menu.append(["Ice Cream", 80])
print("\nAdded 'Sandwich' and 'Ice Cream' to the menu.")

# Remove a sold-out item
sold_out = "Pasta"
for dish in menu:
    if dish[0] == sold_out:
        menu.remove(dish)
        print(f"Removed sold-out item: {sold_out}")
        break

# Final menu display
display_menu()
