from abc import ABC, abstractmethod
from datetime import datetime

# Abstract Base Class
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_role(self):
        pass

# Doctor class (inherits Person)
class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def get_role(self):
        return "Doctor"

    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"

# Patient class (inherits Person)
class Patient(Person):
    def __init__(self, name, age, ailment):
        super().__init__(name, age)
        self.ailment = ailment

    def get_role(self):
        return "Patient"

    def __str__(self):
        return f"{self.name} (Ailment: {self.ailment})"

# Prescription class
class Prescription:
    def __init__(self, medicines, instructions):
        self.medicines = medicines
        self.instructions = instructions

    def __str__(self):
        return f"Medicines: {', '.join(self.medicines)}\nInstructions: {self.instructions}"

# Appointment class (Aggregation of Doctor & Patient)
class Appointment:
    def __init__(self, doctor, patient, date):
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.prescription = None

    def assign_prescription(self, medicines, instructions):
        self.prescription = Prescription(medicines, instructions)

    def __str__(self):
        info = (
            f"Appointment:\nDoctor: {self.doctor}\n"
            f"Patient: {self.patient}\n"
            f"Date: {self.date.strftime('%Y-%m-%d')}\n"
        )
        if self.prescription:
            info += f"--- Prescription ---\n{self.prescription}\n"
        else:
            info += "No prescription added.\n"
        return info

# Sample usage
if __name__ == "__main__":
    doc = Doctor("Priya Sharma", 45, "Cardiologist")
    pat = Patient("Ravi Kumar", 52, "Chest Pain")

    appt = Appointment(doc, pat, datetime(2025, 7, 22))
    appt.assign_prescription(["Aspirin", "Beta Blockers"], "Take after meals")

    print(appt)
