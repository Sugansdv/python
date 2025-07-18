
from inventory import inventory_ops as inv

def main():
    inv.add_device("101", "XPS 13", "Laptop", "Dell", 2022)
    inv.add_device("102", "MacBook Pro", "Laptop", "Apple", 2021)
    inv.add_device("103", "iPhone 14", "Smartphone", "Apple", 2023)

    print("\nAll Devices:")
    inv.list_devices()

    print("\nUnique Brands:")
    inv.list_brands()


if __name__ == "__main__":
    main()
