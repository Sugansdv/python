class Product:
    def __init__(self, name, price, product_id):
        self.name = name
        self.price = price
        self.product_id = product_id

    def __str__(self):
        return f"{self.name} - ₹{self.price}"

    def __eq__(self, other):
        return self.product_id == other.product_id


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        if product in self.items:
            self.items.remove(product)

    def __contains__(self, product):
        return product in self.items

    def __getitem__(self, index):
        return self.items[index]

    def __add__(self, product):
        self.add_item(product)
        return self

    def total_price(self, discount=0):
        total = sum(item.price for item in self.items)
        tax = self.calculate_tax(total)
        return total + tax - discount

    @staticmethod
    def calculate_tax(amount):
        return round(amount * 0.18, 2)  # 18% GST


class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def __str__(self):
        return f"User: {self.name}"


class Order:
    def __init__(self, user):
        self.user = user
        self.items = user.cart.items
        self.total = user.cart.total_price()

    def summary(self):
        print(f"Order for {self.user.name}")
        for item in self.items:
            print(f" - {item}")
        print(f"Total with tax: ₹{self.total}")


# ----------- Demo ----------
if __name__ == "__main__":
    # Create products
    p1 = Product("Laptop", 50000, 101)
    p2 = Product("Mouse", 1500, 102)
    p3 = Product("Keyboard", 2500, 103)

    # Create user
    user1 = User("Amit")

    # Add products to cart
    user1.cart + p1
    user1.cart + p2

    # Remove item
    user1.cart.remove_item(p2)

    # Check if item in cart
    print("Keyboard in cart?", p3 in user1.cart)

    # Add another product
    user1.cart + p3

    # View cart items
    for idx in range(len(user1.cart.items)):
        print(f"Item {idx + 1}: {user1.cart[idx]}")

    # Place order
    order = Order(user1)
    order.summary()
