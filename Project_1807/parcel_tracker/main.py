
from parcel_utils import add_parcel, update_status, fetch_parcel, get_all_cities

def main():
    while True:
        print("\n--- Parcel Tracker Menu ---")
        print("1. Add Parcel")
        print("2. Update Parcel Status")
        print("3. Fetch Parcel Info")
        print("4. Show All Cities")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            tid = input("Enter tracking ID (e.g., P001): ").strip()
            status = input("Enter parcel status: ").strip()
            city = input("Enter city name: ").strip()
            add_parcel((tid,), status, city)

        elif choice == '2':
            tid = input("Enter tracking ID: ").strip()
            status = input("Enter new status: ").strip()
            update_status((tid,), status)

        elif choice == '3':
            tid = input("Enter tracking ID: ").strip()
            parcel_info = fetch_parcel((tid,))
            print("Parcel Info:", parcel_info)

        elif choice == '4':
            print("Visited Cities:", get_all_cities())

        elif choice == '5':
            print("Exiting Parcel Tracker.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
