from datetime import timedelta


class Song:
    MIN_RATING = 1
    MAX_RATING = 5

    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length
        self.bitrate = bitrate
        self.rating = 0
        self.rate(rating)

    def rate(self, rating):
        if rating in range(self.MIN_RATING, self.MAX_RATING + 1):
            self.rating = rating
        else:
            message = "Rating must be in the range [{},{}]"
            raise ValueError(message.format(self.MIN_RATING, self.MAX_RATING))

    def __str__(self):
        time = timedelta(seconds=self.length)
        return "{} {} - {}".format(self.artist, self.title, time)
