# main.py

from timetable_utils import initialize_timetable, add_subject, display_timetable

def main():
    timetable, used_subjects = initialize_timetable()

    while True:
        print("\n--- College Timetable Generator ---")
        print("1. Add Subject")
        print("2. View Timetable")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            day = input("Enter day (e.g., Monday): ").capitalize()
            try:
                period = int(input("Enter period (1-5): "))
                subject = input("Enter subject name: ")

                if day not in used_subjects or not (1 <= period <= 5):
                    print("Invalid day or period.")
                    continue

                add_subject(timetable, used_subjects, day, period, subject)

            except ValueError:
                print("Period must be a number.")

        elif choice == "2":
            display_timetable(timetable)

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
