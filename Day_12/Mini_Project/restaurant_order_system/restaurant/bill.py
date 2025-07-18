def calculate_bill(order):
    subtotal = sum(price * qty for _, price, qty in order)
    tax = round(subtotal * 0.18, 2)
    total = subtotal + tax
    return subtotal, tax, total

def print_bill(order_id, order, subtotal, tax, total):
    print("\n===  Bill Summary ===")
    print(f"Order ID: {order_id}")
    for item, price, qty in order:
        print(f"{item:<10} x{qty:<3} @ ₹{price:<5} = ₹{price*qty}")
    print(f"{'-'*30}")
    print(f"{'Subtotal':<20}: ₹{subtotal}")
    print(f"{'Tax (18%)':<20}: ₹{tax}")
    print(f"{'Total':<20}: ₹{total}")
