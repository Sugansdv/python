class Assignment:
    def __init__(self, title):
        self.title = title

    def submit(self, student):
        student.submit(self)

class CodingAssignment(Assignment):
    def submit(self, student):
        print(f"{student.name} pushed code for: {self.title}")
        student.submitted_assignments.append(self)

class EssayAssignment(Assignment):
    def submit(self, student):
        print(f"{student.name} uploaded document for: {self.title}")
        student.submitted_assignments.append(self)
