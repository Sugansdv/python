from models.attendee import Attendee
from models.event import Event
from models.session import Session
from models.registration import Registration

def main():
    # Create Event
    event = Event("AI Conference", "2025-08-10")

    # Add Sessions
    s1 = Session("AI & Ethics", "Dr. Smith", "10:00 AM")
    s2 = Session("ML in Healthcare", "Dr. Adams", "12:00 PM")
    event.add_session(s1)
    event.add_session(s2)

    print(event)
    for sess in event.sessions:
        print(sess)

    # Register Attendees
    a1 = Attendee("Alice", "alice@example.com")
    a2 = Attendee("Bob", "bob@example.com")

    r1 = Registration(a1, event)
    r1.assign_session(s1)

    r2 = Registration(a2, event)
    r2.assign_session(s1)
    r2.assign_session(s2)

    print("\nRegistrations:")
    print(r1)
    print()
    print(r2)

    print(f"\n Total Attendees Registered: {Attendee.get_total_attendees()}")

if __name__ == "__main__":
    main()
