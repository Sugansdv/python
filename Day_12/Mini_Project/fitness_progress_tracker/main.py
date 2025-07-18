from fitness import log_workout, log_meal, view_progress

def main():
    while True:
        print("\n--- Fitness Tracker Menu ---")
        print("1. Log Workout")
        print("2. Log Meal")
        print("3. View Progress")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            log_workout()
        elif choice == "2":
            log_meal()
        elif choice == "3":
            view_progress()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
