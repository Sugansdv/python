from abc import ABC, abstractmethod

# 26. Abstract class Payment with pay() method
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")

# 27. Shape with abstract area() and concrete describe()
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print("This is a 2D shape.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# 28. Animal abstract class with speak()
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")

# 29. Transport abstract class
class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Transport):
    def start_engine(self):
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")

# 30. Appliance abstract class with power_consumption()
class Appliance(ABC):
    @abstractmethod
    def power_consumption(self):
        pass

class Fridge(Appliance):
    def power_consumption(self):
        return "Fridge consumes 150W"

class WashingMachine(Appliance):
    def power_consumption(self):
        return "Washing Machine consumes 500W"


# ====================
# Run Abstraction
# ====================
if __name__ == "__main__":
    print("TASK 26: Payment Abstraction")
    p1 = CreditCardPayment()
    p2 = PayPalPayment()
    p1.pay(1000)
    p2.pay(500)

    print("\nTASK 27: Shape Abstraction")
    c = Circle(5)
    c.describe()
    print("Area of Circle:", c.area())

    print("\nTASK 28: Animal Abstraction")
    d = Dog()
    cat = Cat()
    d.speak()
    cat.speak()

    print("\nTASK 29: Transport Abstraction")
    my_car = Car()
    my_car.start_engine()
    my_car.stop_engine()

    print("\nTASK 30: Appliance Abstraction")
    fridge = Fridge()
    wm = WashingMachine()
    print(fridge.power_consumption())
    print(wm.power_consumption())
