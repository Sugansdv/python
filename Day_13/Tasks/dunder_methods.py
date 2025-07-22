# 36. Override __add__ for Vector class
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# 37. Override __len__ for Playlist class
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

# 38. Override __getitem__ and __setitem__ for ShoppingCart
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def __getitem__(self, key):
        return self.items.get(key, 0)

    def __setitem__(self, key, value):
        self.items[key] = value

# 39. Override __contains__ for Inventory class
class Inventory:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item.lower() in (i.lower() for i in self.items)

# 40. Money class with __eq__, __gt__, __lt__
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __lt__(self, other):
        return self.amount < other.amount


# ==============================
# Run Dunder Method Examples
# ==============================
if __name__ == "__main__":
    print("TASK 36: Vector Addition with __add__")
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)
    print("v1 + v2 =", v1 + v2)

    print("\nTASK 37: Playlist Length with __len__")
    my_playlist = Playlist(["Song A", "Song B", "Song C"])
    print("Total songs:", len(my_playlist))

    print("\nTASK 38: ShoppingCart __getitem__ and __setitem__")
    cart = ShoppingCart()
    cart["apple"] = 4
    cart["banana"] = 2
    print("Apples in cart:", cart["apple"])
    print("Bananas in cart:", cart["banana"])

    print("\nTASK 39: Inventory with __contains__")
    stock = Inventory(["Keyboard", "Mouse", "Monitor"])
    print("Is 'mouse' in stock?", "mouse" in stock)
    print("Is 'laptop' in stock?", "laptop" in stock)

    print("\nTASK 40: Money Comparison with __eq__, __gt__, __lt__")
    m1 = Money(500)
    m2 = Money(700)
    print("m1 == m2:", m1 == m2)
    print("m1 < m2:", m1 < m2)
    print("m1 > m2:", m1 > m2)
