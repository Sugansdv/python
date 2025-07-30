class Weather:
    def __init__(self, city, data):
        self.city = city
        self.temp = data["current"]["temp_c"]
        self.humidity = data["current"]["humidity"]
        self.condition = data["current"]["condition"]["text"]
        self.forecast_data = data["forecast"]["forecastday"]

    def __str__(self):
        return f"{self.city} | {self.temp}°C | {self.humidity}% Humidity | {self.condition}"

    def forecast_generator(self):
        for day in self.forecast_data:
            yield {
                "date": day["date"],
                "max_temp": day["day"]["maxtemp_c"],
                "min_temp": day["day"]["mintemp_c"],
                "condition": day["day"]["condition"]["text"]
            }
