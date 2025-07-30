from core.flight import Flight
from core.passenger import Passenger

def main():
    flight = Flight("AI101", "New York", 20)
    flight.display_status()

    name = input("Enter passenger name: ")
    seat = input("Enter seat to book (e.g., A1): ").upper()

    passenger = Passenger(name)

    try:
        flight.book_seat(seat, passenger)
        print(f"Booking successful for {name} at seat {seat}!")
    except Exception as e:
        print("Booking failed:", e)

    flight.display_status()

    cancel = input("Cancel a seat? (y/n): ")
    if cancel.lower() == 'y':
        seat_cancel = input("Enter seat to cancel: ").upper()
        try:
            flight.cancel_booking(seat_cancel)
            print(f"Cancelled booking for seat {seat_cancel}")
        except Exception as e:
            print("Cancellation failed:", e)

    print("\nAvailable Seats (via generator):")
    for s in flight.available_seat_generator():
        print(s, end=" ")

if __name__ == "__main__":
    main()

