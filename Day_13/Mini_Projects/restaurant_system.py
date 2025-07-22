# Class: MenuItem
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Class: Order (composition of MenuItems)
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)
        print(f"Added: {item.name} - ₹{item.price}")

    def remove_item(self, item_name):
        for i, item in enumerate(self.items):
            if item.name.lower() == item_name.lower():
                removed = self.items.pop(i)
                print(f"Removed: {removed.name}")
                return
        print(f"Item '{item_name}' not found in order.")

    def get_total(self):
        return sum(item.price for item in self.items)

    def show_order(self):
        print("\n--- Order Summary ---")
        for item in self.items:
            print(f"{item.name} - ₹{item.price}")
        print(f"Subtotal: ₹{self.get_total()}\n")

# Class: Bill
class Bill:
    tax_rate = 0.05  # Class variable for 5% tax

    @classmethod
    def set_tax_rate(cls, rate):
        cls.tax_rate = rate

    @staticmethod
    def calculate_tax(amount):
        return round(amount * Bill.tax_rate, 2)

    @staticmethod
    def generate(order: Order):
        subtotal = order.get_total()
        tax = Bill.calculate_tax(subtotal)
        total = round(subtotal + tax, 2)
        print("--- Final Bill ---")
        print(f"Subtotal: ₹{subtotal}")
        print(f"Tax (@{int(Bill.tax_rate*100)}%): ₹{tax}")
        print(f"Total: ₹{total}")
        return total

# Class: Customer
class Customer:
    def __init__(self, name):
        self.name = name
        self.order = Order()

    def place_order(self, menu):
        print(f"\nWelcome {self.name}, place your order:")
        for i, item in enumerate(menu, 1):
            print(f"{i}. {item.name} - ₹{item.price}")
        while True:
            choice = input("Enter item number to add (or 'done'): ")
            if choice.lower() == 'done':
                break
            if choice.isdigit() and 1 <= int(choice) <= len(menu):
                self.order.add_item(menu[int(choice) - 1])
            else:
                print("Invalid choice.")

    def remove_item_from_order(self):
        item = input("Enter item name to remove: ")
        self.order.remove_item(item)

    def print_bill(self):
        self.order.show_order()
        Bill.generate(self.order)


# Example Run
if __name__ == "__main__":
    # Create menu
    menu = [
        MenuItem("Pizza", 250),
        MenuItem("Burger", 120),
        MenuItem("Pasta", 180),
        MenuItem("Coke", 50)
    ]

    # Create a customer
    cust = Customer("Sneha")

    # Place order
    cust.place_order(menu)

    # Optional: remove item
    remove = input("Do you want to remove any item? (yes/no): ")
    if remove.lower() == "yes":
        cust.remove_item_from_order()

    # Print final bill
    cust.print_bill()
