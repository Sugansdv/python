# 11. Result Card Generator

# • Input subject marks using **kwargs
def generate_result(**marks):
    # • Use map() to grade each subject
    def grade(mark):
        if mark >= 90:
            return 'A'
        elif mark >= 75:
            return 'B'
        elif mark >= 60:
            return 'C'
        elif mark >= 35:
            return 'D'
        else:
            return 'F'

    graded = dict(zip(marks.keys(), map(grade, marks.values())))

    # • Return total, average, and status
    total = sum(marks.values())
    average = total / len(marks)
    status = "Pass" if all(m >= 35 for m in marks.values()) else "Fail"

    print("Subject Grades:", graded)
    return total, average, status

total, avg, status = generate_result(Math=88, English=77, Science=93, History=66, Tamil=81)
print(f"Total: {total} | Average: {avg} | Status: {status}")
