from song import Song


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
