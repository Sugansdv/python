# 12. Daily Temperature Logger
# Goal: Track and analyze daily temperatures.
# Requirements:
# • Store temperatures as (date, (morning_temp, evening_temp))
# • Use slicing to get data for last 7 days.
# • Find highest evening temperature using max().
# • Use unpacking in analysis reports.

# List of daily temperatures
temperature_log = [
    ("2025-07-01", (24.5, 32.1)),
    ("2025-07-02", (25.0, 33.4)),
    ("2025-07-03", (23.8, 31.7)),
    ("2025-07-04", (24.2, 34.0)),
    ("2025-07-05", (25.5, 35.2)),
    ("2025-07-06", (24.9, 33.8)),
    ("2025-07-07", (23.5, 30.5)),
    ("2025-07-08", (22.8, 31.2)),
    ("2025-07-09", (24.3, 34.6))
]

# Get last 7 days
recent_days = temperature_log[-7:]

print(" Last 7 Days Temperature Report:\n")
for date, (morning, evening) in recent_days:
    print(f"{date} → Morning: {morning}°C, Evening: {evening}°C")

# Find highest evening temperature
highest_evening = max(recent_days, key=lambda t: t[1][1])
print(f"\n Highest Evening Temperature: {highest_evening[0]} - {highest_evening[1][1]}°C")
