import os
from datetime import datetime

INVOICE_DIR = "invoices"

# Ensure invoice folder exists
def ensure_directory():
    if not os.path.exists(INVOICE_DIR):
        os.makedirs(INVOICE_DIR)

# Generate a formatted invoice
def generate_invoice(customer_name, items, invoice_id):
    ensure_directory()

    filename = os.path.join(INVOICE_DIR, f"invoice_{invoice_id}.txt")
    total_amount = sum(price * qty for _, qty, price in items)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(filename, "w") as f:
            f.write(f"Invoice ID: {invoice_id}\n")
            f.write(f"Date: {now}\n")
            f.write(f"Customer: {customer_name}\n")
            f.write("-" * 40 + "\n")
            f.write(f"{'Item':<15}{'Qty':<5}{'Rate':<10}{'Amount':<10}\n")
            f.write("-" * 40 + "\n")

            for item, qty, price in items:
                amount = qty * price
                f.write(f"{item:<15}{qty:<5}{price:<10.2f}{amount:<10.2f}\n")

            f.write("-" * 40 + "\n")
            f.write(f"{'Total':>35}: {total_amount:.2f}\n")
            f.write("-" * 40 + "\n")

        print(f" Invoice saved as: {filename}")
    except Exception as e:
        print(" Error writing invoice:", e)

def get_invoice_id():
    existing = os.listdir(INVOICE_DIR) if os.path.exists(INVOICE_DIR) else []
    ids = [int(f.split("_")[1].split(".")[0]) for f in existing if f.startswith("invoice_")]
    return max(ids, default=0) + 1

def main():
    print("=== Invoice Generator ===")
    customer = input("Customer name: ").strip()
    items = []

    while True:
        item = input("Enter item name (or 'done' to finish): ").strip()
        if item.lower() == "done":
            break
        try:
            qty = int(input("Quantity: "))
            price = float(input("Rate: "))
            items.append((item, qty, price))
        except ValueError:
            print(" Invalid quantity or rate. Try again.")

    if items:
        invoice_id = get_invoice_id()
        generate_invoice(customer, items, invoice_id)
    else:
        print(" No items entered. Invoice not created.")

if __name__ == "__main__":
    main()
