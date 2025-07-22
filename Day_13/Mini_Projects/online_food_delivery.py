from abc import ABC, abstractmethod

# ----------------- User & Customer -----------------
class User:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class Customer(User):
    def __init__(self, name, contact, address):
        super().__init__(name, contact)
        self.address = address

# ----------------- Restaurant -----------------
class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu  # dictionary {item: price}

    def show_menu(self):
        print(f"\n--- Menu at {self.name} ---")
        for item, price in self.menu.items():
            print(f"{item}: ₹{price}")

# ----------------- Order -----------------
class Order:
    def __init__(self, customer, restaurant, items):
        self.customer = customer
        self.restaurant = restaurant
        self.items = items  # list of items
        self.total = sum(restaurant.menu[item] for item in items)
        self.delivery = None

    def assign_delivery(self, delivery):
        self.delivery = delivery

    def show_summary(self):
        print(f"\n Order Summary for {self.customer.name}:")
        print(f"Restaurant: {self.restaurant.name}")
        print(f"Items: {', '.join(self.items)}")
        print(f"Total: ₹{self.total}")
        if self.delivery:
            print(f"Delivery Mode: {self.delivery.mode()}")
            print(f"Delivery Address: {self.customer.address}")
        print("---------------------------")

# ----------------- Delivery (Polymorphic) -----------------
class Delivery(ABC):
    @abstractmethod
    def mode(self):
        pass

class BikeDelivery(Delivery):
    def mode(self):
        return "Bike Delivery"

class DroneDelivery(Delivery):
    def mode(self):
        return "Drone Delivery"

# ----------------- Test Flow -----------------
if __name__ == "__main__":
    # Create Customer
    c1 = Customer("Ravi", "9876543210", "Chennai")

    # Create Restaurant
    r1 = Restaurant("Spicy Bites", {"Pizza": 250, "Burger": 120, "Fries": 80})
    r1.show_menu()

    # Place Order
    o1 = Order(c1, r1, ["Pizza", "Fries"])

    # Assign Delivery
    delivery_mode = DroneDelivery()
    o1.assign_delivery(delivery_mode)

    # Show Order
    o1.show_summary()
