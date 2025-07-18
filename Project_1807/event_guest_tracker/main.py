
from guest_utils import create_event, add_guest, update_rsvp, view_event, list_events

def main():
    while True:
        print("\n--- Event Guest Tracker ---")
        print("1. Create Event")
        print("2. Add Guest")
        print("3. Update RSVP")
        print("4. View Event Details")
        print("5. List Events")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == '1':
            eid = input("Enter new Event ID: ").strip()
            create_event(eid)

        elif choice == '2':
            eid = input("Event ID: ").strip()
            name = input("Guest Name: ").strip()
            add_guest(eid, name)

        elif choice == '3':
            eid = input("Event ID: ").strip()
            name = input("Guest Name: ").strip()
            status_input = input("RSVP (yes/no): ").strip().lower()
            status = status_input == "yes"
            update_rsvp(eid, name, status)

        elif choice == '4':
            eid = input("Event ID: ").strip()
            details = view_event(eid)
            if isinstance(details, str):
                print(details)
            else:
                print(f"Guests in Event {eid}:")
                for guest in details["guests"]:
                    rsvp = "Yes" if details["rsvp"][guest] else "No"
                    print(f" - {guest} (RSVP: {rsvp})")

        elif choice == '5':
            events = list_events()
            print("Events:", ", ".join(events) if events else "No events yet.")

        elif choice == '6':
            print("Exiting Guest Tracker.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
