import csv
from core.decorators import unit_converter

class Person:
    def __init__(self, name, weight, height, unit="kg/cm"):
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive.")
        self.name = name
        self.weight, self.height = unit_converter(weight, height, unit)
        self.bmi = None
        self.bmi_category = None

    def calculate_bmi(self):
        self.bmi = self.weight / ((self.height / 100) ** 2)

    def classify_bmi(self):
        if self.bmi < 18.5:
            self.bmi_category = "Underweight"
        elif 18.5 <= self.bmi < 25:
            self.bmi_category = "Normal"
        elif 25 <= self.bmi < 30:
            self.bmi_category = "Overweight"
        else:
            self.bmi_category = "Obese"

    def save_to_file(self, filename):
        with open(filename, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.weight, self.height, f"{self.bmi:.2f}", self.bmi_category])

def get_obese_people(people):
    for person in people:
        if person.bmi_category == "Obese":
            yield person
