# 8. Bus Schedule Management System
# Goal: Handle route schedules using tuples.
# Requirements:
# • Store route as (bus_no, departure_time, arrival_time, (stops))
# • Use slicing and indexing to extract time and stops.
# • Display entire schedule using unpacking.
# • Simulate update by replacing old tuple with a new one.

# Sample bus schedule data
routes = [
    ("B101", "06:00", "08:30", ("Stop A", "Stop B", "Stop C", "Stop D")),
    ("B202", "09:15", "11:45", ("Stop E", "Stop F", "Stop G")),
    ("B303", "13:00", "15:30", ("Stop H", "Stop I", "Stop J", "Stop K"))
]

# Display full schedule
print("Bus Schedule:\n")
for bus_no, dep_time, arr_time, stops in routes:
    print(f"Bus No     : {bus_no}")
    print(f"Departure  : {dep_time}")
    print(f"Arrival    : {arr_time}")
    print("Stops      : " + " → ".join(stops))
    print("-" * 40)

# Extract departure and arrival times of second bus
second_bus = routes[1]
print(f"\n⏱ Second Bus Times: Departure - {second_bus[1]}, Arrival - {second_bus[2]}")

# Simulate update: replace entire tuple with a new one
routes[2] = ("B303", "13:00", "16:00", ("Stop H", "Stop I", "Stop J", "Stop K", "Stop L"))
print("\n Updated Last Bus Schedule:")
bus_no, dep_time, arr_time, stops = routes[2]
print(f"{bus_no}: {dep_time} to {arr_time}, Stops: {' → '.join(stops)}")
