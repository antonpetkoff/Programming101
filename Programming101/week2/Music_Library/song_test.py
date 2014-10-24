import unittest
from song import Song


class SongTests(unittest.TestCase):

    def setUp(self):
        self.song = Song("The Jack", "ACDC", "T.N.T.", 4, 240, 320)

    def test_init(self):
        song = Song("The Jack", "ACDC", "T.N.T.", 4, 240, 320)
        self.assertEqual(song.title, "The Jack")
        self.assertEqual(song.artist, "ACDC")
        self.assertEqual(song.album, "T.N.T.")
        self.assertEqual(song.rating, 4)
        self.assertEqual(song.length, 240)
        self.assertEqual(song.bitrate, 320)

    def test_rate_value_error(self):
        with self.assertRaises(ValueError):
            self.song.rate(6)

    def test_rate_success(self):
        self.song.rate(3)
        self.assertEqual(self.song.rating, 3)

    def test_str(self):
        expected = "ACDC The Jack - 0:04:00"
        self.assertEqual(str(self.song), expected)

if __name__ == '__main__':
    unittest.main()
