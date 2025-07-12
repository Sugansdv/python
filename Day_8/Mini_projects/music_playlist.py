# 16. Music Playlist Creator
# Description: Build a playlist using list operations.

# Start with an initial playlist
playlist = ["Shape of You", "Blinding Lights", "Perfect", "Levitating"]

# Display all songs
print("🎶 Current Playlist:")
for i, song in enumerate(playlist, start=1):
    print(f"{i}. {song}")

# Add songs
playlist.append("Senorita")
playlist.append("Dance Monkey")
print("\nAdded new songs: 'Senorita' and 'Dance Monkey'")

# Remove a song
song_to_remove = "Perfect"
if song_to_remove in playlist:
    playlist.remove(song_to_remove)
    print(f"Removed song: '{song_to_remove}'")

# Repeat songs using * repetition
repeated_playlist = playlist * 2
print("\n Repeated Playlist:")
for i, song in enumerate(repeated_playlist, start=1):
    print(f"{i}. {song}")

# Search for a song using `in`
search_song = "Levitating"
if search_song in playlist:
    print(f"\n '{search_song}' is in your playlist!")
else:
    print(f"\n '{search_song}' is not in your playlist.")
