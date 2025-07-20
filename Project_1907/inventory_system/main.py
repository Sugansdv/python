from modules.inventory_ops import (
    add_item, remove_item, update_stock,
    list_by_category, restock_alerts
)
from modules.utils import unique_suppliers

inventory = {}  # item: (quantity, price, category, supplier)
categories = set()
suppliers = set()

def main():
    print("Welcome to Simple Inventory System")

    while True:
        print("\nMenu:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Stock")
        print("4. List Items by Category")
        print("5. Restock Alerts")
        print("6. View Unique Suppliers")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_item(inventory, categories, suppliers)
        elif choice == "2":
            remove_item(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            list_by_category(inventory)
        elif choice == "5":
            restock_alerts(inventory)
        elif choice == "6":
            unique_suppliers(suppliers)
        elif choice == "7":
            print("Exiting Inventory System.")
            break
        else:
            print("Invalid option.")
            
if __name__ == "__main__":
    main()
