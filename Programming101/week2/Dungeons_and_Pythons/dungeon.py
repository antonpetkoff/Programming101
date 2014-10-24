from entity import Entity
from hero import Hero
from orc import Orc


class Dungeon:

    def __init__(self, filename):
        self.map = self._read_map(filename)         # print format
        self._ROW_LEN = self._get_row_length()
        self.players = {}                           # (player_name, entity)
        self.player_pos = {}                        # (player_name, position)

    def _read_map(self, filename):
        result = ""
        try:
            with open(filename, "r") as readFile:
                result = readFile.read()
        except FileNotFoundError:
            raise
        return result

    def _get_row_length(self):
        return self.map.find("\n")

    def _swap_chars(self, pos_a, pos_b):
        temp = list(self.map)
        temp[pos_a], temp[pos_b] = temp[pos_b], temp[pos_a]
        self.map = "".join(temp)

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

        cur_pos = self.player_pos[player_name]

        if direction == "left":
            if cur_pos > 0 and self.map[cur_pos - 1] == ".":
                self._swap_chars(cur_pos, cur_pos - 1)
                self.player_pos[player_name] = cur_pos - 1
                return True
            else:
                return False
        elif direction == "right":
            if cur_pos < (len(self.map) - 2) and self.map[cur_pos + 1] == ".":
                self._swap_chars(cur_pos, cur_pos + 1)
                self.player_pos[player_name] = cur_pos + 1
                return True
            else:
                return False
        elif direction == "up":
            if cur_pos > self._ROW_LEN:
                pos_above = cur_pos - self._ROW_LEN - 1     # -1 for \n
                if self.map[pos_above] == ".":
                    self._swap_chars(cur_pos, pos_above)
                    self.player_pos[player_name] = pos_above
                    return True
                else:
                    return False
            else:
                return False
        elif direction == "down":
            if cur_pos < len(self.map) - self._ROW_LEN:
                pos_below = cur_pos + self._ROW_LEN + 1     # +1 for \n
                if self.map[pos_below] == ".":
                    self._swap_chars(cur_pos, pos_below)
                    self.player_pos[player_name] = pos_below
                    return True
                else:
                    return False
            else:
                return False
