from core.playlist import Playlist

if __name__ == "__main__":
    playlist = Playlist("My Mix")
    
    playlist.add_song("song1.mp3")
    playlist.add_song("song2.mp3")
    playlist.add_song("song3.mp3")

    playlist.shuffle()

    print("\n🎵 Playing songs (looped):")
    song_gen = playlist.play_looped()
    for _ in range(5):  # simulate 5 plays
        print(next(song_gen))
