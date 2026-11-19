# Music Playlist Manager (complete activity, DSCM2L4). Python 3 standard library only.
# Run: python music_playlist_manager.py, then type a menu number and press Enter.
# Time: add O(1) amortised, remove O(n), view O(n), n = songs. Space: O(n) for the list.


class Playlist:
    def __init__(self, name, genre):
        # Step 1: Parameterised constructor
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"Playlist '{self.name}' ({self.genre}) is ready!")

    def add_song(self, song):
        # Step 2: Add a song
        if song == "":
            print("Song name cannot be empty.")
        else:
            self.songs.append(song)
            print(f"'{song}' added to {self.name}.")

    def remove_song(self, song):
        # Step 3: Remove safely
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}' removed.")
        else:
            print(f"'{song}' is not in the playlist.")

    def display(self):                                         # A: numbered list
        print(f"--- {self.name} ({self.genre}), songs: {len(self.songs)} ---")
        number = 1
        for song in self.songs:
            print(f"  {number}. {song}")
            number = number + 1

    # Step 4: Destructor
    def __del__(self):
        print(f"Playlist '{self.name}' deleted. Goodbye!")


my_playlist = Playlist("Road Trip Mix", "Pop")                 # B: birth, __init__ runs
while True:                                                    # C: the menu loop
    print("\n1. Add  2. Remove  3. View  4. Delete and quit")
    choice = input("Choice: ").strip()
    if choice == "1":
        my_playlist.add_song(input("Song name: ").strip())
    elif choice == "2":
        my_playlist.remove_song(input("Song to remove: ").strip())
    elif choice == "3":
        my_playlist.display()
    elif choice == "4":
        # Step 5: Death
        del my_playlist
        break
    else:
        print("Please type 1, 2, 3 or 4.")
print("Program finished.")                                     # D
