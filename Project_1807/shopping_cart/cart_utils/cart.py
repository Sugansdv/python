

def add_to_cart(cart, item_id, name, price, category):
    if item_id in cart:
        print(f"Item {item_id} already in cart. Increasing quantity.")
        cart[item_id]["quantity"] += 1
    else:
        cart[item_id] = {
            "name": name,
            "price": price,
            "category": category,
            "quantity": 1
        }

def remove_from_cart(cart, item_id):
    if item_id in cart:
        del cart[item_id]
        print(f"Item {item_id} removed from cart.")
    else:
        print("Item not found in cart.")

def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return

    total = 0
    categories = set()

    print("Your Shopping Cart:")
    print("-" * 40)
    for item_id, details in cart.items():
        print(f"ID: {item_id}, Name: {details['name']}, "
              f"Price: ₹{details['price']}, Qty: {details['quantity']}, "
              f"Category: {details['category']}")
        total += details['price'] * details['quantity']
        categories.add(details['category'])
    print("-" * 40)
    print(f"Total: ₹{total}")
    print(f"Categories in Cart: {', '.join(categories)}")
