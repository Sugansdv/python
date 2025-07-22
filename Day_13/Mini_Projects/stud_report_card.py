from typing import List, Dict

# Base Class
class Person:
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id_number

    def __str__(self):
        return f"{self.__name} (ID: {self.__id_number})"

# Subject Class
class Subject:
    def __init__(self, name):
        self.name = name
        self.marks = {}

    def set_mark(self, student_id, mark):
        self.marks[student_id] = mark

    def get_mark(self, student_id):
        return self.marks.get(student_id, None)

# Student Class
class Student(Person):
    def __init__(self, name, id_number, grade):
        super().__init__(name, id_number)
        self.grade = grade

    def __str__(self):
        return f"Student: {self.get_name()} | Grade: {self.grade}"

# Teacher Class
class Teacher(Person):
    def __init__(self, name, id_number, subject: Subject):
        super().__init__(name, id_number)
        self.subject = subject

    def update_mark(self, student: Student, mark: int):
        self.subject.set_mark(student.get_id(), mark)

# Report Card Class
class ReportCard:
    def __init__(self, student: Student, subjects: List[Subject]):
        self.student = student
        self.subjects = subjects

    def generate(self):
        print(f"\nReport Card for {self.student.get_name()} (Grade: {self.student.grade}):")
        total = 0
        count = 0
        for subject in self.subjects:
            mark = subject.get_mark(self.student.get_id())
            if mark is not None:
                print(f"- {subject.name}: {mark}")
                total += mark
                count += 1
            else:
                print(f"- {subject.name}: Not Available")

        if count > 0:
            average = total / count
            grade = self.calculate_grade(average)
            print(f"Average: {average:.2f} | Final Grade: {grade}")
        else:
            print("No marks available.")

    def calculate_grade(self, avg):
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "F"

# -------- Example Usage --------
if __name__ == "__main__":
    math = Subject("Mathematics")
    science = Subject("Science")

    student1 = Student("Alice", "S101", "10th")
    teacher1 = Teacher("Mr. Sharma", "T201", math)
    teacher2 = Teacher("Ms. Rina", "T202", science)

    teacher1.update_mark(student1, 88)
    teacher2.update_mark(student1, 92)

    report = ReportCard(student1, [math, science])
    report.generate()
