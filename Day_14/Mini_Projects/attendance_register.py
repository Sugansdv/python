import csv
from datetime import datetime
import os

FILENAME = "attendance.csv"

def mark_attendance(name):
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    header = ["Name", "Date", "Time"]
    data = [name, date_str, time_str]

    file_exists = os.path.exists(FILENAME)

    try:
        with open(FILENAME, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(header)
            writer.writerow(data)
        print(f" Attendance marked for {name} at {date_str} {time_str}")
    except Exception as e:
        print(" Error writing attendance:", e)

def generate_report(employee_name):
    if not os.path.exists(FILENAME):
        print(" Attendance file not found.")
        return

    print(f"\n Attendance Report for {employee_name}:\n")
    try:
        with open(FILENAME, "r") as f:
            reader = csv.DictReader(f)
            found = False
            for row in reader:
                if row["Name"].lower() == employee_name.lower():
                    print(f"{row['Date']} at {row['Time']}")
                    found = True
            if not found:
                print("No records found.")
    except Exception as e:
        print(" Error reading attendance file:", e)

def main():
    while True:
        print("\n=== Employee Attendance Register ===")
        print("1. Mark Attendance")
        print("2. Generate Report")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == "1":
            name = input("Enter employee name: ").strip()
            if name:
                mark_attendance(name)
        elif choice == "2":
            emp = input("Enter employee name for report: ").strip()
            generate_report(emp)
        elif choice == "3":
            print(" Exiting...")
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
