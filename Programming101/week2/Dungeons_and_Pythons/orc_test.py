from orc import Orc
from weapon import Weapon
import unittest


class TestOrc(unittest.TestCase):

    def setUp(self):
        self.orc = Orc("Berserk", 100, 2)

    def test_orc_init(self):
        self.assertEqual("Berserk", self.orc.name)
        self.assertEqual(100, self.orc.health)
        self.assertEqual(2, self.orc.berserk_factor)

    def test_berserk_factor_over(self):
        tincho = Orc("Tincho", 200, 5)
        self.assertTrue(tincho.berserk_factor in [1, 2])

    def test_berserk_factor_under(self):
        pencho = Orc("Pencho", 210, 0.5)
        self.assertTrue(pencho.berserk_factor in [1, 2])

    def test_attack_berserk_with_weapon(self):
        weapon = Weapon("Mighty Axe", 25, 0.2)
        self.orc.equip_weapon(weapon)
        self.assertEqual(25 * 2, self.orc.attack())

    def test_attack_berserk_without_weapon(self):
        self.assertEqual(0, self.orc.attack())

if __name__ == '__main__':
    unittest.main()
