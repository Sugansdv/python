from people.student import Student
from people.instructor import Instructor
from course import Course
from assignment import CodingAssignment, EssayAssignment

# Create instructor and course
instructor = Instructor("Dr. Smith")
course = Course("Python Programming", instructor)

# Create students
s1 = Student("Alice")
s2 = Student("Bob")

# Enroll students
course.enroll(s1)
course.enroll(s2)

# Create assignments
a1 = CodingAssignment("OOP Project")
a2 = EssayAssignment("Design Principles Essay")

# Add assignments to course
course.add_assignment(a1)
course.add_assignment(a2)

# Students submit assignments
a1.submit(s1)
a2.submit(s2)

# Show course info
course.show_course_info()
