#2. Email Template Customizer
# Input: name, course, duration
name = input("Enter your name: ")            
course = input("Enter your course name: ")   
duration = input("Enter duration in days: ")

# Template: "Dear {name}, your {course} course starts in {duration} days."
template = "Dear {name}, your {course} course starts in {duration} days."

# Replace placeholders using .format()
customized_email = template.format(name=name, course=course, duration=duration)
print(customized_email)

