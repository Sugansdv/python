

bookings = {}  # passenger_id (tuple) → booking details
destinations = set()  # To avoid duplicate destinations

def create_booking(passenger_id: tuple, name: str, destination: str):
    if passenger_id in bookings:
        return "Booking already exists for this passenger."

    bookings[passenger_id] = {
        "name": name,
        "destination": destination.title()
    }
    destinations.add(destination.title())
    return "Booking successful."


def view_booking(passenger_id: tuple):
    return bookings.get(passenger_id, "No booking found.")


def list_destinations():
    return sorted(destinations)
