# 18. Flight Booking System
# Description: Manage passenger bookings for flights.
# Requirements:
# - {flight_id: {"route": ..., "passengers": [...]} }
# - Add/remove passengers
# - Check seat availability
# - Use .setdefault() to auto-create flights

flights = {
    "AI101": {"route": "Chennai → Delhi", "passengers": ["Alice", "Bob"]},
    "AI202": {"route": "Mumbai → Bangalore", "passengers": ["Charlie"]}
}

MAX_SEATS = 5

def add_passenger(flight_id, passenger):
    flight = flights.setdefault(flight_id, {"route": "Unknown", "passengers": []})
    if len(flight["passengers"]) < MAX_SEATS:
        if passenger not in flight["passengers"]:
            flight["passengers"].append(passenger)
            print(f"{passenger} booked on flight {flight_id}.")
        else:
            print(f"{passenger} is already booked on flight {flight_id}.")
    else:
        print(f"Flight {flight_id} is full.")

def remove_passenger(flight_id, passenger):
    if flight_id in flights and passenger in flights[flight_id]["passengers"]:
        flights[flight_id]["passengers"].remove(passenger)
        print(f"{passenger} removed from flight {flight_id}.")
    else:
        print(f"{passenger} not found on flight {flight_id}.")

def check_availability(flight_id):
    if flight_id in flights:
        available = MAX_SEATS - len(flights[flight_id]["passengers"])
        print(f"Flight {flight_id} has {available} seat(s) available.")
    else:
        print(f"Flight {flight_id} not found.")

add_passenger("AI101", "David")
add_passenger("AI303", "Eve")
remove_passenger("AI202", "Charlie")
remove_passenger("AI101", "Zoe")
check_availability("AI101")
check_availability("AI303")
