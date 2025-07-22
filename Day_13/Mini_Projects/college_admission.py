# Base Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Department Class (Aggregation target)
class Department:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.admitted_students = []

    def allocate(self, student):
        if len(self.admitted_students) < self.capacity:
            self.admitted_students.append(student)
            print(f" {student.name} admitted to {self.name} department.")
        else:
            print(f" No seats left in {self.name} department.")

    def show_students(self):
        print(f"\n Students in {self.name} Department:")
        for s in self.admitted_students:
            print(f" {s.name}")

# Admission Form with basic validation
class AdmissionForm:
    def __init__(self, student, documents_submitted):
        self.__student = student  # Encapsulation
        self.__documents_submitted = documents_submitted

    def verify_documents(self):
        print(f" Verifying documents for {self.__student.name}...")
        if self.__documents_submitted:
            print(" All required documents submitted.")
            return True
        else:
            print(" Missing documents.")
            return False

# Student class (inherits from Person and aggregates Department)
class Student(Person):
    def __init__(self, name, age, department: Department):
        super().__init__(name, age)  # Call parent constructor
        self.department = department  # Aggregation

    def apply(self):
        form = AdmissionForm(self, documents_submitted=True)
        if form.verify_documents():
            self.department.allocate(self)
        else:
            print(f" {self.name}'s admission rejected due to incomplete documents.")

# Demo
if __name__ == "__main__":
    # Create departments
    cs = Department("Computer Science", 2)
    mech = Department("Mechanical", 1)

    # Create and apply students
    s1 = Student("Arjun", 18, cs)
    s2 = Student("Bhavna", 19, cs)
    s3 = Student("Chetan", 18, cs)  # Will exceed CS capacity
    s4 = Student("Divya", 20, mech)

    s1.apply()
    s2.apply()
    s3.apply()
    s4.apply()

    # Show department allocations
    cs.show_students()
    mech.show_students()
