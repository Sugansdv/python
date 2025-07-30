class Student:
    def __init__(self, student_id, name, marks):
        self.id = student_id
        self.name = name
        self.marks = marks  # dict: subject -> score (0-100)

    def average(self):
        return sum(self.marks.values()) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        elif avg >= 50:
            return 'E'
        else:
            return 'F'
