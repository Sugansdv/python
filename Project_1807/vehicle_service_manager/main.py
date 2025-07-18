

from service_manager import add_vehicle_record, get_service_types, display_all_records

def main():
    records = {}

    # Add vehicles
    v1 = add_vehicle_record(records, "TN-12-AB1234", "Ravi Kumar", ["Oil Change", "Tire Rotation"])
    v2 = add_vehicle_record(records, "KA-01-CD5678", "Anita Sharma", ["Brake Check"])
    
    # Update services
    add_vehicle_record(records, "TN-12-AB1234", "Ravi Kumar", ["Wheel Alignment"])

    # Display
    print("All Vehicle Records:")
    display_all_records(records)

    # Fetch services of a vehicle
    print("Services for TN-12-AB1234:")
    print(get_service_types(records, v1))

if __name__ == "__main__":
    main()
