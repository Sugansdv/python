from collections import defaultdict

def monthly_summary(log):
    if not log:
        print("No data to summarize.")
        return
    monthly = defaultdict(list)
    for date, (temp, hum, _) in log.items():
        month = date[:7]  # YYYY-MM
        monthly[month].append((temp, hum))

    for month, entries in monthly.items():
        avg_temp = sum(t for t, _ in entries) / len(entries)
        avg_hum = sum(h for _, h in entries) / len(entries)
        print(f"{month}: Avg Temp: {avg_temp:.2f}°C, Avg Humidity: {avg_hum:.2f}%")

def unique_conditions(log):
    conditions = set(cond for _, (_, _, cond) in log.items())
    print("Unique Conditions Recorded:")
    for cond in conditions:
        print(f"- {cond}")
