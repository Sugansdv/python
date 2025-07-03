## 15. Shopping Cart
print("========================================")
print("             Shopping Cart              ")
print("========================================")

# 1. Ask the user to input item names and their prices (3 items)
item1 = input("Enter name of Item 1: ")
price1 = float(input(f"Enter price of {item1}: ₹"))

item2 = input("\nEnter name of Item 2: ")
price2 = float(input(f"Enter price of {item2}: ₹"))

item3 = input("\nEnter name of Item 3: ")
price3 = float(input(f"Enter price of {item3}: ₹"))

# 2. Store items and prices in a dictionary
cart = {
    item1: price1,
    item2: price2,
    item3: price3
}

# 3. Calculate total amount
total = sum(cart.values())

# 4. Print the items and total using f-string
print("\n Cart Summary:")
for item, price in cart.items():
    print(f"{item}: ₹{price:.2f}")

print(f"\n Total Amount: ₹{total:.2f}")
