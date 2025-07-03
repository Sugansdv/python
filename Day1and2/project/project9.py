## 9. Event RSVP Tracker
print("========================================")
print("            Event RSVP Tracker          ")
print("========================================")

# 1. Ask for the names of three attendees
attendee1 = input("Enter name of Attendee 1: ")
attendee2 = input("Enter name of Attendee 2: ")
attendee3 = input("Enter name of Attendee 3: ")

# 2. Store in a set to avoid duplicates
attendees = {attendee1, attendee2, attendee3}

# 3. Print the set and its type
print("\n RSVP List (duplicates removed if any):")
print(attendees)
print(f"\nType of 'attendees': {type(attendees)}")
