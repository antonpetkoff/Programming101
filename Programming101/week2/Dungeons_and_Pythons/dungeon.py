from entity import Entity
from hero import Hero
from orc import Orc


class Dungeon:

    def __init__(self, filename):
        self.map = self._read_map(filename)
        self._ROW_LEN = self._get_row_length()
        self.map_list = self._make_list()
        self.players = {}
        self.player_pos = {}

    def _read_map(self, filename):
        result = ""
        try:
            with open(filename, "r") as readFile:
                result = readFile.read()
        except FileNotFoundError:
            raise
        return result

    def _get_row_length(self):
        i = 0
        while i < len(self.map):
            if self.map[i] == "\n":
                return i
            i += 1
        return 0

    def _make_list(self):
        return [elem for elem in list(self.map) if elem != "\n"]

    def print_map(self):
        print(self.map)

    def spawn(self, player_name, entity):
        new_letter = ""
        if isinstance(entity, Entity):
            if isinstance(entity, Hero):
                new_letter = "H"
            elif isinstance(entity, Orc):
                new_letter = "O"
        else:
            raise TypeError

        pos = self.map.find("S")
        if pos != -1:
            self.players[player_name] = entity
            self.player_pos[player_name] = pos
            self.map = self.map.replace("S", new_letter, 1)
            return True
        else:
            return False

    def move(self, player_name, direction):
        if player_name not in self.players.keys():
            raise ValueError
        if direction not in ["up", "down", "left", "right"]:
            raise ValueError
        player = "H" if isinstance(self.players[player_name], Hero) else "O"

        if direction == "up":
            pass
        elif direction == "down":
            pass
        elif direction == "left":
            pass
        elif direction == "right":
            pass
