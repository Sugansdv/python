# 15. Movie Theater Booking
# Goal: Handle seating allocation in a theater.
# Requirements:
# • Store seats as tuple of tuples: ((row1), (row2), ...)
# • Access specific seat using seat[row][col].
# • Show all empty seats using loop.
# • Prevent changes to seats once booked using immutability.

# Representing theater seating layout
# "E" = Empty, "B" = Booked
seats = (
    ("E", "B", "E", "E"),
    ("B", "B", "E", "E"),
    ("E", "E", "E", "B"),
    ("B", "E", "E", "E")
)

# Show all empty seats
print(" Empty Seats:\n")
for row_index, row in enumerate(seats):
    for col_index, seat in enumerate(row):
        if seat == "E":
            print(f"Row {row_index + 1}, Seat {col_index + 1} is available")

# Access a specific seat (e.g., row 3, seat 2)
row_num = 2
seat_num = 1
status = seats[row_num][seat_num]
print(f"\n Seat at Row {row_num + 1}, Seat {seat_num + 1} is: {'Empty' if status == 'E' else 'Booked'}")
