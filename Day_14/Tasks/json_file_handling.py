import json
import os

JSON_FILE = "user_profiles.json"

# 36. Save user profile data into a .json file
def save_user_profiles():
    users = [
        {"name": "Alice", "age": 25, "skills": ["Python", "Django"]},
        {"name": "Bob", "age": 30, "skills": ["JavaScript", "React"]},
    ]
    with open(JSON_FILE, "w") as file:
        json.dump(users, file, indent=4)
    print("36. User profiles saved to JSON.")

# 37. Read and display all user profiles
def display_profiles():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as file:
            data = json.load(file)
            print("37. All user profiles:")
            for user in data:
                print(f"   Name: {user['name']}, Age: {user['age']}, Skills: {', '.join(user['skills'])}")
    else:
        print("37. File does not exist.")

# 38. Add a new entry and save it back
def add_user_profile(name, age, skills):
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append({"name": name, "age": age, "skills": skills})
    
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)
    print(f"38. Added user: {name}")

# 39. Mini phonebook app using JSON as the database
def phonebook_app():
    phonebook_file = "phonebook.json"
    def load_phonebook():
        if os.path.exists(phonebook_file):
            with open(phonebook_file, "r") as f:
                return json.load(f)
        return {}

    def save_phonebook(pb):
        with open(phonebook_file, "w") as f:
            json.dump(pb, f, indent=4)

    phonebook = load_phonebook()
    print("39. Phonebook App - Options: add, view, exit")

    while True:
        action = input("Enter action (add/view/exit): ").strip().lower()
        if action == "add":
            name = input("Name: ")
            number = input("Phone: ")
            phonebook[name] = number
            save_phonebook(phonebook)
            print(f"   {name} added.")
        elif action == "view":
            for name, number in phonebook.items():
                print(f"   {name}: {number}")
        elif action == "exit":
            break
        else:
            print("   Invalid option.")

# 40. Validate if a JSON file has required keys
def validate_json(required_keys):
    try:
        with open(JSON_FILE, "r") as file:
            data = json.load(file)
            for i, user in enumerate(data):
                for key in required_keys:
                    if key not in user:
                        raise KeyError(f"User {i+1} missing key: '{key}'")
        print("40. All profiles validated successfully.")
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"40. Error reading file: {e}")
    except KeyError as ke:
        print(f"40. Validation Error: {ke}")

# ------------------ Demo ------------------

save_user_profiles()
display_profiles()
add_user_profile("Charlie", 28, ["Java", "Spring"])
display_profiles()
validate_json(["name", "age", "skills"])

phonebook_app()
