from modules.sale_ops import add_sale
from modules.report_ops import generate_report

products = {
    "P1001": {"name": "Phone", "price": 500},
    "P1002": {"name": "Laptop", "price": 1000},
    "P1003": {"name": "Headphones", "price": 150}
}

sales = []
buyers = set()

def main():
    print("🛒 Digital Flash Sale System")

    while True:
        print("\nMenu:")
        print("1. Make a Sale")
        print("2. Generate Report")
        print("3. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_sale(products, sales, buyers)
        elif choice == "2":
            generate_report(sales)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
