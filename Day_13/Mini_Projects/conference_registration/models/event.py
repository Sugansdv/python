class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)

    def __str__(self):
        return f"Event: {self.name} on {self.date}"
