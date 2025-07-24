from datetime import datetime

class NoSeatsAvailableError(Exception):
    pass

class InvalidPassengerIDError(Exception):
    pass

class FrequentFlyerBookingError(Exception):
    pass

TOTAL_SEATS = 3
booked_passengers = []
frequent_flyers = ['FF1001', 'FF2002']

def book_ticket(passenger_id, travel_date):
    try:
        # Check if seats are available
        if len(booked_passengers) >= TOTAL_SEATS:
            raise NoSeatsAvailableError(" No seats available for booking.")

        # Validate passenger ID
        if not passenger_id.startswith("ID") and not passenger_id.startswith("FF"):
            raise InvalidPassengerIDError(" Passenger ID is invalid. Must start with 'ID' or 'FF'.")

        # Convert and validate date
        try:
            travel_date = datetime.strptime(travel_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        # Check if frequent flyer has restriction
        if passenger_id in frequent_flyers:
            raise FrequentFlyerBookingError(f" Frequent flyer {passenger_id} has exceeded booking limit.")

        booked_passengers.append((passenger_id, travel_date))
        print(f" Ticket booked for {passenger_id} on {travel_date.date()}")

    except (NoSeatsAvailableError, InvalidPassengerIDError, ValueError, FrequentFlyerBookingError) as e:
        print(e)

    finally:
        print(f" Booking status: {len(booked_passengers)} seat(s) booked.\n")

# --- Run Task 19 ---
book_ticket("ID1234", "2025-08-10")
book_ticket("FF1001", "2025-08-11")
book_ticket("ID5678", "2025-08-12")
book_ticket("X999", "2025-08-13")  # Invalid ID
book_ticket("ID9999", "invalid-date")  # Invalid date
book_ticket("ID7777", "2025-08-14")  # No seats
