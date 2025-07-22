# === 41. Car with Engine (Composition) ===
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP started.")


class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower)

    def drive(self):
        self.engine.start()
        print(f"{self.brand} is now driving.")


# === 42. Library with Books (Aggregation) ===
class Book:
    def __init__(self, title):
        self.title = title


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to {self.name} Library")

    def list_books(self):
        print(f"\nBooks in {self.name} Library:")
        for book in self.books:
            print(f"- {book.title}")


# === 43. University with Departments (Composition) ===
class Department:
    def __init__(self, name):
        self.name = name


class University:
    def __init__(self, uni_name):
        self.uni_name = uni_name
        self.departments = []

    def add_department(self, dept_name):
        dept = Department(dept_name)
        self.departments.append(dept)

    def show_departments(self):
        print(f"\nDepartments in {self.uni_name}:")
        for d in self.departments:
            print(f"- {d.name}")


# === 44. Company with Employees (Aggregation) ===
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def hire(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} hired by {self.name}")

    def list_employees(self):
        print(f"\nEmployees at {self.name}:")
        for emp in self.employees:
            print(f"- {emp.name} (ID: {emp.emp_id})")


# === 45. Flight with Pilot, Crew, and Passengers ===
class Pilot:
    def __init__(self, name):
        self.name = name


class CabinCrew:
    def __init__(self, name):
        self.name = name


class Passenger:
    def __init__(self, name):
        self.name = name


class Flight:
    def __init__(self, flight_number, pilot):
        self.flight_number = flight_number
        self.pilot = pilot
        self.cabin_crew = []
        self.passengers = []

    def add_crew(self, crew_member):
        self.cabin_crew.append(crew_member)

    def board_passenger(self, passenger):
        self.passengers.append(passenger)

    def show_details(self):
        print(f"\nFlight {self.flight_number}")
        print(f"Pilot: {self.pilot.name}")
        print("Cabin Crew:")
        for crew in self.cabin_crew:
            print(f"- {crew.name}")
        print("Passengers:")
        for p in self.passengers:
            print(f"- {p.name}")


# === Run All Examples ===
if __name__ == "__main__":
    print("\n== 41. Car Example ==")
    car = Car("Toyota", 150)
    car.drive()

    print("\n== 42. Library Example ==")
    b1 = Book("Python Crash Course")
    b2 = Book("Clean Code")
    lib = Library("City Library")
    lib.add_book(b1)
    lib.add_book(b2)
    lib.list_books()

    print("\n== 43. University Example ==")
    uni = University("Tech University")
    uni.add_department("Computer Science")
    uni.add_department("Mathematics")
    uni.show_departments()

    print("\n== 44. Company Example ==")
    e1 = Employee("Alice", 101)
    e2 = Employee("Bob", 102)
    comp = Company("TechCorp")
    comp.hire(e1)
    comp.hire(e2)
    comp.list_employees()

    print("\n== 45. Flight Example ==")
    pilot = Pilot("Captain John")
    flight = Flight("AI202", pilot)
    flight.add_crew(CabinCrew("Mary"))
    flight.add_crew(CabinCrew("Tom"))
    flight.board_passenger(Passenger("Alice"))
    flight.board_passenger(Passenger("Bob"))
    flight.show_details()
