from .items import items

def add_to_cart(cart, item):
    if item in items:
        cart.append(item)
        return f"Added {item}"
    return f"{item} not found"
