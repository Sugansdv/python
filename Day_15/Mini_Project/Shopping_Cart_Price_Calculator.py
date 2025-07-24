class ProductExistsError(Exception):
    pass

def shopping_cart():
    cart = {}
    total = 0.0

    try:
        while True:
            product = input("Enter product name (or 'done' to finish): ").strip().lower()
            if product == "done":
                break
            if product in cart:
                raise ProductExistsError(f" Product '{product}' already exists in cart.")
            
            try:
                price = float(input(f"Enter price for {product}: "))
                if price < 0:
                    raise ValueError(" Price cannot be negative.")
                cart[product] = price
            except ValueError as ve:
                print(ve)

    except ProductExistsError as pe:
        print(pe)

    finally:
        total = sum(cart.values())
        print(f"\n Cart Summary ({len(cart)} items):")
        for p, pr in cart.items():
            print(f" - {p}: ₹{pr}")
        print(f"Total: ₹{total:.2f}")

if __name__ == "__main__":
    shopping_cart()
