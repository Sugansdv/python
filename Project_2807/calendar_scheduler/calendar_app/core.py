from datetime import datetime
from icalendar import Calendar, Event as ICalEvent
from .utils import save_calendar, parse_date

class Event:
    def __init__(self, title, date_str, start_time, end_time):
        self.title = title
        self.date = parse_date(date_str)
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.title} on {self.date.strftime('%Y-%m-%d')} from {self.start_time} to {self.end_time}"

class CalendarScheduler:
    def __init__(self):
        self.events = {}

    def add_event(self, event):
        date_key = event.date.strftime('%Y-%m-%d')
        if date_key not in self.events:
            self.events[date_key] = []

        # Check for time conflict
        for existing in self.events[date_key]:
            if existing.start_time == event.start_time:
                raise Exception("Time conflict: event already scheduled.")

        self.events[date_key].append(event)

    def save_to_ics(self, path="data/calendar.ics"):
        cal = Calendar()
        for date, evts in self.events.items():
            for evt in evts:
                ical_event = ICalEvent()
                start_dt = datetime.strptime(f"{date} {evt.start_time}", "%Y-%m-%d %H:%M")
                end_dt = datetime.strptime(f"{date} {evt.end_time}", "%Y-%m-%d %H:%M")
                ical_event.add("summary", evt.title)
                ical_event.add("dtstart", start_dt)
                ical_event.add("dtend", end_dt)
                cal.add_component(ical_event)
        save_calendar(cal, path)

    def daily_events(self, date_str):
        date_key = parse_date(date_str).strftime('%Y-%m-%d')
        if date_key not in self.events:
            yield "No events scheduled."
        else:
            for event in self.events[date_key]:
                yield str(event)
