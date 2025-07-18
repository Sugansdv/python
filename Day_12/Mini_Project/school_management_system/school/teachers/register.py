from utils.file_handler import load_json, save_json
import os

TEACHER_FILE = os.path.join("data", "teachers.json")

def register_teacher(name, subject):
    data = load_json(TEACHER_FILE)
    teacher = {"name": name, "subject": subject}
    data.append(teacher)
    save_json(TEACHER_FILE, data)
    print(f" Registered teacher: {name}")
