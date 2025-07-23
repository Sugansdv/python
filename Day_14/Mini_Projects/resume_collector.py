import json
import os

FILE = "resumes.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_resume():
    name = input("Enter full name: ").strip()
    email = input("Enter email: ").strip()
    phone = input("Enter phone: ").strip()
    skills = input("Enter skills (comma separated): ").strip().split(",")
    experience = input("Enter years of experience: ").strip()

    resumes = load_data()
    resumes[name] = {
        "email": email,
        "phone": phone,
        "skills": [skill.strip() for skill in skills],
        "experience": experience
    }

    save_data(resumes)
    print(f" Resume for {name} saved.")

def view_resume():
    name = input("Enter candidate name to search: ").strip()
    resumes = load_data()

    if name in resumes:
        data = resumes[name]
        print(f"\n Resume for {name}")
        print(f"Email: {data['email']}")
        print(f"Phone: {data['phone']}")
        print(f"Skills: {', '.join(data['skills'])}")
        print(f"Experience: {data['experience']} years")
    else:
        print(" Resume not found.")

def update_resume():
    name = input("Enter name to update: ").strip()
    resumes = load_data()

    if name not in resumes:
        print(" Resume not found.")
        return

    print("Enter new details (leave blank to keep current):")
    email = input(f"New email [{resumes[name]['email']}]: ").strip()
    phone = input(f"New phone [{resumes[name]['phone']}]: ").strip()
    skills = input(f"New skills (comma separated) [{', '.join(resumes[name]['skills'])}]: ").strip()
    experience = input(f"New experience [{resumes[name]['experience']}]: ").strip()

    if email:
        resumes[name]['email'] = email
    if phone:
        resumes[name]['phone'] = phone
    if skills:
        resumes[name]['skills'] = [s.strip() for s in skills.split(",")]
    if experience:
        resumes[name]['experience'] = experience

    save_data(resumes)
    print(f" Resume for {name} updated.")

def main():
    while True:
        print("\n Resume Collector Menu")
        print("1. Add Resume")
        print("2. View Resume")
        print("3. Update Resume")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_resume()
        elif choice == "2":
            view_resume()
        elif choice == "3":
            update_resume()
        elif choice == "4":
            print(" Exiting Resume Collector.")
            break
        else:
            print(" Invalid option.")

if __name__ == "__main__":
    main()
