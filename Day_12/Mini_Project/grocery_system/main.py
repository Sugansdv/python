from grocery.items import list_items
from grocery.cart import ShoppingCart
from grocery.checkout import generate_bill

def main():
    cart = ShoppingCart()

    while True:
        print("\n--- Grocery Shopping ---")
        print("1. List Items")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        try:
            if choice == "1":
                list_items()
            elif choice == "2":
                name = input("Item name: ")
                qty = int(input("Quantity: "))
                cart.add_item(name, qty)
                print(f"{qty} x {name} added to cart.")
            elif choice == "3":
                name = input("Item name to remove: ")
                cart.remove_item(name)
                print(f"{name} removed from cart.")
            elif choice == "4":
                cart.view_cart()
            elif choice == "5":
                generate_bill(cart.get_cart_data())
                break
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid option.")
        except Exception as e:
            print(f" Error: {e}")

if __name__ == "__main__":
    main()
