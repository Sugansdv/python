from core.store import products

def add_to_cart(cart, product_id, quantity):
    if product_id not in products:
        print("Product not found.")
        return
    name, price, stock = products[product_id]
    if stock < quantity:
        print("Not enough stock.")
        return
    cart.append((product_id, quantity))
    products[product_id] = (name, price, stock - quantity)
    print(f"Added {quantity} x {name} to cart.")

def remove_from_cart(cart, product_id):
    for item in cart:
        if item[0] == product_id:
            cart.remove(item)
            name, price, stock = products[product_id]
            products[product_id] = (name, price, stock + item[1])
            print(f"Removed {item[1]} x {name} from cart.")
            return
    print("Item not found in cart.")

def checkout(cart, products):
    total = 0
    unique_items = set()
    print("\n--- Bill ---")
    for product_id, qty in cart:
        name, price, _ = products[product_id]
        total += price * qty
        unique_items.add(product_id)
        print(f"{name} x {qty} = Rs.{price * qty:.2f}")
    print(f"Items Bought: {', '.join(unique_items)}")
    return total
