import re

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        if not re.match(r"^\d{10}$", phone):
            raise ValueError("Invalid phone number format. Must be 10 digits.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"
