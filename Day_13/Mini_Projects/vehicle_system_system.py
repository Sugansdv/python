from datetime import datetime

# Base Vehicle class
class Vehicle:
    vehicle_count = 0  # Class variable

    def __init__(self, vehicle_id, brand, base_rate):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.base_rate = base_rate
        self.available = True
        Vehicle.vehicle_count += 1

    def calculate_rent(self, days):
        return self.base_rate * days  # To be overridden in subclasses

    def __str__(self):
        return f"{self.brand} (ID: {self.vehicle_id}, Available: {self.available})"

    @classmethod
    def total_vehicles(cls):
        return cls.vehicle_count

    @staticmethod
    def date_diff(start_date, end_date):
        return (end_date - start_date).days

# Bike class
class Bike(Vehicle):
    def calculate_rent(self, days):
        return super().calculate_rent(days) * 0.9  # 10% discount

# Car class
class Car(Vehicle):
    def calculate_rent(self, days):
        return super().calculate_rent(days) + (50 * days)  # Extra charge

# Customer class
class Customer:
    def __init__(self, name):
        self.name = name
        self.rented_vehicle = None
        self.rent_date = None

    def rent_vehicle(self, vehicle, rent_date):
        if vehicle.available:
            self.rented_vehicle = vehicle
            self.rent_date = rent_date
            vehicle.available = False
            print(f"{self.name} rented {vehicle}")
        else:
            print(f"{vehicle} is not available.")

    def return_vehicle(self, return_date):
        if self.rented_vehicle:
            days = Vehicle.date_diff(self.rent_date, return_date)
            rent = self.rented_vehicle.calculate_rent(days)
            print(f"{self.name} returned {self.rented_vehicle}")
            print(f"Total Rent for {days} days: ₹{rent}")
            self.rented_vehicle.available = True
            self.rented_vehicle = None
        else:
            print("No vehicle to return.")

# Rental system
if __name__ == "__main__":
    # Create vehicles
    bike1 = Bike("B101", "Yamaha", 200)
    car1 = Car("C202", "Honda", 500)

    # Create customer
    cust1 = Customer("Sneha")

    # Rent a vehicle
    rent_date = datetime(2025, 7, 20)
    cust1.rent_vehicle(bike1, rent_date)

    # Return the vehicle
    return_date = datetime(2025, 7, 23)
    cust1.return_vehicle(return_date)

    # Show total vehicles
    print("Total vehicles in system:", Vehicle.total_vehicles())
