def add_appointment(appointments):
    date = input("Date (YYYY-MM-DD): ").strip()
    time = input("Time (HH:MM): ").strip()
    person = input("Person: ").strip()
    purpose = input("Purpose: ").strip()

    appt = (time, person, purpose)
    appointments.setdefault(date, []).append(appt)
    print("Appointment added.")

def remove_appointment(appointments):
    date = input("Date (YYYY-MM-DD): ").strip()
    if date not in appointments:
        print("No appointments on this date.")
        return

    for idx, (time, person, purpose) in enumerate(appointments[date], start=1):
        print(f"{idx}. {time} - {person} - {purpose}")
    choice = input("Enter number to remove: ").strip()

    try:
        index = int(choice) - 1
        removed = appointments[date].pop(index)
        print(f"Removed: {removed}")
        if not appointments[date]:
            del appointments[date]
    except (ValueError, IndexError):
        print("Invalid choice.")

def edit_appointment(appointments):
    date = input("Date (YYYY-MM-DD): ").strip()
    if date not in appointments:
        print("No appointments on this date.")
        return

    for idx, (time, person, purpose) in enumerate(appointments[date], start=1):
        print(f"{idx}. {time} - {person} - {purpose}")
    choice = input("Enter number to edit: ").strip()

    try:
        index = int(choice) - 1
        time = input("New Time (HH:MM): ").strip()
        person = input("New Person: ").strip()
        purpose = input("New Purpose: ").strip()
        appointments[date][index] = (time, person, purpose)
        print("Appointment updated.")
    except (ValueError, IndexError):
        print("Invalid choice.")

def view_schedule(appointments):
    if not appointments:
        print("No appointments scheduled.")
        return
    for date in sorted(appointments):
        print(f"\nDate: {date}")
        for time, person, purpose in sorted(appointments[date]):
            print(f" - {time} | {person} | {purpose}")
