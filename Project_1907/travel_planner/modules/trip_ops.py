def add_trip(trips):
    destination = input("Destination: ")
    start = input("Start Date (YYYY-MM-DD): ")
    end = input("End Date (YYYY-MM-DD): ")
    participants = set(input("Participants (comma-separated): ").split(","))
    itinerary = input("Itinerary (comma-separated items): ").split(",")

    trip = {
        "destination": destination,
        "dates": (start, end),
        "participants": participants,
        "itinerary": itinerary
    }
    trips.append(trip)
    print(" Trip added.")

def edit_trip(trips):
    destination = input("Destination to edit: ")
    for trip in trips:
        if trip["destination"] == destination:
            trip["dates"] = (input("New Start Date: "), input("New End Date: "))
            trip["participants"] = set(input("New participants: ").split(","))
            trip["itinerary"] = input("New itinerary (comma-separated): ").split(",")
            print("✏️ Trip updated.")
            return
    print(" Trip not found.")

def remove_trip(trips):
    destination = input("Destination to remove: ")
    for i, trip in enumerate(trips):
        if trip["destination"] == destination:
            del trips[i]
            print(" Trip removed.")
            return
    print(" Trip not found.")

def list_trips(trips):
    if not trips:
        print(" No trips found.")
        return
    for trip in trips:
        print(f" {trip['destination']} ({trip['dates'][0]} to {trip['dates'][1]}) - {len(trip['participants'])} participants")

def calculate_costs(trips):
    for trip in trips:
        cost_per_person = float(input(f"Enter cost per person for {trip['destination']}: "))
        total = cost_per_person * len(trip["participants"])
        print(f" Total cost for {trip['destination']}: ₹{total}")
