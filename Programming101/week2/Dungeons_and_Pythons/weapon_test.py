from weapon import Weapon
import unittest


class TestWeapon(unittest.TestCase):

    def setUp(self):
        self.axe = Weapon("Mighty Axe", 25, 0.2)

    def test_weapon_init(self):
        self.assertEqual(self.axe.type, "Mighty Axe")
        self.assertEqual(self.axe.damage, 25)
        self.assertEqual(self.axe.critical_strike_percent, 0.2)

    def test_critical_strike_percent_error(self):
        with self.assertRaises(ValueError):
            Weapon("Dingo", 25, 3.5)

    def test_critical_hit(self):
        flags = set()
        for i in range(1000):
            flags.add(self.axe.critical_hit())
        self.assertEqual(2, len(flags))

if __name__ == '__main__':
    unittest.main()
