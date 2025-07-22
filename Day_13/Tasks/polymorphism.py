# 31. Method Overriding
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# 32. Duck Typing Example
class Circle:
    def draw(self):
        print("Drawing a circle")

class Rectangle:
    def draw(self):
        print("Drawing a rectangle")

def render_shape(shape):
    shape.draw()

# 33. Simulate Overloading using Default Arguments
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# 34. Simulate Overloading using *args
class Sum:
    def add(self, *args):
        return sum(args)

# 35. Notification Subclasses
class Notification:
    def send(self, msg):
        print(f"Sending: {msg}")

class SMS(Notification):
    def send(self, msg):
        print(f"Sending SMS: {msg}")

class Email(Notification):
    def send(self, msg):
        print(f"Sending Email: {msg}")

class PushNotification(Notification):
    def send(self, msg):
        print(f"Sending Push Notification: {msg}")


# =======================
# Run Polymorphism Tasks
# =======================
if __name__ == "__main__":
    print("TASK 31: Method Overriding")
    a = Animal()
    d = Dog()
    a.speak()
    d.speak()

    print("\nTASK 32: Duck Typing")
    c = Circle()
    r = Rectangle()
    render_shape(c)
    render_shape(r)

    print("\nTASK 33: Simulated Overloading with Default Arguments")
    calc = Calculator()
    print("add(2, 3):", calc.add(2, 3))
    print("add(2, 3, 4):", calc.add(2, 3, 4))

    print("\nTASK 34: Simulated Overloading with *args")
    s = Sum()
    print("add(2, 3):", s.add(2, 3))
    print("add(1, 2, 3, 4, 5):", s.add(1, 2, 3, 4, 5))

    print("\nTASK 35: Notification Polymorphism")
    notifiers = [SMS(), Email(), PushNotification()]
    for n in notifiers:
        n.send("Hello, world!")
