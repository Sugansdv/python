# 17. Festival Event Planner
# Goal: Plan festival events with tuple-based scheduling.
# Requirements:
# • Store event as (event_name, (start_time, end_time, location))
# • Display schedule with index-based access.
# • Use list of tuples to show full day plan.
# • Immutable tuples prevent accidental time edits.

# List of festival events
festival_schedule = [
    ("Opening Ceremony", ("09:00 AM", "10:00 AM", "Main Stage")),
    ("Music Show", ("10:30 AM", "12:00 PM", "Auditorium")),
    ("Food Tasting", ("12:30 PM", "02:00 PM", "Food Court")),
    ("Dance Performance", ("02:30 PM", "04:00 PM", "Stage B")),
    ("Closing Ceremony", ("05:00 PM", "06:00 PM", "Main Stage"))
]

# Display full day plan using index-based access
print(" Festival Event Schedule:\n")
for event in festival_schedule:
    name = event[0]
    start_time = event[1][0]
    end_time = event[1][1]
    location = event[1][2]
    print(f"{name} | {start_time} - {end_time} at {location}")
