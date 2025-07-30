import json
from functools import wraps

def confirm_booking(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print("Confirming booking...")
        return func(self, *args, **kwargs)
    return wrapper

class Flight:
    def __init__(self, flight_id, destination, total_seats):
        self.flight_id = flight_id
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = [f"{chr(row)}{col}" for row in range(65, 70) for col in range(1, 5)]  # A1-D4
        self.booked_seats = set()
        self.passengers = {}
        self.load_bookings()

    def load_bookings(self):
        try:
            with open(f"{self.flight_id}_bookings.json", "r") as f:
                data = json.load(f)
                self.booked_seats = set(data["booked_seats"])
                self.passengers = data["passengers"]
                self.available_seats = [s for s in self.available_seats if s not in self.booked_seats]
        except FileNotFoundError:
            pass

    def save_bookings(self):
        data = {
            "booked_seats": list(self.booked_seats),
            "passengers": self.passengers
        }
        with open(f"{self.flight_id}_bookings.json", "w") as f:
            json.dump(data, f, indent=4)

    @confirm_booking
    def book_seat(self, seat, passenger):
        if seat in self.booked_seats:
            raise Exception(f"Seat {seat} is already booked.")
        if seat not in self.available_seats:
            raise Exception(f"Seat {seat} is invalid.")
        self.booked_seats.add(seat)
        self.available_seats.remove(seat)
        self.passengers[seat] = passenger.name
        self.save_bookings()

    def cancel_booking(self, seat):
        if seat not in self.booked_seats:
            raise Exception(f"Seat {seat} is not booked.")
        self.booked_seats.remove(seat)
        self.available_seats.append(seat)
        del self.passengers[seat]
        self.save_bookings()

    def display_status(self):
        print(f"\nFlight to {self.destination}")
        print("Available Seats:", sorted(self.available_seats))
        print("Booked Seats:", sorted(self.booked_seats))

    def available_seat_generator(self):
        for seat in sorted(self.available_seats):
            yield seat
