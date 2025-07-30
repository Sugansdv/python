import json
import os
import random
from core.decorators import repeat

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
        self.current_index = 0
        self.file_path = f"data/{self.name.lower().replace(' ', '_')}.json"
        self.load_playlist()

    def add_song(self, song_path):
        if not isinstance(song_path, str) or not song_path.strip():
            raise ValueError("Invalid song path")
        self.songs.append(song_path)
        self.save_playlist()
        print(f"Added: {song_path}")

    def shuffle(self):
        random.shuffle(self.songs)
        self.current_index = 0
        self.save_playlist()
        print("Playlist shuffled.")

    def save_playlist(self):
        os.makedirs("data", exist_ok=True)
        with open(self.file_path, "w") as f:
            json.dump({"songs": self.songs}, f)

    def load_playlist(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.songs = data.get("songs", [])
                print(f"Loaded playlist with {len(self.songs)} songs.")
        else:
            print("New playlist created.")

    def play(self):
        while self.current_index < len(self.songs):
            song = self.songs[self.current_index]
            self.current_index += 1
            yield f"Now playing: {song}"

    @repeat
    def play_looped(self):
        while True:
            song = self.songs[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.songs)
            yield f"Looping: {song}"
