# 16. Vehicle Service History Tracker
# Goal: Maintain vehicle service history.
# Requirements:
# • Each record: (vehicle_number, (service1_date, service2_date))
# • Use slicing to show recent services.
# • Unpack data to display timeline.
# • Replace old tuple on new service.

# List of service history records
service_records = [
    ("TN10AB1234", ("2023-05-10", "2024-05-15")),
    ("MH12XY5678", ("2022-11-20", "2023-11-25")),
    ("KA05GH9012", ("2023-03-01", "2024-03-05"))
]

# Display full service timeline
print("Vehicle Service History:\n")
for vehicle, (s1, s2) in service_records:
    print(f"Vehicle: {vehicle}")
    print(f"  Service 1: {s1}")
    print(f"  Service 2: {s2}")
    print("-" * 30)

# Show recent service dates (last service only)
print("\n Recent Services:")
for vehicle, services in service_records:
    print(f"{vehicle} - Last Serviced On: {services[-1]}")

# Replace old tuple to simulate a new service entry
# (e.g., update MH12XY5678 with a new service date)
old_record = service_records[1]
vehicle_num, (old_s1, old_s2) = old_record
new_record = (vehicle_num, (old_s2, "2025-07-15"))
service_records[1] = new_record

print("\n Updated Record:")
print(f"{new_record[0]} → Service Dates: {new_record[1][0]}, {new_record[1][1]}")
