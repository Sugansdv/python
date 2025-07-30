from calendar_app.core import Event, CalendarScheduler

def main():
    scheduler = CalendarScheduler()

    print(" Calendar Scheduler")
    while True:
        title = input("Enter event title: ")
        date = input("Enter event date (YYYY-MM-DD): ")
        start = input("Enter start time (HH:MM): ")
        end = input("Enter end time (HH:MM): ")

        try:
            event = Event(title, date, start, end)
            scheduler.add_event(event)
            print(" Event added.")
        except Exception as e:
            print(f" Error: {e}")

        more = input("Add another event? (y/n): ").lower()
        if more != 'y':
            break

    scheduler.save_to_ics()
    print(" Calendar saved to data/calendar.ics")

    view_date = input("\n View events for date (YYYY-MM-DD): ")
    print(" Events:")
    for e in scheduler.daily_events(view_date):
        print("-", e)

if __name__ == "__main__":
    main()
