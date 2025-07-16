# 19. City Distance Map
# Description: Store distances between cities.
# Requirements:
# - Nested format: {city1: {city2: distance}}
# - Query distance between two cities
# - Update distances
# - Find shortest route using min value

city_map = {
    "Chennai": {"Bangalore": 350, "Hyderabad": 630},
    "Bangalore": {"Chennai": 350, "Hyderabad": 500},
    "Hyderabad": {"Chennai": 630, "Bangalore": 500}
}

def get_distance(from_city, to_city):
    distance = city_map.get(from_city, {}).get(to_city)
    if distance is not None:
        print(f"Distance from {from_city} to {to_city} is {distance} km.")
    else:
        print(f"No route found from {from_city} to {to_city}.")

def update_distance(from_city, to_city, distance):
    city_map.setdefault(from_city, {})[to_city] = distance
    city_map.setdefault(to_city, {})[from_city] = distance  
    print(f"Distance between {from_city} and {to_city} updated to {distance} km.")

def find_shortest_route(from_city):
    if from_city in city_map:
        routes = city_map[from_city]
        if routes:
            shortest = min(routes.items(), key=lambda x: x[1])
            print(f"Shortest route from {from_city} is to {shortest[0]} ({shortest[1]} km).")
        else:
            print(f"No routes from {from_city}.")
    else:
        print(f"{from_city} not found in map.")

get_distance("Chennai", "Hyderabad")
update_distance("Chennai", "Mumbai", 1030)
get_distance("Chennai", "Mumbai")
find_shortest_route("Chennai")
