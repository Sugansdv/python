class Student:
    def __init__(self, name):
        self.name = name
        self.submitted_assignments = []

    def submit(self, assignment):
        print(f"{self.name} submitted: {assignment.title}")
        self.submitted_assignments.append(assignment)
