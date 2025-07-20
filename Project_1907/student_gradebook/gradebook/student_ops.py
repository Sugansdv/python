def add_student(students, roll, name):
    key = (roll, name)
    for s in students:
        if s['info'] == key:
            print(" Student already exists.")
            return
    students.append({"info": key, "grades": {}})
    print(f" Student {name} added.")

def update_grades(students, roll, subject, marks):
    for s in students:
        if s['info'][0] == roll:
            s['grades'][subject] = marks
            print(f" Updated {subject} marks for {s['info'][1]}")
            return
    print(" Student not found.")

def calculate_averages(students):
    print("\n Averages:")
    for s in students:
        grades = s['grades']
        if grades:
            avg = sum(grades.values()) / len(grades)
            print(f"{s['info'][1]} (Roll: {s['info'][0]}): {avg:.2f}")
        else:
            print(f"{s['info'][1]} (Roll: {s['info'][0]}): No grades")

def find_top_students(students):
    max_avg = 0
    toppers = []
    for s in students:
        grades = s['grades']
        if grades:
            avg = sum(grades.values()) / len(grades)
            if avg > max_avg:
                max_avg = avg
                toppers = [s]
            elif avg == max_avg:
                toppers.append(s)
    if toppers:
        print(f" Top Performer(s) with Avg {max_avg:.2f}:")
        for s in toppers:
            print(f" - {s['info'][1]} (Roll: {s['info'][0]})")
    else:
        print(" No grades available.")
