# ---------------------- Bus Class ----------------------
class Bus:
    def __init__(self, bus_no, total_seats):
        self.bus_no = bus_no
        self.total_seats = total_seats
        self.available_seats = [Seat(i+1) for i in range(total_seats)]

    def check_availability(self):
        return len(self.available_seats) > 0

    def assign_seat(self):
        if self.check_availability():
            return self.available_seats.pop(0)  # FIFO seat assignment
        else:
            return None

# ---------------------- Seat Class ----------------------
class Seat:
    def __init__(self, seat_no):
        self.seat_no = seat_no

    def __str__(self):
        return f"Seat #{self.seat_no}"

# ---------------------- Passenger Class ----------------------
class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# ---------------------- Booking Class ----------------------
class Booking:
    def __init__(self, passenger, bus):
        self.passenger = passenger
        self.bus = bus
        self.seat = self.bus.assign_seat()

    def __eq__(self, other):
        return (
            isinstance(other, Booking)
            and self.passenger.name == other.passenger.name
            and self.bus.bus_no == other.bus.bus_no
            and self.seat.seat_no == other.seat.seat_no
        )

    def __str__(self):
        if self.seat:
            return (
                f" Booking Ticket\n"
                f"Name      : {self.passenger.name}\n"
                f"Age       : {self.passenger.age}\n"
                f"Bus No.   : {self.bus.bus_no}\n"
                f"Seat No.  : {self.seat.seat_no}\n"
                f"--------------------------"
            )
        else:
            return f"No seats available for {self.passenger.name}"

# ---------------------- Test the System ----------------------
if __name__ == "__main__":
    bus1 = Bus("KA01AB1234", 2)  # Only 2 seats

    p1 = Passenger("Arjun", 28)
    p2 = Passenger("Kiran", 34)
    p3 = Passenger("Riya", 22)

    b1 = Booking(p1, bus1)
    b2 = Booking(p2, bus1)
    b3 = Booking(p3, bus1)  # Should show no seats available

    print(b1)
    print(b2)
    print(b3)

    # Check equality
    print("\n Is b1 same as b2?", b1 == b2)
