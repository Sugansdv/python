# Simple Discount Engine

# Input: product price
price = float(input("Enter the product price: ₹"))

# Use if-elif-else to apply discount
# 2000: 20% off, >1000: 10%, else: No discount
if price == 2000:
    discount = price * 0.20
elif price > 1000:
    discount = price * 0.10
else:
    discount = 0

final_price = price - discount

# Print result
print("\n========== Discount Summary ==========")
print(f"Original Price  : ₹{price:.2f}")
print(f"Discount Applied: ₹{discount:.2f}")
print(f"Final Price     : ₹{final_price:.2f}")
print("======================================")
