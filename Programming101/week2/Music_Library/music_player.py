#from playlist import Playlist
from music_crawler import MusicCrawler
import pygame


class MusicPlayer():

    def __init__(self, directory):
        self.mc = MusicCrawler(directory)
        self.playlist = self.mc.generate_playlist()

    def playSound(self):
        pass

    @staticmethod
    def loop():
        musicPlayer = MusicPlayer("/home/tony/Music/")

        while True:
            command = input("> ")

            #firstPlay = True
            pygame.init()
            pygame.mixer.music.load(musicPlayer.mc.mp3_files[0])
            pos = 0.0

            if command == "play":
                pygame.mixer.music.set_pos(pos)
                pygame.mixer.music.play()
            elif command == "pause":
                pos = pygame.mixer.music.get_pos()
                pygame.mixer.music.pause()
            elif command == "quit":
                print("bye!")
                break
            else:
                print("Invalid command!")


def main():
    MusicPlayer.loop()


if __name__ == '__main__':
    main()
