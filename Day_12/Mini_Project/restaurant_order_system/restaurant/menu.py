menu_items = {
    1: ("Burger", 120),
    2: ("Pizza", 250),
    3: ("Pasta", 180),
    4: ("Fries", 100),
    5: ("Coke", 40)
}

def show_menu():
    print("\n--- Menu ---")
    for item_no, (name, price) in menu_items.items():
        print(f"{item_no}. {name} - ₹{price}")
