from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from fnmatch import fnmatch
from song import Song
from playlist import Playlist
import os


class MusicCrawler:

    def __init__(self, directory):
        self.directory = directory
        self.mp3_files = []

    def generate_playlist(self):
        playlist = Playlist("Playlist")
        for file_name in os.listdir(self.directory):
            if fnmatch(file_name, "*.mp3"):
                self.mp3_files.append(self.directory + file_name)
                id3 = ID3(self.directory + file_name)
                mp3 = MP3(self.directory + file_name)
                song = Song(id3['TIT2'],
                            id3['TPE1'],
                            id3['TALB'],
                            5,
                            mp3.info.length,
                            mp3.info.bitrate)
                playlist.add_song(song)
        return playlist


def main():
    a = MusicCrawler("/home/tony/Music/")
    playlist = a.generate_playlist()
    print(str(playlist))


if __name__ == '__main__':
    main()
