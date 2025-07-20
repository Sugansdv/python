from datetime import datetime

def generate_event_id(date, time, desc):
    return (date, time, desc[:5])  # partial description as part of ID

def add_event(events):
    date = input("Date (YYYY-MM-DD): ")
    time = input("Time (HH:MM): ")
    desc = input("Description: ")
    participants = input("Participants (comma-separated): ").split(',')
    event = {
        "id": generate_event_id(date, time, desc),
        "date": date,
        "time": time,
        "desc": desc,
        "participants": set(p.strip() for p in participants)
    }
    events.append(event)
    print(" Event added.")

def delete_event(events):
    desc = input("Enter event description to delete: ")
    found = False
    for event in events:
        if desc.lower() in event["desc"].lower():
            events.remove(event)
            found = True
            print(" Event deleted.")
            break
    if not found:
        print(" Event not found.")

def update_event(events):
    desc = input("Enter event description to update: ")
    for event in events:
        if desc.lower() in event["desc"].lower():
            print("Leave blank to keep existing.")
            new_time = input(f"New time (current: {event['time']}): ") or event["time"]
            new_participants = input("New participants (comma-separated): ")
            if new_participants:
                event["participants"] = set(p.strip() for p in new_participants.split(','))
            event["time"] = new_time
            print(" Event updated.")
            return
    print(" Event not found.")

def get_all_dates(events):
    return sorted(set(event["date"] for event in events))
