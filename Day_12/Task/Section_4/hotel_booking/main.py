from rooms import list_rooms
from guests import guest_info
from bookings import book_room

rooms = list_rooms()
print("Available rooms:", rooms)
guest = guest_info("Sugan")
print(guest)
print(book_room("101", "Sugan"))
