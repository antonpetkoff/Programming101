from song import Song
from collections import namedtuple
import json


class Playlist:
    MIN_BITRATE = 128

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if isinstance(song, Song):
            self.songs.append(song)
        else:
            raise TypeError("song must be of type \"Song\"!")

    def remove_song(self, song_name):
        self.songs = [s for s in self.songs if s.title != song_name]

    def total_length(self):
        length = 0
        for song in self.songs:
            length += song.length
        return length

    def remove_disrated(self, rating):
        if rating in range(Song.MIN_RATING, Song.MAX_RATING + 1):
            self.songs = [s for s in self.songs if s.rating >= rating]
        else:
            message = "Rating must be in the range [{},{}]"
            raise ValueError(message.format(Song.MIN_RATING, Song.MAX_RATING))

    def remove_bad_quality(self):
        self.songs = [s for s in self.songs if s.bitrate >= self.MIN_BITRATE]

    def show_artists(self):
        artists = set()
        for song in self.songs:
            artists.add(song.artist)
        return list(artists)

    def __str__(self):
        result = ""
        for i in range(len(self.songs)):
            result += str(self.songs[i])
            if i != len(self.songs) - 1:
                result += "\n"
        return result

    def to_JSON(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def save(self, file_name):
        with open(file_name, "w") as writeFile:
            writeFile.write(self.to_JSON())

    @staticmethod
    def load(file_name):
        with open(file_name, "r") as readFile:
            source = json.loads(readFile.read())
            playlist = Playlist(source["name"])
            for song in source["songs"]:
                playlist.add_song(Song(**song))
            return playlist


def main():
    song = Song("The Jack", "ACDC", "T.N.T.", 4, 256, 320)
    song_2 = Song("The Mack", "ACDC", "B.N.B.", 2, 256, 96)
    playlist = Playlist("Test Playlist")
    playlist.add_song(song)
    playlist.add_song(song_2)

    playlist.save("output.json")
    new_playlist = Playlist.load("output.json")
    print(str(new_playlist))
    print(str(playlist))

if __name__ == '__main__':
    main()
