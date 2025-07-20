from core.cart import add_to_cart, remove_from_cart, checkout
from core.store import products
from core.discounts import apply_discount

cart = []

def main():
    while True:
        print("\nShopping Cart Menu")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            for pid, (name, price, stock) in products.items():
                print(f"{pid}: {name} - Rs.{price} (Stock: {stock})")

        elif choice == "2":
            pid = input("Enter Product ID: ").strip()
            qty = int(input("Enter quantity: "))
            add_to_cart(cart, pid, qty)

        elif choice == "3":
            pid = input("Enter Product ID to remove: ").strip()
            remove_from_cart(cart, pid)

        elif choice == "4":
            total = checkout(cart, products)
            discounted = apply_discount(total)
            print(f"Total: Rs.{total:.2f}")
            print(f"After Discount: Rs.{discounted:.2f}")
            break

        elif choice == "5":
            print("Exiting shopping cart.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
