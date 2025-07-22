from people.student import Student
from people.instructor import Instructor

class Course:
    def __init__(self, title, instructor):
        self.title = title
        self.instructor = instructor
        self.students = []
        self.assignments = []

    def enroll(self, student):
        self.students.append(student)
        print(f"{student.name} enrolled in {self.title}")

    def add_assignment(self, assignment):
        self.assignments.append(assignment)
        print(f"Assignment '{assignment.title}' added to {self.title}")

    def show_course_info(self):
        print(f"\nCourse: {self.title}")
        print(f"Instructor: {self.instructor.name}")
        print("Students Enrolled:")
        for s in self.students:
            print(f"- {s.name}")
