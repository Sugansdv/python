from utils.file_handler import append_csv
import os

SUBJECT_FILE = os.path.join("data", "subjects.csv")

def assign_subject(subject, teacher_name):
    row = {"Subject": subject, "Teacher": teacher_name}
    append_csv(SUBJECT_FILE, row)
    print(f" Assigned subject '{subject}' to teacher '{teacher_name}'")
