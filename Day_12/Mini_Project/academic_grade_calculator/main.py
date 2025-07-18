from gradesystem.report import generate_report
from gradesystem.utils import format_report

student = "Alice"
marks_data = {
    "Math": [88, 92, 79],
    "Science": [85, 90, 87],
    "English": [75, 80, 78],
    "History": [82, 84, 80]
}

report = generate_report(student, marks_data)
print(format_report(report))
