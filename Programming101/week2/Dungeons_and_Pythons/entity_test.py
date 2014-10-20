from entity import Entity
from weapon import Weapon
import unittest


class TestEntity(unittest.TestCase):
    def setUp(self):
        self.entity = Entity("Entity", 100)

    def test_entity_init(self):
        self.assertEqual(self.entity.name, "Entity")
        self.assertEqual(self.entity.health, 100)

    def test_get_health(self):
        self.assertEqual(self.entity.get_health(), 100)

    def test_is_alive(self):
        self.assertTrue(self.entity.is_alive())

    def test_is_not_alive(self):
        self.entity.health = 0
        self.assertFalse(self.entity.is_alive())

    def test_take_damage(self):
        self.entity.take_damage(60)
        self.assertEqual(40, self.entity.get_health())
        self.entity.take_damage(14.5)
        self.assertEqual(25.5, self.entity.get_health())

    def test_take_too_much_damage(self):
        self.entity.take_damage(250.3)
        self.assertEqual(0, self.entity.get_health())

    def test_take_healing_alive(self):
        self.entity.take_damage(40)        # entity should be at 60
        self.assertEqual(60, self.entity.get_health())
        self.assertTrue(self.entity.take_healing(15))
        self.assertEqual(75, self.entity.get_health())

    def test_take_healing_overheal(self):
        self.assertTrue(self.entity.take_healing(24))
        self.assertEqual(100, self.entity.get_health())

    def test_take_healing_max_health(self):
        self.entity.health = 50
        self.assertTrue(self.entity.take_healing(70))
        self.assertEqual(100, self.entity.health)

    def test_take_healing_dead(self):
        self.entity.take_damage(100)        # entity is dead now
        self.assertFalse(self.entity.is_alive())
        self.assertFalse(self.entity.take_healing(90))
        self.assertEqual(0, self.entity.get_health())

    def test_has_weapon(self):
        self.entity.weapon = Weapon("Axe", 20, 0.5)
        self.assertTrue(self.entity.has_weapon())

    def test_doesnt_have_weapon(self):
        self.assertFalse(self.entity.has_weapon())

    def test_equip_weapon(self):
        old_weapon = Weapon("Axe", 20, 0.5)
        self.entity.equip_weapon(old_weapon)
        self.assertTrue(self.entity.has_weapon())
        self.assertEqual(old_weapon, self.entity.weapon)

    def test_equip_new_weapon(self):
        old_weapon = Weapon("Axe", 20, 0.5)
        self.entity.equip_weapon(old_weapon)
        new_weapon = Weapon("Sopa", 30, 0.8)
        self.entity.equip_weapon(new_weapon)
        self.assertEqual(new_weapon, self.entity.weapon)

    def test_equip_invalid_weapon(self):
        with self.assertRaises(TypeError):
            self.entity.equip_weapon(set())

    def test_attack_with_weapon(self):
        weapon = Weapon("Axe", 20, 0.5)
        self.entity.equip_weapon(weapon)
        self.assertEqual(20, self.entity.attack())

    def test_attack_without_weapon(self):
        self.assertEqual(0, self.entity.attack())

if __name__ == '__main__':
    unittest.main()
