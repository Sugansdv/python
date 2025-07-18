import statistics

def summarize(data, column):
    values = [float(row[column]) for row in data if row[column]]
    return {
        "min": min(values),
        "max": max(values),
        "mean": statistics.mean(values),
        "median": statistics.median(values)
    }
