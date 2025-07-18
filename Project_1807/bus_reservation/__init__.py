
# Dictionary to store seat info (key: seat number, value: (user_id tuple))
seat_info = {}

# Set to track occupied seats
occupied_seats = set()

def reserve_seat(seat_number, user_id):
    if seat_number in occupied_seats:
        return f"Seat {seat_number} is already reserved."
    
    seat_info[seat_number] = user_id  # store user_id tuple
    occupied_seats.add(seat_number)
    return f"Seat {seat_number} successfully reserved for user {user_id}"

def cancel_reservation(seat_number):
    if seat_number in occupied_seats:
        occupied_seats.remove(seat_number)
        seat_info.pop(seat_number, None)
        return f"Seat {seat_number} reservation cancelled."
    return f"Seat {seat_number} is not reserved."

def show_reserved_seats():
    return {seat: user for seat, user in seat_info.items()}
