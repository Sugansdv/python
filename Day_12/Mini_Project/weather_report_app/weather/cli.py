from weather import api as weather_api
from weather import formatter as weather_formatter

def start_cli():
    print("=== 🌦️ Weather Report App ===")
    city = input("Enter city name: ").strip()

    data = weather_api.get_weather(city)
    result = weather_formatter.format_weather(data)
    print(result)
