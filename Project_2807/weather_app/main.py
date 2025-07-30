from core.api import fetch_weather_data
from core.weather import Weather
from core.logger import log_weather

def main():
    while True:
        city = input("Enter city name (or 'exit'): ").strip()
        if city.lower() == 'exit':
            break
        try:
            data = fetch_weather_data(city)
            weather = Weather(city, data)
            print(weather)
            log_weather(str(weather))
            
            print("\nForecast (Next 3 Days):")
            for day in weather.forecast_generator():
                print(f"{day['date']}: {day['min_temp']}°C - {day['max_temp']}°C | {day['condition']}")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
