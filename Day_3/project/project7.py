
print("=======================================")
print("          Product Discount System            ")
print("=======================================\n")

# Input: Product name, price, discount %
product_name = input("Enter product name: ")
price = float(input("Enter product price (₹): "))
discount_percent = float(input("Enter discount percentage (%): "))

# Arithmetic and assignment operator to apply discount
discount_amount = price * (discount_percent / 100)
price -= discount_amount  

# Display result using f-string
print("\n========== Final Bill ==========")
print(f"Product Name      : {product_name}")
print(f"Discount Applied  : {discount_percent}%")
print(f"Final Price (₹)   : ₹{price:.2f}")
print("=================================")
