from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_details(self):
        pass


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def get_details(self):
        return f"Student: {self.name}, ID: {self.student_id}, Grades: {self.grades}"


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def get_details(self):
        return f"Teacher: {self.name}, Subject: {self.subject}"

# Example
s1 = Student("Alice", "STU101")
s1.add_grade("Math", "A")
t1 = Teacher("Mr. Smith", "Math")
print(s1.get_details())
print(t1.get_details())
