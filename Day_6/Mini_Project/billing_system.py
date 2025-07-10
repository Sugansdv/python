#  1. Billing System

# • Use global variable to maintain the total bill
total = 0  # Global variable to track total bill

# • Add items with price
# • Use *args to allow multiple item prices
def add_items(*args):
    global total
    print("Items added:")
    for price in args:
        print(f"Item price: ₹{price}")
        total += price  # Add each price to global total

# • Calculate total using a function
def get_total():
    return total  # Return the current total bill

# • Apply discount with a function
def apply_discount(percent):
    global total
    discount_amount = total * (percent / 100)
    total -= discount_amount
    return round(total, 2)  # Return final bill after discount

# ------------------ Demonstration ------------------
add_items(100, 250, 75)  # Add multiple items
print("Total before discount: ₹", get_total())
print("Total after 10% discount: ₹", apply_discount(10))
