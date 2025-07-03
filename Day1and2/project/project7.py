## 7. Movie Organizer
print("========================================")
print("            Movie Organizer             ")
print("========================================")

# 1. Ask the user for three favorite movies
movie1 = input("Enter your first favorite movie: ")
movie2 = input("Enter your second favorite movie: ")
movie3 = input("Enter your third favorite movie: ")

# 2. Store them in a tuple
movies = (movie1, movie2, movie3)

# 3. Print the entire tuple and each movie separately
print("\n Your Favorite Movies:")
print("All Movies (Tuple):", movies)
print(f"1. {movies[0]}")
print(f"2. {movies[1]}")
print(f"3. {movies[2]}")

# 4. Display the type using type()
print(f"\nType of 'movies' variable: {type(movies)}")
