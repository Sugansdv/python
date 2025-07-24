from datetime import datetime

class OverBookingError(Exception):
    pass

def hotel_booking():
    total_rooms = 5

    try:
        date_input = input("Enter booking date (YYYY-MM-DD): ")
        try:
            booking_date = datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            raise ValueError(" Invalid date format. Use YYYY-MM-DD.")

        guests = int(input("Enter number of guests: "))
        assert guests > 0, " Guest count must be positive."

        if guests > total_rooms:
            raise OverBookingError(" Not enough rooms available.")

        print(f" Booking confirmed for {guests} guest(s) on {booking_date.date()}.")

    except OverBookingError as oe:
        print(oe)
    except AssertionError as ae:
        print(ae)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(" Unexpected error:", e)

if __name__ == "__main__":
    hotel_booking()
