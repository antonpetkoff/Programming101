import unittest
from uuid import uuid4
from os import remove
from dungeon import Dungeon
from hero import Hero
from orc import Orc


class TestDungeon(unittest.TestCase):

    def setUp(self):
        self.existing_file = str(uuid4)
        self.test_map = \
            "S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S"
        with open(self.existing_file, "w") as writeFile:
            writeFile.write(self.test_map)
        self.dungeon = Dungeon(self.existing_file)

        self.hero = Hero("Hero", 100, "Nick")
        self.orc = Orc("Orc", 100, 2)

    def tearDown(self):
        remove(self.existing_file)

    def test_dungeon_init_existing_file(self):
        self.assertEqual(self.dungeon.map, self.test_map)
        self.assertEqual(10, self.dungeon._get_row_length())

    def test_dungeon_init_nonexisting_file(self):
        fileName = str(uuid4())
        with self.assertRaises(FileNotFoundError):
            Dungeon(fileName)

    def test_spawn_success(self):
        self.assertTrue(self.dungeon.spawn("the_hero", self.hero))
        self.test_map = self.test_map.replace("S", "H", 1)
        self.assertEqual(self.dungeon.map, self.test_map)
        self.assertEqual(self.dungeon.player_pos["the_hero"], 0)

        self.assertTrue(self.dungeon.spawn("the_orc", self.orc))
        self.test_map = self.test_map.replace("S", "O", 1)
        self.assertEqual(self.dungeon.map, self.test_map)
        self.assertEqual(self.dungeon.player_pos["the_orc"],
                         len(self.test_map) - 1)

    def test_spawn_fail(self):
        self.dungeon.spawn("the_hero", self.hero)
        self.dungeon.spawn("the_orc", self.orc)
        self.assertFalse(self.dungeon.spawn("new_hero", self.hero))

    def test_spawn_type_error(self):
        with self.assertRaises(TypeError):
            self.dungeon.spawn("Dingo")
"""
    def test_move_success(self):
        self.dungeon.spawn("the_hero", self.hero)
        self.dungeon.spawn("the_orc", self.orc)

        self.assertTrue(self.dungeon.move("the_hero", "right"))
        self.test_map = self.test_map.replace(".", "H", 1)
        self.test_map = self.test_map.replace("H", ".", 1)
        self.assertEqual(self.test_map, self.dungeon.map)

        self.assertTrue(self.dungeon.move("the_orc", "up"))
        temp_list = list(self.test_map)
        temp_list[len(temp_list) - 11] = "O"
        temp_list[len(temp_list) - 1] = "."
        self.test_map = "".join(temp_list)
        self.assertEqual(self.test_map, self.dungeon.map)

    def test_move_fail(self):
        self.dungeon.spawn("the_hero", self.hero)
        self.dungeon.spawn("the_orc", self.orc)

        self.assertFalse(self.dungeon.move("the_hero", "left"))
        self.assertFalse(self.dungeon.move("the_hero", "up"))
        self.assertFalse(self.dungeon.move("the_hero", "down"))

        self.assertFalse(self.dungeon.move("the_orc", "right"))
        self.assertFalse(self.dungeon.move("the_orc", "down"))

    def test_move_invalid_direction(self):
        self.dungeon.spawn("the_hero", self.hero)

        with self.assertRaises(ValueError):
            self.dungeon.move("the_hero", "dooooooown")

    def test_move_invalid_player(self):
        with self.assertRaises(ValueError):
            self.dungeon.move("invalid", "down")
"""
if __name__ == '__main__':
    unittest.main()
