# 1. Student Roll Call System
# Objective: Take attendance for a classroom.

print(" Student Roll Call System\n")

students = []
count = 0

# • Use a while loop to enter student names one by one.
while count < 10:
    name = input(f"Enter name of student {count + 1}: ").strip()

    # • Skip empty names using continue.
    if name == "":
        print(" Empty name! Try again.")
        continue

    students.append(name)
    count += 1

# • Use else after loop to print “Attendance completed!”
else:
    print("\n Attendance completed!")

# • Stop after a total of 10 students are entered.

print("\n Present Students:")
for i, student in enumerate(students, start=1):
    print(f"{i}. {student}")
