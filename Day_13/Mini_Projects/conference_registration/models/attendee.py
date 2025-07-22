class Attendee:
    total_attendees = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Attendee.total_attendees += 1

    def __str__(self):
        return f"{self.name} ({self.email})"

    @classmethod
    def get_total_attendees(cls):
        return cls.total_attendees
