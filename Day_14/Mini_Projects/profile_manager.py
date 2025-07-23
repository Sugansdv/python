import json
import os

FILENAME = "profiles.json"

def load_profiles():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return empty dict if file doesn't exist
    except json.JSONDecodeError:
        return {}  # Return empty if JSON is malformed

def save_profiles(profiles):
    with open(FILENAME, "w") as file:
        json.dump(profiles, file, indent=4)

def add_profile():
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    age = input("Age: ").strip()
    phone = input("Phone: ").strip()

    profiles = load_profiles()

    if name in profiles:
        print(" Profile already exists. Use update option.")
        return

    profiles[name] = {
        "email": email,
        "age": age,
        "phone": phone
    }

    save_profiles(profiles)
    print(" Profile added successfully.")

def view_profiles():
    profiles = load_profiles()

    if not profiles:
        print(" No profiles found.")
        return

    print("\n Stored Profiles:")
    for name, data in profiles.items():
        print(f"\n Name: {name}")
        print(f" Email: {data['email']}")
        print(f" Age: {data['age']}")
        print(f" Phone: {data['phone']}")

def update_profile():
    name = input("Enter name of profile to update: ").strip()
    profiles = load_profiles()

    try:
        profile = profiles[name]
        print(f"\nCurrent profile: {profile}")
        email = input("New Email (leave blank to keep current): ").strip()
        age = input("New Age (leave blank to keep current): ").strip()
        phone = input("New Phone (leave blank to keep current): ").strip()

        if email:
            profile["email"] = email
        if age:
            profile["age"] = age
        if phone:
            profile["phone"] = phone

        profiles[name] = profile
        save_profiles(profiles)
        print(" Profile updated.")
    except KeyError:
        print(" Profile not found.")

def delete_profile():
    name = input("Enter name of profile to delete: ").strip()
    profiles = load_profiles()

    try:
        del profiles[name]
        save_profiles(profiles)
        print(" Profile deleted.")
    except KeyError:
        print(" Profile not found.")

def main():
    print("=== JSON Profile Manager ===")

    while True:
        print("\nMenu:")
        print("1. Add Profile")
        print("2. View Profiles")
        print("3. Update Profile")
        print("4. Delete Profile")
        print("5. Exit")

        choice = input("Enter choice (1–5): ").strip()

        if choice == "1":
            add_profile()
        elif choice == "2":
            view_profiles()
        elif choice == "3":
            update_profile()
        elif choice == "4":
            delete_profile()
        elif choice == "5":
            print(" Exiting. Goodbye!")
            break
        else:
            print(" Invalid option. Try again.")

if __name__ == "__main__":
    main()
