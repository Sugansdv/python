from modules.trip_ops import add_trip, edit_trip, remove_trip, list_trips, calculate_costs
from modules.suggestion_engine import suggest_destinations
from modules.store import load_trips, save_trips

def main():
    trips = load_trips()

    while True:
        print("\n Travel Planner")
        print("1. Add Trip")
        print("2. Edit Trip")
        print("3. Remove Trip")
        print("4. List Trips")
        print("5. Suggest Destinations")
        print("6. Calculate Costs")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_trip(trips)
        elif choice == "2":
            edit_trip(trips)
        elif choice == "3":
            remove_trip(trips)
        elif choice == "4":
            list_trips(trips)
        elif choice == "5":
            suggest_destinations(trips)
        elif choice == "6":
            calculate_costs(trips)
        elif choice == "7":
            save_trips(trips)
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice.")

if __name__ == "__main__":
    main()
