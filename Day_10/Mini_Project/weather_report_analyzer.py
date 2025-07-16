# 16. Weather Report Analyzer
# Description: Store temperature data by city.
# Requirements:
# - Structure: {city_name: [temps]}
# - Add new temperature each day
# - Calculate average per city
# - Sort cities by hottest average

weather_data = {
    "Chennai": [34, 36, 35],
    "Delhi": [38, 40, 39],
    "Mumbai": [30, 32, 31]
}

def add_temperature(city, temp):
    if city in weather_data:
        weather_data[city].append(temp)
    else:
        weather_data[city] = [temp]
    print(f"Temperature {temp}°C added for {city}.")

def calculate_averages():
    print("\nAverage Temperatures:")
    for city, temps in weather_data.items():
        avg = sum(temps) / len(temps)
        print(f"{city}: {avg:.2f}°C")

def sort_by_average_temp():
    averages = {
        city: sum(temps) / len(temps)
        for city, temps in weather_data.items()
    }
    sorted_cities = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    print("\nCities Sorted by Hottest Average:")
    for city, avg in sorted_cities:
        print(f"{city}: {avg:.2f}°C")

add_temperature("Chennai", 37)
add_temperature("Bangalore", 29)
calculate_averages()
sort_by_average_temp()
