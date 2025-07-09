#  11. Meal Ordering System
# Objective: Simulate food order entry.

orders = []

# • Use while loop to add items.
while True:
    item = input(" Enter food item (or type 'done' to finish): ").strip()

    # • Use break when user types "done".
    if item.lower() == "done":
        break

    # • Skip empty entries using continue.
    if item == "":
        print(" Item cannot be empty. Try again.")
        continue

    orders.append(item)
    print(f" '{item}' added to your order.")

# • At the end, use else to print total items ordered.
else:
    print(" Ordering loop exited unexpectedly.")  # This won't run unless while has no break

# Show final order summary
print("\n Order Summary:")
for i, item in enumerate(orders, start=1):
    print(f"{i}. {item}")

print(f"\n🍴 Total items ordered: {len(orders)}")
