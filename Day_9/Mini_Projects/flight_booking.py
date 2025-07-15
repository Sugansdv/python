# 11. Flight Booking System
# Goal: Manage flight details and passengers using tuples.
# Requirements:
# • Store each flight as: (flight_id, source, destination, (passenger_list))
# • Show all passengers using nested loop and unpacking.
# • Count number of passengers per flight.
# • Update the flight by replacing with a new tuple.

# List of flights
flights = [
    ("AI101", "Delhi", "Mumbai", ("Alice", "Bob", "Charlie")),
    ("BA202", "Chennai", "Bangalore", ("David", "Eva")),
    ("QA303", "Kolkata", "Hyderabad", ("Frank", "Grace", "Helen", "Ian"))
]

# Show flight and passengers
print(" Flight Details:\n")
for flight_id, source, destination, passengers in flights:
    print(f"Flight: {flight_id} | From: {source} → To: {destination}")
    print("Passengers:")
    for p in passengers:
        print(f"  - {p}")
    print(f"Total Passengers: {len(passengers)}")
    print("-" * 40)

# Update a flight by replacing its tuple (e.g., add a new passenger to BA202)
flights[1] = ("BA202", "Chennai", "Bangalore", ("David", "Eva", "Jacob"))

print("\n Updated Flight:\n")
fid, src, dest, pax = flights[1]
print(f"Flight: {fid} | From: {src} → To: {dest}")
print("Passengers:", ", ".join(pax))
