# 12. Event Guest List Manager
# Description: Track guest names for an event.

# Initial guest list
guest_list = ["Alice", "Bob", "Charlie", "Diana"]

# Display initial list
print("Current Guest List:")
for guest in guest_list:
    print("-", guest)

# Add guests
guest_list.append("Ethan")
guest_list.append("Fiona")
print("\nAdded 'Ethan' and 'Fiona' to the guest list.")

# Remove a guest
guest_to_remove = "Charlie"
if guest_to_remove in guest_list:
    guest_list.remove(guest_to_remove)
    print(f"Removed '{guest_to_remove}' from the list.")

# Print total number of guests using len()
print(f"\nTotal Guests: {len(guest_list)}")

# Check if a guest is invited using `in`
check_name = "Diana"
if check_name in guest_list:
    print(f"{check_name} is on the guest list. ")
else:
    print(f"{check_name} is NOT on the guest list. ")
