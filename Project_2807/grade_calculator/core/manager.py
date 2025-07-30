import csv
from core.student import Student
from core.memoize import memoize

class StudentManager:
    def __init__(self):
        self.students = {}  # id -> Student

    def add_student(self, student):
        if any(m < 0 or m > 100 for m in student.marks.values()):
            raise ValueError("Marks must be between 0 and 100.")
        self.students[student.id] = student

    @memoize
    def calculate_gpa(self, student):
        return round(student.average() / 10, 2)

    def top_student(self):
        return max(self.students.values(), key=lambda s: s.average(), default=None)

    def class_average(self):
        if not self.students:
            return 0
        return sum(s.average() for s in self.students.values()) / len(self.students)

    def export_grades(self, filepath="data/grades.csv"):
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "GPA", "Grade"])
            for student in self.students.values():
                writer.writerow([
                    student.id,
                    student.name,
                    self.calculate_gpa(student),
                    student.grade()
                ])
