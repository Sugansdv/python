# 5. Product Inventory System
# Goal: Store product details using tuples.
# Requirements:
# • Each product: (product_id, name, price, in_stock)
# • Use tuple operations to find total inventory value.
# • Filter products using for loop and conditions.
# • Sort products by price using sorted().
# • Print reports with unpacked tuple values.

# List of products
products = [
    (101, "Laptop", 55000.0, True),
    (102, "Mouse", 500.0, True),
    (103, "Keyboard", 1200.0, False),
    (104, "Monitor", 8000.0, True),
    (105, "Printer", 6500.0, False)
]

# Total inventory value (only in-stock)
total_value = sum(price for _, _, price, in_stock in products if in_stock)
print(f" Total Inventory Value (In-Stock): ₹{total_value:.2f}\n")

# Filter and print in-stock products
print(" In-Stock Products:")
for product in products:
    product_id, name, price, in_stock = product
    if in_stock:
        print(f"{product_id}: {name} - ₹{price:.2f}")

# Sort by price and display
sorted_by_price = sorted(products, key=lambda p: p[2])
print("\n Products Sorted by Price:")
for product_id, name, price, in_stock in sorted_by_price:
    print(f"{product_id}: {name} - ₹{price:.2f} ({'In Stock' if in_stock else 'Out of Stock'})")
