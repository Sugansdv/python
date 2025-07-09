# 14. Shopping Cart Input App
# Objective: Enter product names into cart.

cart = []

# • Use infinite while True loop.
while True:
    product = input(" Enter product name (or type 'done' to finish): ").strip()

    # • User types product name or “done” to stop.
    if product.lower() == "done":
        break

    # • Use continue to skip empty input.
    if product == "":
        print(" Product name cannot be empty.")
        continue

    cart.append(product)
    print(f" '{product}' added to cart.")

# • Print product list in else.
else:
    print(" Unexpected loop exit.") 

print("\n Your Shopping Cart:")
for i, item in enumerate(cart, start=1):
    print(f"{i}. {item}")
