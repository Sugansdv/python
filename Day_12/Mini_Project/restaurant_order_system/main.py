from restaurant.menu import show_menu
from restaurant.order import take_order
from restaurant.bill import calculate_bill, print_bill
from restaurant.offers import apply_offers

def main():
    print(" Welcome to the Restaurant Order System")
    show_menu()
    order_id, order = take_order()
    if not order:
        print("No items ordered.")
        return
    order = apply_offers(order)
    subtotal, tax, total = calculate_bill(order)
    print_bill(order_id, order, subtotal, tax, total)

if __name__ == "__main__":
    main()
