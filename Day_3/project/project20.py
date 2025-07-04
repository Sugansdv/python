
print("=======================================")
print("          E-commerce Checkout System          ")
print("=======================================\n")

# Input: product price and quantity
price = float(input("Enter product price (₹): "))
quantity = int(input("Enter quantity: "))

# Predefined discount codes with percentages
discount_codes = {
    "SAVE10": 10,
    "SAVE20": 20,
    "FESTIVE30": 30
}

# Input: discount code
code = input("Enter discount code (or press Enter to skip): ").upper()

# Initial total calculation
total = price * quantity  # Arithmetic operator

# Check discount code and apply if valid
if code in discount_codes:  # membership operator
    discount_percent = discount_codes[code]
    discount_amount = total * (discount_percent / 100)
    total -= discount_amount  # Assignment operator
    print(f"\n Discount '{code}' applied ({discount_percent}% off).")
    print(f" You saved ₹{discount_amount:.2f}")
else:
    print("\n No valid discount code applied.")

# Final formatted output
print("\n========== Checkout Summary ==========")
print(f"Price per Item  : ₹{price}")
print(f"Quantity        : {quantity}")
print(f"Final Total     : ₹{total:.2f}")
print("=======================================")
