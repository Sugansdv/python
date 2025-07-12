# 6. Movie Watchlist App
# Description: Users can manage a list of movies to watch.

# Initialize the movie watchlist
watchlist = ["Inception", "Interstellar", "The Matrix", "Parasite", "The Godfather", "Shutter Island"]

# Print the watchlist with index using a loop
print("Your Movie Watchlist:")
for index, movie in enumerate(watchlist, start=1):
    print(f"{index}. {movie}")

# Add movies to the list
watchlist.append("Oppenheimer")
watchlist.append("Joker")
print("\nAdded 'Oppenheimer' and 'Joker' to the watchlist.")

# Mark as watched (remove a movie)
watched_movie = "Parasite"
if watched_movie in watchlist:
    watchlist.remove(watched_movie)
    print(f"Marked '{watched_movie}' as watched and removed from list.")

# Show top 5 movies to watch using slicing
print("\nTop 5 movies to watch:")
top5 = watchlist[:5]
for movie in top5:
    print("-", movie)

# Final watchlist with index
print("\nUpdated Watchlist:")
for index, movie in enumerate(watchlist, start=1):
    print(f"{index}. {movie}")
