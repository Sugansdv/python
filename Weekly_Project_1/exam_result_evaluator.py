# Online Exam Result Evaluator

# Take 5 subject marks using a list
marks = [45, 78, 89, 90, 55]  # You can change values to test different cases

# Use a for loop to calculate total and percentage
total = 0
for mark in marks:
    total += mark

percentage = total / len(marks)

# Check if any subject is less than 35 → Fail
fail_flag = False
for mark in marks:
    if mark < 35:
        fail_flag = True
        break

# Use conditions : else use if-elif for grade based on percentage.
if fail_flag:
    result = "Fail"
    division = "-"
else:
    result = "Pass"
    if percentage >= 75:
        division = "Distinction"
    elif percentage >= 60:
        division = "First Division"
    elif percentage >= 50:
        division = "Second Division"
    elif percentage >= 35:
        division = "Third Division"
    else:
        division = "Fail"

print("\n===== Online Exam Result =====")
print(f"Marks      : {marks}")
print(f"Total      : {total}")
print(f"Percentage : {percentage:.2f}%")
print(f"Result     : {result}")
print(f"Division   : {division}")
print("==============================")
