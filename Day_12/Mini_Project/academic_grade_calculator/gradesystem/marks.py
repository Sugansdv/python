class InvalidMarksError(Exception):
    pass

def validate_marks(marks):
    if not all(0 <= mark <= 100 for mark in marks):
        raise InvalidMarksError("Marks should be between 0 and 100.")
    return True

def calculate_average(marks):
    validate_marks(marks)
    return sum(marks) / len(marks)
