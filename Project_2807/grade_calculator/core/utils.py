def grade_a_students(students):
    for student in students.values():
        if student.grade() == 'A':
            yield student

def unique_subjects(students):
    subjects = set()
    for student in students.values():
        subjects.update(student.marks.keys())
    return subjects
