# ==== MINI PROJECT 13: EMPLOYEE BONUS REPORT GENERATOR ====

print("====================")
print("Employee Bonus Report Generator")
print("====================")

# Use a list of employees and their scores
employees = [
    ("Arun", 92),
    ("Banu", 85),
    ("Charan", 74),
    ("Divya", 60),
    ("Elan", 90)
]

# Loop through each employee
for name, score in employees:
    # If score ≥ 90: Excellent → ₹10,000
    if score >= 90:
        bonus = 10000
        remark = "Excellent"
    # If 75–89: Good → ₹5,000
    elif score >= 75:
        bonus = 5000
        remark = "Good"
    # Else: ₹2,000
    else:
        bonus = 2000
        remark = "Needs Improvement"
    
    # Use f-string to display formatted bonus report
    print(f"{name}: {remark} Performance → Bonus ₹{bonus}")
