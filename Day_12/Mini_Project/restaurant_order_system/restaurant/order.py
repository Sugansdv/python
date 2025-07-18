import random
from .menu import menu_items

def take_order():
    order = []
    order_id = random.randint(1000, 9999)
    print(f"\n🧾 Order ID: {order_id}")
    while True:
        try:
            item_no = int(input("Enter item number (0 to finish): "))
            if item_no == 0:
                break
            if item_no in menu_items:
                qty = int(input(f"Enter quantity for {menu_items[item_no][0]}: "))
                order.append((menu_items[item_no][0], menu_items[item_no][1], qty))
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")
    return order_id, order
