#20. Marks to Grade Converter
# • Accept list of marks
marks = list(map(int, input("Enter marks separated by space: ").split()))

# • Convert to grade using conditions (A, B, etc.)
def convert_to_grade(mark):
    if mark >= 90:
        return 'A'
    elif mark >= 75:
        return 'B'
    elif mark >= 60:
        return 'C'
    elif mark >= 40:
        return 'D'
    else:
        return 'F'

# • Return final graded list
graded_list = list(map(lambda m: convert_to_grade(m), marks))

print("\nGrades:", graded_list)
