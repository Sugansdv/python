def list_events_by_date(events, date):
    found = False
    print(f" Events on {date}:")
    for event in events:
        if event["date"] == date:
            found = True
            print(f" {event['time']} - {event['desc']} | Participants: {', '.join(event['participants'])}")
    if not found:
        print("No events found on this date.")
