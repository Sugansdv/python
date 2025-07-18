

def calculate_average(marks):
    return sum(marks.values()) / len(marks)


def assign_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'


def validate_subjects(subjects):
    return set(subjects)
