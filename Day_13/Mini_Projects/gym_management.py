# Base Member Class
class Member:
    total_members = 0  # Class Variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sessions = []
        Member.total_members += 1
        print(f" Member '{self.name}' registered. Total members: {Member.total_members}")

    def register_sessions(self, *args):  # Using *args
        self.sessions.extend(args)
        print(f" {self.name} registered for sessions: {', '.join(args)}")

    def view_schedule(self):
        print(f" {self.name}'s Sessions: {', '.join(self.sessions) if self.sessions else 'None'}")


# Trainer Class (inherits from Member)
class Trainer(Member):
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty = specialty

    def assign(self):
        print(f" Trainer {self.name} (Specialty: {self.specialty}) assigned.")


# Schedule Class
class Schedule:
    def __init__(self, time, session):
        self.time = time
        self.session = session

    def show(self):
        print(f" Schedule: {self.session} at {self.time}")


# Subscription Class with Overloading via __str__
class Subscription:
    def __init__(self, member, months):
        self.member = member
        self.months = months

    def __str__(self):
        return f" Subscription: {self.member.name} for {self.months} month(s)"


# Demo
if __name__ == "__main__":
    # Register Member
    m1 = Member("Alice", 28)
    m1.register_sessions("Yoga", "Zumba", "HIIT")
    m1.view_schedule()

    # Assign Trainer
    t1 = Trainer("Jake", 32, "Strength Training")
    t1.assign()

    # Add Schedule
    s1 = Schedule("6:00 AM", "Yoga")
    s1.show()

    # Create Subscription
    sub = Subscription(m1, 3)
    print(sub)

    # Show total members
    print(f"\n Total Registered Members: {Member.total_members}")
