print("=======================================")
print("     Student Grade Evaluator           ")
print("=======================================\n")

# Input: name and marks in 5 subjects
name = input("Enter your name: ")
m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))
m4 = float(input("Enter marks for Subject 4: "))
m5 = float(input("Enter marks for Subject 5: "))

# Arithmetic: Calculate average
total = m1 + m2 + m3 + m4 + m5
average = total / 5  # Assignment + arithmetic

# Comparison and logical operators with if-elif-else
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
else:
    grade = "D"

# Display using f-string
print("\n========== Student Report ==========")
print(f"Student Name      : {name}")
print(f"Total Marks       : {total}/500")
print(f"Average Percentage: {average:.2f}%")
print(f"Grade             : {grade}")
print("=====================================")