from grocery.items import available_items

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, name, quantity):
        name = name.lower()
        if name not in available_items:
            raise ValueError(f"{name} is not available.")
        self.cart[name] = self.cart.get(name, 0) + quantity

    def remove_item(self, name):
        name = name.lower()
        if name in self.cart:
            del self.cart[name]
        else:
            raise ValueError(f"{name} not found in cart.")

    def view_cart(self):
        if not self.cart:
            print("🛒 Your cart is empty.")
        else:
            print("\n🛒 Your Cart:")
            for item, qty in self.cart.items():
                price = available_items[item]
                print(f"{item.title()} x {qty} = ₹{price * qty:.2f}")

    def get_cart_data(self):
        return self.cart
