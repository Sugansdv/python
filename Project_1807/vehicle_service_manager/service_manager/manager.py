
def add_vehicle_record(records, plate_number, owner, services):
    plate_id = tuple(plate_number.split('-'))  # e.g., "TN-12-AB1234"
    if plate_id not in records:
        records[plate_id] = {
            "owner": owner,
            "services": set(services)
        }
    else:
        records[plate_id]["services"].update(services)
    return plate_id

def get_service_types(records, plate_id):
    return records.get(plate_id, {}).get("services", set())

def display_all_records(records):
    for plate_id, info in records.items():
        print(f"Vehicle ID: {'-'.join(plate_id)}")
        print(f"Owner: {info['owner']}")
        print(f"Services: {', '.join(info['services'])}")
        print("-" * 40)
