from datetime import date

def mark_attendance(students, attendance):
    today = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    if not today:
        today = str(date.today())

    present = set()
    print("Mark attendance (y/n) for each student:")
    for roll_no, name in students:
        resp = input(f"{roll_no} - {name}: ").strip().lower()
        if resp == "y":
            present.add(roll_no)

    attendance[today] = present
    print(f"Attendance marked for {today}.")

def view_by_date(attendance):
    d = input("Enter date (YYYY-MM-DD): ").strip()
    if d in attendance:
        print(f"Present on {d}: {', '.join(attendance[d])}")
    else:
        print("No record for that date.")

def view_by_student(students, attendance):
    roll = input("Enter roll number: ").strip()
    dates = [d for d, present in attendance.items() if roll in present]
    if dates:
        print(f"{roll} was present on: {', '.join(dates)}")
    else:
        print("No attendance found for that student.")

def show_absentees(students, attendance):
    d = input("Enter date (YYYY-MM-DD): ").strip()
    if d not in attendance:
        print("No attendance for that date.")
        return

    present = attendance[d]
    absentees = {roll for roll, _ in students} - present
    print(f"Absent on {d}: {', '.join(absentees)}")
