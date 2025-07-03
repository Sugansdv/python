## 6. Student Gradebook
print("========================================")
print("            Student Gradebook           ")
print("========================================")

# 1. Ask for a student's name and three subject scores
name = input("Enter student name: ")
score1 = float(input("Enter score for Subject 1: "))
score2 = float(input("Enter score for Subject 2: "))
score3 = float(input("Enter score for Subject 3: "))

# 2. Store data in a dictionary
student = {
    "Name": name,
    "Scores": [score1, score2, score3]
}

# 3. Calculate the average
average = sum(student["Scores"]) / len(student["Scores"])

# 4. Display results using f-strings
print("\n Student Report:")
print(f"Name      : {student['Name']}")
print(f"Scores    : {student['Scores']}")
print(f"Average   : {average:.2f}")

# 5. Show the type of the average
print(f"Type of average: {type(average)}")
