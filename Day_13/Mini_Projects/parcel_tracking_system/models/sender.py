class Sender:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Sender: {self.name}, Address: {self.address}"
