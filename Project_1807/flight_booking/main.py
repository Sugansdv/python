
from flight import (
    create_booking,
    view_booking,
    list_destinations,
    process_payment,
    check_payment_status
)

def main():
    print("=== Flight Booking Tracker ===")

    while True:
        print("\n1. Book Flight\n2. View Booking\n3. Make Payment")
        print("4. Payment Status\n5. List Destinations\n6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Passenger Name: ")
            id_num = input("ID Number: ")
            dest = input("Destination: ")
            passenger_id = (name.lower(), id_num.strip())
            print(create_booking(passenger_id, name.title(), dest))
        elif choice == '2':
            name = input("Passenger Name: ")
            id_num = input("ID Number: ")
            passenger_id = (name.lower(), id_num.strip())
            print(view_booking(passenger_id))
        elif choice == '3':
            name = input("Passenger Name: ")
            id_num = input("ID Number: ")
            amount = float(input("Enter amount: ₹"))
            passenger_id = (name.lower(), id_num.strip())
            print(process_payment(passenger_id, amount))
        elif choice == '4':
            name = input("Passenger Name: ")
            id_num = input("ID Number: ")
            passenger_id = (name.lower(), id_num.strip())
            print("Payment Status:", check_payment_status(passenger_id))
        elif choice == '5':
            print("Available Destinations:", list_destinations())
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
