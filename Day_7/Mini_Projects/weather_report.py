#12. Weather Report Generator
# Input: city name, temperature (°C), and humidity
city = input("Enter city name: ")         
temp = input("Enter temperature (°C): ")   
humidity = input("Enter humidity (%): ")  

# Using f-string
report_fstring = f"Weather in {city}: {temp}°C, {humidity}% humidity"

# Using + (string concatenation)
report_plus = "Weather in " + city + ": " + temp + "°C, " + humidity + "% humidity"

# Using .format()
report_format = "Weather in {}: {}°C, {}% humidity".format(city, temp, humidity)

# Print all three formatted reports
print("\nUsing f-string:     ", report_fstring)
print("Using + operator:   ", report_plus)
print("Using .format():    ", report_format)
