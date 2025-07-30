from datetime import datetime

def save_calendar(calendar_obj, path):
    with open(path, "wb") as f:
        f.write(calendar_obj.to_ical())

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format! Use YYYY-MM-DD")
