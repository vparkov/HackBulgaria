import unittest
from weapon import Weapon
from entity import Entity


class EntityTest (unittest.TestCase):
    def setUp(self):
        self.entity = Entity("Samy", 100)
        self._MAX_HEALTH = 100

    def test_hero_init(self):

        self.assertEqual(self.entity.name, "Samy")
        self.assertEqual(self.entity.health, 100)

    def test_get_health(self):

        self.assertEqual(self.entity.get_health(), 100)

    def test_is_alive_return_false(self):

        self.entity.health = 0
        self.assertFalse(self.entity.is_alive())

    def test_is_alive(self):
        self.assertTrue(self.entity.is_alive())

    def test_take_damage(self):

        self.assertEqual(80, self.entity.take_damage(20))

    def test_take_damage_more_than_health(self):
        self.assertEqual(0, self.entity.take_damage(120))

    def test_take_healing_to_dead_person(self):
        self.entity.health = 0
        self.assertFalse(self.entity.take_healing(20))

    def test_take_healing_more_than_full_health(self):
        self.entity.health = 90
        self.entity.take_healing(40)
        self.assertTrue(self.entity.take_healing(self._MAX_HEALTH))

    def test_take_healing_true(self):
        self.entity.health = 40

    def test_it_entity_has_no_weapon(self):
        self.assertFalse(self.entity.has_weapon())

    def test_if_entity_has_weapon(self):
        weapon = Weapon("Mighty Axe", 25, 0.2)
        self.entity.equip_weapon(weapon)
        self.assertTrue(self.entity.has_weapon())

    def test_equip_weapon(self):
        weapon = Weapon("Mighty Axe", 25, 0.2)
        self.assertEqual(self.entity.equip_weapon(weapon),
                         {'Weaponn': {'type': 'Mighty Axe', 'damage': 25, 'csp': 0.2}})

    def test_equip_with_another_weapon(self):
        weapon = Weapon("Mighty Axe", 25, 0.2)
        self.entity.equip_weapon(weapon)
        weapon = Weapon("Magic Sword", 20, 0.3)
        self.assertEqual(self.entity.equip_weapon(weapon),
                         {'weapon': {'type': 'Magic Sword', 'damage': 20, 'csp': 0.3}})

    def test_attack_with_no_weapon(self):
        self.assertEqual(self.entity.attack(), 0)

    def test_attack_with_weapon(self):
        weapon = Weapon("Mighty Axe", 25, 0.2)
        self.entity.equip_weapon(weapon)
        self.assertEqual(self.entity.attack(), 25)

if __name__ == '__main__':
    unittest.main()
