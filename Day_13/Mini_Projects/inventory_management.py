# Item Class
class Item:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def update(self, quantity=None, price=None):
        if quantity is not None:
            self.quantity = quantity
        if price is not None:
            self.price = price

    def __str__(self):
        return f"[{self.item_id}] {self.name} - Qty: {self.quantity}, Price: ₹{self.price}"

# Supplier Class with Encapsulation
class Supplier:
    def __init__(self, name, contact):
        self.__name = name
        self.__contact = contact

    def get_info(self):
        return f"Supplier: {self.__name}, Contact: {self.__contact}"

# Inventory Class
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.item_id in self.items:
            print(f"Item ID {item.item_id} already exists. Use update.")
        else:
            self.items[item.item_id] = item
            print(f"Added: {item.name}")

    def update_item(self, item_id, quantity=None, price=None):
        if item_id in self.items:
            self.items[item_id].update(quantity, price)
            print(f"Updated: {self.items[item_id]}")
        else:
            print(f"Item ID {item_id} not found.")

    def remove_item(self, item_id):
        if item_id in self.items:
            removed = self.items.pop(item_id)
            print(f"Removed: {removed.name}")
        else:
            print(f"Item ID {item_id} not found.")

    def __contains__(self, item_name):
        return any(item.name.lower() == item_name.lower() for item in self.items.values())

    def __getitem__(self, item_id):
        return self.items.get(item_id, None)

    def display_items(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            for item in self.items.values():
                print(item)

# --- Sample Usage ---
if __name__ == "__main__":
    # Create Inventory and Supplier
    inv = Inventory()
    supplier = Supplier("FreshMart Supplies", "+91-9876543210")

    # Add Items
    inv.add_item(Item(101, "Apples", 50, 120))
    inv.add_item(Item(102, "Bananas", 100, 60))

    # Update Item
    inv.update_item(101, quantity=75)

    # Check item by name (dunder __contains__)
    print("\nIs 'Bananas' in inventory?", "Bananas" in inv)

    # Get item by ID (dunder __getitem__)
    print("Item 102 details:", inv[102])

    # Display all items
    print("\nCurrent Inventory:")
    inv.display_items()

    # Remove item
    inv.remove_item(101)

    # Secure Supplier Info
    print("\nSupplier Info:")
    print(supplier.get_info())
