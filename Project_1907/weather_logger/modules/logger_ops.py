def add_weather_data(log):
    date = input("Enter date (YYYY-MM-DD): ").strip()
    if date in log:
        print("Data for this date already exists.")
        return
    try:
        temp = float(input("Temperature (°C): "))
        humidity = float(input("Humidity (%): "))
        condition = input("Condition (e.g., Sunny, Rainy): ").strip()
        log[date] = (temp, humidity, condition)
        print("Weather data added.")
    except ValueError:
        print("Invalid input. Please enter numeric values for temperature and humidity.")

def view_weather_data(log):
    if not log:
        print("No weather data available.")
        return
    for date, (temp, hum, cond) in sorted(log.items()):
        print(f"{date}: {temp}°C, {hum}%, {cond}")
