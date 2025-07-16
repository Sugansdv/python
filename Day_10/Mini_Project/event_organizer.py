# 20. Event Organizer
# Description: Organize event registrations.
# Requirements:
# - {event_name: {"participants": [...], "max": ...}}
# - Register participant (check max limit)
# - Cancel registration using remove()
# - Count participants per event

events = {
    "TechTalk": {"participants": ["Alice", "Bob"], "max": 3},
    "Hackathon": {"participants": ["Charlie"], "max": 5}
}

def register(event, name):
    event_info = events.get(event)
    if event_info:
        if name in event_info["participants"]:
            print(f"{name} is already registered for {event}.")
        elif len(event_info["participants"]) < event_info["max"]:
            event_info["participants"].append(name)
            print(f"{name} registered for {event}.")
        else:
            print(f"{event} is full.")
    else:
        print(f"Event '{event}' not found.")

def cancel_registration(event, name):
    if event in events and name in events[event]["participants"]:
        events[event]["participants"].remove(name)
        print(f"{name} removed from {event}.")
    else:
        print(f"{name} not found in {event}.")

def count_participants(event):
    if event in events:
        count = len(events[event]["participants"])
        print(f"{event} has {count} participant(s).")
    else:
        print(f"{event} not found.")

register("TechTalk", "David")
register("TechTalk", "Eve")       
register("TechTalk", "Frank")    
cancel_registration("Hackathon", "Charlie")
count_participants("TechTalk")
count_participants("Hackathon")
