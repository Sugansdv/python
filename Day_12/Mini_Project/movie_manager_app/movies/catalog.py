import pickle
import os
import csv
from datetime import datetime

MOVIE_FILE = "movies/data.pkl"

def add_movie(collection, title, genre, year):
    collection.append({
        "title": title,
        "genre": genre,
        "year": year,
        "added_on": datetime.now().strftime("%Y-%m-%d"),
        "rating": None
    })

def remove_movie(collection, title):
    return [movie for movie in collection if movie['title'].lower() != title.lower()]

def view_movies(collection):
    for idx, movie in enumerate(collection, 1):
        print(f"{idx}. {movie['title']} ({movie['year']}) - {movie['genre']} - Rating: {movie['rating']}")

def save_movies(collection):
    with open(MOVIE_FILE, 'wb') as f:
        pickle.dump(collection, f)

def load_movies():
    if os.path.exists(MOVIE_FILE):
        with open(MOVIE_FILE, 'rb') as f:
            return pickle.load(f)
    return []

def export_movies(collection, filename="movies/export.csv"):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Genre", "Year", "Added On", "Rating"])
        for movie in collection:
            writer.writerow([movie['title'], movie['genre'], movie['year'], movie['added_on'], movie['rating']])
