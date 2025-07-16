# 2. Online Shopping Cart
# Description: Simulate a shopping cart for an online store.
# Requirements:
# - Cart format: {item_name: {"quantity": x, "price": y}}
# - Add, update, or remove items
# - Calculate total bill
# - Remove out-of-stock items using pop()
# - Show highest value item
# - Apply .values() and .items() for bill summary
# - Use nested dictionaries and in keyword

cart = {
    "apple": {"quantity": 2, "price": 50},
    "banana": {"quantity": 5, "price": 10}
}

def add_item(item, qty, price):
    if item in cart:
        cart[item]["quantity"] += qty
    else:
        cart[item] = {"quantity": qty, "price": price}

def remove_item(item):
    cart.pop(item, None)

def calculate_total():
    return sum(item["quantity"] * item["price"] for item in cart.values())

def remove_out_of_stock():
    for item in list(cart):
        if cart[item]["quantity"] == 0:
            cart.pop(item)

def highest_value_item():
    return max(cart.items(), key=lambda x: x[1]["quantity"] * x[1]["price"])

