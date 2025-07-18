import json
import os

def collect_input():
    print("🔧 Enter your resume details:")
    data = {
        "name": input("Full Name: "),
        "email": input("Email: "),
        "phone": input("Phone: "),
        "summary": input("Professional Summary: "),
        "skills": input("Skills (comma-separated): ").split(","),
        "experience": [],
        "education": []
    }

    print("\n➕ Add Work Experience:")
    while True:
        title = input("Job Title (leave blank to stop): ")
        if not title.strip():
            break
        company = input("Company: ")
        years = input("Years (e.g. 2020-2022): ")
        desc = input("Description: ")
        data["experience"].append({
            "title": title, "company": company, "years": years, "description": desc
        })

    print("\n➕ Add Education:")
    while True:
        degree = input("Degree (leave blank to stop): ")
        if not degree.strip():
            break
        institute = input("Institute: ")
        year = input("Year: ")
        data["education"].append({
            "degree": degree, "institute": institute, "year": year
        })

    return data

def load_input_from_json(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("JSON file not found.")
    with open(file_path, 'r') as f:
        return json.load(f)
