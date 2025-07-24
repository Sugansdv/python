MAX_DAYS = 30

class AttendanceExceededError(Exception):
    pass

students = {"101": "Alice", "102": "Bob", "103": "Charlie"}
attendance = {}

for roll in students:
    try:
        days_present = int(input(f"Enter days present for {students[roll]} (Roll: {roll}): "))
        if days_present > MAX_DAYS:
            raise AttendanceExceededError(f"Attendance can't exceed {MAX_DAYS}.")
        attendance[roll] = days_present
    except ValueError:
        print("Please enter a valid number.")
    except AttendanceExceededError as e:
        print(e)
    except KeyError:
        print("Invalid roll number.")
    except Exception as e:
        print("Unexpected error:", e)

print("Attendance Records:", attendance)
