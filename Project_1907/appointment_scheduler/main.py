from modules.scheduler import add_appointment, remove_appointment, edit_appointment, view_schedule
from modules.notifier import get_unique_people

appointments = {}

def main():
    print("Welcome to Appointment Scheduler")

    while True:
        print("\nMenu:")
        print("1. Add Appointment")
        print("2. Remove Appointment")
        print("3. Edit Appointment")
        print("4. View Schedule")
        print("5. Unique People")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_appointment(appointments)
        elif choice == "2":
            remove_appointment(appointments)
        elif choice == "3":
            edit_appointment(appointments)
        elif choice == "4":
            view_schedule(appointments)
        elif choice == "5":
            people = get_unique_people(appointments)
            print("Unique People:")
            for p in people:
                print(f" - {p}")
        elif choice == "6":
            print("Exiting Appointment Scheduler.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
