import csv

CSV_FILE = "students.csv"

# 31. Create a CSV file with student names and marks
def create_csv():
    data = [
        ["Name", "Marks"],
        ["Alice", 85],
        ["Bob", 78],
        ["Charlie", 92],
        ["David", 60],
        ["Eva", 88]
    ]
    with open(CSV_FILE, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("31. CSV file created with initial student data.")

# 32. Read CSV and print students with marks > 80
def high_scorers():
    print("32. Students scoring >80:")
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["Marks"]) > 80:
                print(f"   {row['Name']} - {row['Marks']}")

# 33. Append new student data to the CSV file
def append_student(name, marks):
    with open(CSV_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, marks])
    print(f"33. Appended student: {name}, Marks: {marks}")

# 34. Convert CSV to dictionary (name: marks)
def csv_to_dict():
    student_dict = {}
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_dict[row["Name"]] = int(row["Marks"])
    print("34. CSV converted to dictionary:\n", student_dict)
    return student_dict

# 35. Summarize highest and average marks
def summarize_marks():
    marks = []
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            marks.append(int(row["Marks"]))
    if marks:
        highest = max(marks)
        average = sum(marks) / len(marks)
        print(f"35. Summary Report:\n   Highest Marks: {highest}\n   Average Marks: {average:.2f}")
    else:
        print("35. No marks found in the file.")

# ------------------ Test / Run Section ------------------

create_csv()
high_scorers()
append_student("Frank", 91)
append_student("Grace", 76)
csv_to_dict()
summarize_marks()
