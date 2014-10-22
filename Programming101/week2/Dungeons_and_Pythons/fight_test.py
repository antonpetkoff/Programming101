import unittest
from fight import Fight
from hero import Hero
from orc import Orc
from weapon import Weapon


class TestFight(unittest.TestCase):

    def setUp(self):
        self.orc = Orc("Berserk", 1000, 2)
        self.hero = Hero("Bron", 1000, "DragonSlayer")
        self.weapon = Weapon("Mighty Axe", 25, 0.3)
        self.orc.equip_weapon(self.weapon)
        self.hero.equip_weapon(self.weapon)
        self.fight = Fight(self.hero, self.orc)

    def test_simulate_fight(self):
        self.fight.simulate_fight()
        self.assertTrue(not self.orc.is_alive() or not self.hero.is_alive())


if __name__ == '__main__':
    unittest.main()
