def suggest_destinations(trips):
    visited = set(trip["destination"].lower() for trip in trips)
    popular = {"paris", "london", "tokyo", "sydney", "new york"}
    suggestions = popular - visited
    if suggestions:
        print(" You might like to visit:")
        for place in suggestions:
            print(f"- {place.title()}")
    else:
        print(" You've visited all popular destinations!")
