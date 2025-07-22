class Room:
    def __init__(self, number, room_type, price):
        self.number = number
        self.room_type = room_type
        self.price = price
        self.is_booked = False


class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Booking(Room):
    def __init__(self, room, customer, days):
        super().__init__(room.number, room.room_type, room.price)
        self.customer = customer
        self.days = days

    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
            total = self.price * self.days
            return f"Room {self.number} booked for {self.customer.name}. Total: ₹{total}"
        else:
            return f"Room {self.number} is already booked."

# Example
r1 = Room(101, "Deluxe", 2000)
cust1 = Customer("John", "9876543210")
booking = Booking(r1, cust1, 3)
print(booking.book_room())
