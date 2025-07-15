# 7. E-commerce Order Tracker
# Goal: Manage orders in an e-commerce system.
# Requirements:
# • Store orders as (order_id, customer_name, (item1, item2, item3))
# • Use tuple nesting to represent items in each order.
# • Iterate through orders to generate a report.
# • Display all items using nested loop and unpacking.
# • Prevent accidental changes in the order items.

orders = [
    (101, "Alice", ("Laptop", "Mouse", "Keyboard")),
    (102, "Bob", ("Smartphone", "Charger", "Case")),
    (103, "Charlie", ("Book", "Pen", "Notebook")),
    (104, "David", ("Tablet", "Cover", "Stylus"))
]

# Generate report
print(" E-commerce Order Report:\n")

for order_id, customer_name, items in orders:
    print(f"Order ID: {order_id}")
    print(f"Customer: {customer_name}")
    print("Items:")
    for item in items:
        print(f"  - {item}")
    print("-" * 30)
