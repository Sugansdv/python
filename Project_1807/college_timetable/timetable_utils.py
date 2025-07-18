

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
PERIODS = [1, 2, 3, 4, 5]

def initialize_timetable():
    return {}, {day: set() for day in DAYS}  # timetable, subject tracker

def add_subject(timetable, used_subjects, day, period, subject):
    key = (day, period)
    if subject in used_subjects[day]:
        print(f"Subject '{subject}' already used on {day}.")
        return
    timetable[key] = subject
    used_subjects[day].add(subject)
    print(f"Added '{subject}' to {day}, Period {period}.")

def display_timetable(timetable):
    print("\n Timetable:")
    for day in DAYS:
        print(f"\n{day}:")
        for period in PERIODS:
            subject = timetable.get((day, period), "---")
            print(f"  Period {period}: {subject}")
