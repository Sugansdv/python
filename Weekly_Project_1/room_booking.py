# Simple Hotel Room Booking

# Use dictionary: room type → price per night
room_prices = {
    "Standard": 1000,
    "Deluxe": 2000,
    "Suite": 3000
}

# Input: room type and number of nights
print("Available room types: Standard, Deluxe, Suite")
room_type = input("Enter room type: ").strip().title()
nights = int(input("Enter number of nights: "))

# Check if room type is valid
if room_type in room_prices:
    price_per_night = room_prices[room_type]
    total = price_per_night * nights

    # If nights > 3, give 10% off
    if nights > 3:
        discount = total * 0.10
        total -= discount
        discount_applied = True
    else:
        discount = 0
        discount_applied = False

    print("\n========= Booking Summary =========")
    print(f"Room Type      : {room_type}")
    print(f"Price per Night: ₹{price_per_night}")
    print(f"Nights Stayed  : {nights}")
    if discount_applied:
        print(f"Discount (10%) : -₹{discount:.2f}")
    print(f"Total Amount   : ₹{total:.2f}")
    print("===================================")
else:
    print("Invalid room type selected.")
