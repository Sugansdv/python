def format_weather(data):
    if "error" in data:
        return f" Error fetching weather: {data['error']}"

    return (
        f"\n Weather in {data['city']}\n"
        f" Time: {data['datetime']}\n"
        f" Temp: {data['temp']}°C\n"
        f" Humidity: {data['humidity']}%\n"
        f" Wind Speed: {data['wind']} m/s\n"
        f" Description: {data['description'].capitalize()}\n"
    )
