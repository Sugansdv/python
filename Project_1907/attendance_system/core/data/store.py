import json
import os

DATA_FILE = "core/data/attendance_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            students = [tuple(s) for s in data.get("students", [])]
            attendance = {k: set(v) for k, v in data.get("attendance", {}).items()}
            return students, attendance
    else:
        # Default student list
        students = [
            ("S001", "Alice"),
            ("S002", "Bob"),
            ("S003", "Charlie"),
        ]
        attendance = {}
        return students, attendance

def save_data(students, attendance):
    with open(DATA_FILE, "w") as f:
        data = {
            "students": list(students),
            "attendance": {k: list(v) for k, v in attendance.items()}
        }
        json.dump(data, f, indent=4)
        print("✅ Data saved successfully.")
