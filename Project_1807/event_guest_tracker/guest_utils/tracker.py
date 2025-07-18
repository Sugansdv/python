

guest_data = {}  # { (event_id,): { "guests": set(), "rsvp": { name: True/False } } }

def create_event(event_id):
    key = (event_id,)
    if key in guest_data:
        print("Event already exists.")
    else:
        guest_data[key] = { "guests": set(), "rsvp": {} }
        print("Event created.")

def add_guest(event_id, name):
    key = (event_id,)
    if key not in guest_data:
        print("Event not found.")
        return

    if name in guest_data[key]["guests"]:
        print(f"{name} is already invited.")
    else:
        guest_data[key]["guests"].add(name)
        guest_data[key]["rsvp"][name] = False
        print(f"{name} added to event {event_id}.")

def update_rsvp(event_id, name, status):
    key = (event_id,)
    if key in guest_data and name in guest_data[key]["rsvp"]:
        guest_data[key]["rsvp"][name] = status
        print(f"RSVP updated: {name} → {'Yes' if status else 'No'}")
    else:
        print("Guest or event not found.")

def view_event(event_id):
    key = (event_id,)
    if key not in guest_data:
        return "Event not found."
    
    guests = guest_data[key]["guests"]
    rsvp = guest_data[key]["rsvp"]
    return {
        "guests": list(guests),
        "rsvp": rsvp
    }

def list_events():
    return [eid[0] for eid in guest_data.keys()]
