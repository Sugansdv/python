def generate_report(sales):
    if not sales:
        print("No sales yet.")
        return

    print("\n🧾 Sales Report:")
    for code, buyer, qty, time, total in sales:
        print(f"{time} | {buyer} bought {qty} x {code} → ₹{total:.2f}")

    print(f"\nTotal Transactions: {len(sales)}")
