class Receiver:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Receiver: {self.name}, Address: {self.address}"
