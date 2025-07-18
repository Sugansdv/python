from bus_ops import reserve_seat, cancel_reservation, show_reserved_seats

# Users represented by tuples (ID, Name)
user1 = (101, "Alice")
user2 = (102, "Bob")

# Make reservations
print(reserve_seat(1, user1))  # Seat 1 for Alice
print(reserve_seat(2, user2))  # Seat 2 for Bob
print(reserve_seat(1, user2))  # Seat 1 already reserved

# Cancel a reservation
print(cancel_reservation(1))   # Cancel Alice
print(reserve_seat(1, user2))  # Now Bob can book it

# Show all reserved seats
print("Current Reservations:", show_reserved_seats())
