#  9. Fuel Filling Simulation
# Objective: Simulate filling fuel up to 50L.

total_fuel = 0
fuel_limit = 50

# • Use while to repeatedly ask how much fuel to add.
while total_fuel < fuel_limit:
    try:
        fuel = float(input(" Enter fuel to add (in liters): "))

        # • Use continue for zero or negative values.
        if fuel <= 0:
            print(" Invalid amount. Must be greater than 0.")
            continue

        total_fuel += fuel
        print(f" Added {fuel}L | Total: {total_fuel}L")

        # • Stop when 50L is reached.
        if total_fuel >= fuel_limit:
            print(" Tank is full (50L reached).")
            break

    except ValueError:
        print(" Please enter a valid number.")
