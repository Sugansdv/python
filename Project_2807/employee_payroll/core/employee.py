class Employee:
    def __init__(self, emp_id, name, hours, rate):
        if hours < 0 or rate < 0:
            raise ValueError("Hours and rate must be non-negative.")
        self.emp_id = emp_id
        self.name = name
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        base = self.hours * self.rate
        bonus = 0
        if self.hours > 40:
            bonus = (self.hours - 40) * (self.rate * 0.5)
        gross = base + bonus
        tax = self.calculate_tax(gross)
        return gross - tax, tax

    def calculate_tax(self, amount):
        if amount <= 1000:
            return amount * 0.1
        elif amount <= 2000:
            return amount * 0.15
        else:
            return amount * 0.2

    def __str__(self):
        return f"{self.emp_id} - {self.name}"
