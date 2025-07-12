# 10. Travel Bucket List
# Description: Maintain a list of places a user wants to visit.

# Initial list of places
bucket_list = ["Japan", "Norway", "Canada", "New Zealand"]

# Display all places
def display_places():
    print("\n Travel Bucket List:")
    for index, place in enumerate(bucket_list, start=1):
        print(f"{index}. {place}")

# Display current list
display_places()

# Add a new place
new_place = "Switzerland"
if new_place not in bucket_list:
    bucket_list.append(new_place)
    print(f"\nAdded '{new_place}' to the bucket list.")
else:
    print(f"\n'{new_place}' is already on the list.")

# Remove a place
place_to_remove = "Canada"
if place_to_remove in bucket_list:
    bucket_list.remove(place_to_remove)
    print(f"Removed '{place_to_remove}' from the list.")

# Update a place (change 'Norway' to 'Iceland')
for i in range(len(bucket_list)):
    if bucket_list[i] == "Norway":
        bucket_list[i] = "Iceland"
        print("Updated 'Norway' to 'Iceland'.")

# Final display
display_places()
