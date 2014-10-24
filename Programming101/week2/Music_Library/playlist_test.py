import unittest
from playlist import Playlist
from song import Song
from uuid import uuid4
from os import remove


class PlaylistTests(unittest.TestCase):

    def setUp(self):
        self.playlist = Playlist("Test Playlist")
        self.song = Song("The Jack", "ACDC", "T.N.T.", 4, 256, 320)
        self.song_2 = Song("The Mack", "ACDC", "B.N.B.", 2, 256, 96)

    def test_init(self):
        test_playlist = Playlist("ASDF")
        self.assertEqual(test_playlist.name, "ASDF")

    def test_add_song_success(self):
        self.playlist.add_song(self.song)
        self.assertEqual(self.playlist.songs[0], self.song)

    def test_add_song_type_error(self):
        with self.assertRaises(TypeError):
            self.playlist.add_song("not a song")

    def test_remove_song(self):
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.song_2)
        self.playlist.remove_song(self.song.title)
        self.assertEqual(self.playlist.songs, [self.song_2])

    def test_total_length(self):
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.song_2)
        self.assertEqual(self.playlist.total_length(), 512)

    def test_remove_disrated_success(self):
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.song_2)
        self.playlist.remove_disrated(3)
        self.assertEqual(self.playlist.songs, [self.song])

    def test_remove_disrated_value_error(self):
        with self.assertRaises(ValueError):
            self.playlist.remove_disrated(8)

    def test_remove_bad_quality(self):
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.song_2)
        self.playlist.remove_bad_quality()
        self.assertEqual(self.playlist.songs, [self.song])

    def test_show_artists(self):
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.song_2)
        self.assertEqual(self.playlist.show_artists(), ["ACDC"])

    def test_load(self):
        self.playlist.add_song(self.song)
        self.playlist.add_song(self.song_2)

        file_name = str(uuid4())
        self.playlist.save(file_name)
        loaded_playlist = Playlist.load(file_name)
        remove(file_name)

        self.assertEqual(str(self.playlist), str(loaded_playlist))


if __name__ == '__main__':
    unittest.main()
