# 10. Inventory Management System
# Description: Track store inventory levels.
# Requirements:
# - {item_name: {"stock": ..., "min_required": ..., "supplier": ...}}
# - Alert items below minimum
# - Add new items using setdefault()
# - Delete discontinued items
# - Export low-stock items using dictionary comprehension

inventory = {
    "Apples": {"stock": 50, "min_required": 30, "supplier": "FreshFarms"},
    "Oranges": {"stock": 20, "min_required": 25, "supplier": "CitrusCo"},
    "Bananas": {"stock": 15, "min_required": 20, "supplier": "TropicFruits"}
}

def alert_low_stock():
    print("\nLow Stock Alerts:")
    for item, info in inventory.items():
        if info["stock"] < info["min_required"]:
            print(f"{item}: Stock = {info['stock']}, Minimum Required = {info['min_required']}")

def add_item(name, stock, min_required, supplier):
    inventory.setdefault(name, {"stock": stock, "min_required": min_required, "supplier": supplier})
    print(f"Item '{name}' added (if not already present).")

def delete_item(name):
    if name in inventory:
        del inventory[name]
        print(f"Item '{name}' deleted from inventory.")
    else:
        print(f"Item '{name}' not found.")

def export_low_stock_items():
    low_stock = {
        item: info for item, info in inventory.items()
        if info["stock"] < info["min_required"]
    }
    print("\nExported Low Stock Items:")
    for item, info in low_stock.items():
        print(f"{item}: {info}")

add_item("Tomatoes", 40, 35, "VeggieSupply")
add_item("Apples", 100, 30, "FreshFarms")  
delete_item("Bananas")
alert_low_stock()
export_low_stock_items()
