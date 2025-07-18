
parcel_db = {}  # { (tracking_id,): {status, city} }
visited_cities = set()  # Unique cities

def add_parcel(tracking_id, status, city):
    if not isinstance(tracking_id, tuple):
        raise TypeError("Tracking ID must be a tuple.")
    if tracking_id in parcel_db:
        print("Parcel already exists.")
    else:
        parcel_db[tracking_id] = {"status": status, "city": city}
        visited_cities.add(city)
        print("Parcel added successfully.")

def update_status(tracking_id, new_status):
    if tracking_id in parcel_db:
        parcel_db[tracking_id]["status"] = new_status
        print("Status updated successfully.")
    else:
        print("Parcel not found.")

def fetch_parcel(tracking_id):
    return parcel_db.get(tracking_id, "Parcel not found.")

def get_all_cities():
    return visited_cities
