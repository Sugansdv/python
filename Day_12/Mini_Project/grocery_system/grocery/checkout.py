import json
import random
from datetime import datetime
from grocery.items import available_items

def generate_bill(cart_data):
    if not cart_data:
        print("Cart is empty. Cannot checkout.")
        return

    bill_id = random.randint(10000, 99999)
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total = sum(available_items[item] * qty for item, qty in cart_data.items())

    bill = {
        "bill_id": bill_id,
        "date_time": time,
        "items": [
            {"name": item, "quantity": qty, "price": available_items[item], "subtotal": available_items[item]*qty}
            for item, qty in cart_data.items()
        ],
        "total_amount": total
    }

    filename = f"bill_{bill_id}.json"
    with open(filename, "w") as f:
        json.dump(bill, f, indent=4)

    print(f"\n Bill ID: {bill_id}")
    print(f"Date: {time}")
    print("Items Purchased:")
    for i in bill['items']:
        print(f"- {i['name'].title()} x {i['quantity']} = ₹{i['subtotal']:.2f}")
    print(f"\nTotal Amount: ₹{total:.2f}")
    print(f"\n Bill saved as '{filename}'")
