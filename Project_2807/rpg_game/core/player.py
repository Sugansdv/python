class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage. Health: {self.health}")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} healed {amount} HP. Health: {self.health}")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"Added {item} to inventory.")

    def display_inventory(self):
        print("Inventory:", ", ".join(self.inventory) or "Empty")
