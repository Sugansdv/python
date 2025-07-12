# 18. Online Order History
# Description: Track user orders in a list.

# Initial list of past orders
order_history = [
    "Order#1001 - Shoes",
    "Order#1002 - T-shirt",
    "Order#1003 - Headphones",
    "Order#1004 - Laptop Stand",
    "Order#1005 - Coffee Mug",
    "Order#1006 - Backpack"
]

# Display current order history
print(" Order History:")
for order in order_history:
    print("-", order)

# Add new orders
order_history.append("Order#1007 - Mouse")
order_history.append("Order#1008 - Keyboard")
print("\nAdded two new orders: Mouse and Keyboard")

# Remove canceled orders
cancelled_order = "Order#1003 - Headphones"
if cancelled_order in order_history:
    order_history.remove(cancelled_order)
    print(f"Removed cancelled order: {cancelled_order}")

# Show last 5 orders using slicing
last_five_orders = order_history[-5:]
print("\n Last 5 Orders:")
for order in last_five_orders:
    print("-", order)

# Display total order count
print(f"\n Total Orders: {len(order_history)}")
