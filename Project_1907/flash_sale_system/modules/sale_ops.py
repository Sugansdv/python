from datetime import datetime

def add_sale(products, sales, buyers):
    code = input("Enter product code: ").strip()
    if code not in products:
        print("❌ Invalid product code.")
        return

    buyer = input("Enter buyer name: ").strip().title()
    try:
        qty = int(input("Enter quantity: ").strip())
    except ValueError:
        print("❌ Quantity must be a number.")
        return

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    price = products[code]["price"]
    if qty >= 3:
        discount = 0.1
        print("🎉 10% discount applied!")
    else:
        discount = 0.0

    total = qty * price * (1 - discount)
    sales.append((code, buyer, qty, time, total))
    buyers.add(buyer)
    print(f"✅ Sale added for {products[code]['name']}. Total: ₹{total:.2f}")
