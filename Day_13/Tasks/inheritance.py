# 11. Vehicle → Car, Bike, Truck
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_info(self):
        print(f"Vehicle Brand: {self.brand}")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

class Truck(Vehicle):
    pass

# 12. Use super() in Child Constructor
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def display(self):
        print(f"Dog Name: {self.name}, Breed: {self.breed}")

# 13. Shape → Square, Triangle — Override area()
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# 14. Multi-level Inheritance: Person → Employee → Manager
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

# 15. Multiple Inheritance: Father + Mother → Child
class Father:
    def skills(self):
        print("Programming")

class Mother:
    def hobbies(self):
        print("Painting")

class Child(Father, Mother):
    def interests(self):
        print("Video Games")

# 16. Hierarchical Inheritance: Teacher → MathTeacher, ScienceTeacher
class Teacher:
    def teach(self):
        print("Teaching subjects")

class MathTeacher(Teacher):
    def teach_math(self):
        print("Teaching Math")

class ScienceTeacher(Teacher):
    def teach_science(self):
        print("Teaching Science")

# 17. Use isinstance()
class Fruit:
    pass

class Apple(Fruit):
    pass

# 18. Use issubclass()
class A: pass
class B(A): pass

# 19. Product → ElectronicProduct → MobilePhone
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

class MobilePhone(ElectronicProduct):
    def __init__(self, name, price, brand, model):
        super().__init__(name, price, brand)
        self.model = model

# 20. MRO Example
class X:
    def msg(self): print("Class X")

class Y(X):
    def msg(self): print("Class Y")

class Z(X):
    def msg(self): print("Class Z")

class P(Y, Z):  # MRO: P → Y → Z → X
    pass


# ======================
# Run tasks
# ======================
if __name__ == "__main__":
    print("TASK 11: Inheritance - Vehicle subclasses")
    car = Car("Toyota")
    bike = Bike("Yamaha")
    truck = Truck("Tata")
    car.show_info()
    bike.show_info()
    truck.show_info()

    print("\nTASK 12: super() in Dog")
    d = Dog("Tommy", "Beagle")
    d.display()

    print("\nTASK 13: Override area()")
    sq = Square(4)
    tri = Triangle(5, 10)
    print("Square Area:", sq.area())
    print("Triangle Area:", tri.area())

    print("\nTASK 14: Multi-level Inheritance")
    mgr = Manager("Alice", 101, "HR")
    print(f"Name: {mgr.name}, ID: {mgr.emp_id}, Dept: {mgr.department}")

    print("\nTASK 15: Multiple Inheritance")
    c = Child()
    c.skills()
    c.hobbies()
    c.interests()

    print("\nTASK 16: Hierarchical Inheritance")
    mt = MathTeacher()
    st = ScienceTeacher()
    mt.teach()
    mt.teach_math()
    st.teach()
    st.teach_science()

    print("\nTASK 17: isinstance()")
    apple = Apple()
    print("Is apple instance of Fruit?", isinstance(apple, Fruit))

    print("\nTASK 18: issubclass()")
    print("Is B subclass of A?", issubclass(B, A))

    print("\nTASK 19: E-commerce Inheritance")
    phone = MobilePhone("Smartphone", 20000, "Samsung", "Galaxy A14")
    print(f"Product: {phone.name}, Price: ₹{phone.price}, Brand: {phone.brand}, Model: {phone.model}")

    print("\nTASK 20: MRO")
    p = P()
    p.msg()
    print("MRO of P:", [cls.__name__ for cls in P.__mro__])
