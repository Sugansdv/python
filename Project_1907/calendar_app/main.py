from modules.event_ops import add_event, delete_event, update_event, get_all_dates
from modules.calendar_view import list_events_by_date
from datetime import datetime

events = []

def main():
    while True:
        print("\n Simple Calendar App")
        print("1. Add Event")
        print("2. Delete Event")
        print("3. Update Event")
        print("4. View Events by Date")
        print("5. View All Dates with Events")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_event(events)
        elif choice == "2":
            delete_event(events)
        elif choice == "3":
            update_event(events)
        elif choice == "4":
            date = input("Enter date (YYYY-MM-DD): ")
            list_events_by_date(events, date)
        elif choice == "5":
            dates = get_all_dates(events)
            print("Dates with Events:", dates)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
