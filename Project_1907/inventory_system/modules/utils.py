def unique_suppliers(suppliers):
    print("\nUnique Suppliers:")
    for s in sorted(suppliers):
        print(f"- {s}")
    if not suppliers:
        print("No suppliers yet.")
