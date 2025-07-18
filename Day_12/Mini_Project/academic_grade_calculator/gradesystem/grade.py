def calculate_cgpa(averages):
    return sum(averages) / len(averages)

def get_grade(cgpa):
    if cgpa >= 9:
        return 'A+'
    elif cgpa >= 8:
        return 'A'
    elif cgpa >= 7:
        return 'B'
    elif cgpa >= 6:
        return 'C'
    elif cgpa >= 5:
        return 'D'
    else:
        return 'F'
