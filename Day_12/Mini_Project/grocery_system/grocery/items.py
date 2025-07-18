# Predefined list of available items
available_items = {
    "apple": 30.0,
    "banana": 10.0,
    "milk": 50.0,
    "bread": 25.0,
    "rice": 70.0
}

def list_items():
    print("\nAvailable Items:")
    for item, price in available_items.items():
        print(f"- {item.title()}: ₹{price:.2f}")
