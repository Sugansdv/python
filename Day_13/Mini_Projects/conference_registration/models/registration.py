class Registration:
    def __init__(self, attendee, event):
        self.attendee = attendee
        self.event = event
        self.assigned_sessions = []

    def assign_session(self, session):
        self.assigned_sessions.append(session)

    def __str__(self):
        sessions = "\n  ".join(str(s) for s in self.assigned_sessions)
        return f"Registration for {self.attendee}:\n  Sessions:\n  {sessions if sessions else 'No sessions assigned'}"
