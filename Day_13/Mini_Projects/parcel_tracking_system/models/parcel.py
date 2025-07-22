from .tracking import Tracking

class Parcel:
    def __init__(self, sender, receiver, weight):
        self.sender = sender
        self.receiver = receiver
        self.weight = weight
        self.tracking = Tracking.generate_tracking(self)

    def __str__(self):
        return (f"{self.sender}\n{self.receiver}\n"
                f"Weight: {self.weight}kg\nTracking ID: {self.tracking}")
