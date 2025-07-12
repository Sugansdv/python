# 1. Grocery Cart System
# Description: Build a program to manage a user’s shopping cart.

cart = []

# Add items using append()
cart.append("apple")
cart.append("bread")
cart.append("milk")

# Add multiple items using extend()
cart.extend(["eggs", "banana", "apple"])  # Intentionally added a duplicate "apple"

# Display items using for loop
print("Items in the cart:")
for item in cart:
    print("-", item)

# Remove items using remove() or pop()
if "bread" in cart:
    cart.remove("bread")  # Remove by value
print("\nRemoved 'bread' from cart.")

removed_item = cart.pop()  # Removes last item ("apple")
print(f"Removed last item using pop(): {removed_item}")

# Show total count using len()
print("\nTotal items in cart:", len(cart))

# Check for duplicates
print("\nChecking for duplicates:")
unique_items = set()
duplicates = set()
for item in cart:
    if item in unique_items:
        duplicates.add(item)
    else:
        unique_items.add(item)

if duplicates:
    print("Duplicate items found:", list(duplicates))
else:
    print("No duplicates found.")

# Use slicing to show first 3 items in the cart
print("\nFirst 3 items in cart:", cart[:3])

