# 2. GPS Location Logger
# Goal: Track locations using latitude and longitude stored in tuples.
# Requirements:
# • Store GPS coordinates as (latitude, longitude) tuples.
# • Maintain a list of these tuples to simulate movement.
# • Use slicing to retrieve the last 5 locations.
# • Unpack coordinates for mapping on screen.
# • Prevent editing the original GPS points.

# List of GPS coordinates representing tracked locations
gps_log = [
    (12.9716, 77.5946),
    (12.9721, 77.5950),
    (12.9725, 77.5955),
    (12.9730, 77.5960),
    (12.9735, 77.5965),
    (12.9740, 77.5970),
    (12.9745, 77.5975),
    (12.9750, 77.5980)
]

print(" Last 5 GPS Locations:\n")

# Get the last 5 coordinates using slicing
recent_locations = gps_log[-5:]

for i, (lat, lon) in enumerate(recent_locations, start=1):
    print(f"{i}. Latitude: {lat}, Longitude: {lon}")
