# inventory_ops.py

devices = {}  # {(device_id, model): {'type': str, 'brand': str, 'year': int}}
brands = set()  # to track unique brands


def add_device(device_id, model, dev_type, brand, year):
    key = (device_id, model)
    if key in devices:
        print("Device already exists.")
        return

    devices[key] = {
        'type': dev_type,
        'brand': brand,
        'year': year
    }
    brands.add(brand)
    print(f"Device {model} added.")


def list_devices():
    if not devices:
        print("No devices found.")
        return

    for key, details in devices.items():
        print(f"ID: {key[0]}, Model: {key[1]}, Type: {details['type']}, Brand: {details['brand']}, Year: {details['year']}")


def list_brands():
    print("Available Brands:", ", ".join(brands))
