# Movie class
class Movie:
    def __init__(self, title, duration, seats):
        self.title = title
        self.duration = duration
        self.seats = [Seat(i+1) for i in range(seats)]

    def show_available_seats(self):
        available = [str(seat.number) for seat in self.seats if seat.is_available]
        print(f" Available seats for '{self.title}': {', '.join(available) if available else 'None'}")

    @staticmethod
    def check_seat_availability(seat):
        return seat.is_available

# Seat class
class Seat:
    def __init__(self, number):
        self.number = number
        self.is_available = True

    def book(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def cancel(self):
        self.is_available = True

# Ticket class with polymorphism (via __str__)
class Ticket:
    def __init__(self, movie, seat, user):
        self.movie = movie
        self.seat = seat
        self.user = user

    def cancel_ticket(self):
        self.seat.cancel()
        print(f"Ticket cancelled for {self.user.name} (Seat {self.seat.number})")

    def __str__(self):
        return (f" Ticket\n"
                f"User: {self.user.name}\n"
                f"Movie: {self.movie.title}\n"
                f"Seat No: {self.seat.number}\n")

# User class
class User:
    def __init__(self, name):
        self.name = name
        self.tickets = []

    def book_ticket(self, movie, seat_number):
        if 0 < seat_number <= len(movie.seats):
            seat = movie.seats[seat_number - 1]
            if Movie.check_seat_availability(seat):
                if seat.book():
                    ticket = Ticket(movie, seat, self)
                    self.tickets.append(ticket)
                    print(f"Ticket booked for {self.name} (Seat {seat_number})")
                    print(ticket)
                else:
                    print(" Seat already booked.")
            else:
                print(" Seat not available.")
        else:
            print(" Invalid seat number.")

    def cancel_ticket(self, seat_number):
        for ticket in self.tickets:
            if ticket.seat.number == seat_number:
                ticket.cancel_ticket()
                self.tickets.remove(ticket)
                return
        print(f" No ticket found for seat {seat_number}.")

# Demo
if __name__ == "__main__":
    # Create movie
    movie = Movie("Interstellar", "2h 49m", seats=5)

    # Create users
    user1 = User("Aarav")
    user2 = User("Sneha")

    # Show available seats
    movie.show_available_seats()

    # Book tickets
    user1.book_ticket(movie, 2)
    user2.book_ticket(movie, 3)
    user2.book_ticket(movie, 2)  # Already booked

    # Cancel a ticket
    user1.cancel_ticket(2)

    # Try to rebook the same seat
    user2.book_ticket(movie, 2)

    # Final available seats
    movie.show_available_seats()
