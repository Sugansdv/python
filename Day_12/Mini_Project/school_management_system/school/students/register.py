from utils.file_handler import load_json, save_json
import os

STUDENT_FILE = os.path.join("data", "students.json")

def register_student(name, grade):
    data = load_json(STUDENT_FILE)
    student = {"name": name, "grade": grade}
    data.append(student)
    save_json(STUDENT_FILE, data)
    print(f" Registered student: {name}")
