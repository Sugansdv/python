class Session:
    def __init__(self, title, speaker, time):
        self.title = title
        self.speaker = speaker
        self.time = time

    def __str__(self):
        return f"Session: {self.title} by {self.speaker} at {self.time}"
