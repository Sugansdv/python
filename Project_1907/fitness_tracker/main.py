from tracker.operations import add_activity, edit_activity, view_statistics
from visuals.plot import show_activity_chart

activities = []

def main():
    while True:
        print("\n Fitness Tracker")
        print("1. Add Activity")
        print("2. Edit Activity")
        print("3. View Statistics")
        print("4. Show Activity Chart")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            type_ = input("Activity Type: ")
            duration = float(input("Duration (in mins): "))
            calories = float(input("Calories burned: "))
            add_activity(activities, date, type_, duration, calories)

        elif choice == "2":
            date = input("Enter date to edit: ")
            type_ = input("New Type: ")
            duration = float(input("New Duration: "))
            calories = float(input("New Calories: "))
            edit_activity(activities, date, type_, duration, calories)

        elif choice == "3":
            view_statistics(activities)

        elif choice == "4":
            show_activity_chart(activities)

        elif choice == "5":
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
