def add_item(inventory, categories, suppliers):
    item = input("Item Name: ").strip().lower()
    if item in inventory:
        print("Item already exists. Use update.")
        return

    try:
        qty = int(input("Quantity: "))
        price = float(input("Price: "))
    except ValueError:
        print("Invalid quantity or price.")
        return

    category = input("Category: ").strip().lower()
    supplier = input("Supplier: ").strip().title()

    inventory[item] = (qty, price, category, supplier)
    categories.add(category)
    suppliers.add(supplier)
    print("Item added.")

def remove_item(inventory):
    item = input("Item to remove: ").strip().lower()
    if item in inventory:
        del inventory[item]
        print("Item removed.")
    else:
        print("Item not found.")

def update_stock(inventory):
    item = input("Item to update: ").strip().lower()
    if item not in inventory:
        print("Item not found.")
        return

    try:
        qty = int(input("New Quantity: "))
        price = float(input("New Price: "))
    except ValueError:
        print("Invalid quantity or price.")
        return

    category, supplier = inventory[item][2], inventory[item][3]
    inventory[item] = (qty, price, category, supplier)
    print("Stock updated.")

def list_by_category(inventory):
    cat = input("Enter category: ").strip().lower()
    found = False
    for item, (qty, price, category, _) in inventory.items():
        if category == cat:
            print(f"{item} - Qty: {qty}, Price: {price}")
            found = True
    if not found:
        print("No items in this category.")

def restock_alerts(inventory, threshold=5):
    print("\nRestock Alerts:")
    found = False
    for item, (qty, _, _, _) in inventory.items():
        if qty <= threshold:
            print(f"{item} - Quantity: {qty}")
            found = True
    if not found:
        print("All items well stocked.")
