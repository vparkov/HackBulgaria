import hero
import unittest


class HeroTests(unittest.TestCase):

    def setUp(self):
        self.bron_hero = hero.Hero("Bron", 100, 'DragonSlayer')
        self.MAX_HEALTH = self.bron_hero.health

    def test_hero_init(self):
        self.assertEqual(self.bron_hero.name, "Bron")
        self.assertEqual(self.bron_hero.health, 100)
        self.assertEqual(self.bron_hero.nickname, 'DragonSlayer')
        self.assertEqual(self.bron_hero.MAX_HEALTH, 100)

    def test_hero_known_as(self):
        self.assertEqual(self.bron_hero.know_as(), 'Bron the DragonSlayer')

    def test_get_health(self):
        self.assertEqual(self.bron_hero.get_health(), 100)

    def test_is_alive(self):
        self.assertTrue(self.bron_hero.is_alive())
        self.bron_hero.health = 0
        self.assertFalse(self.bron_hero.is_alive())

    def test_take_damage_int(self):
        self.bron_hero.take_damage(10)
        self.assertEqual(self.bron_hero.get_health(), 90)

    def test_take_damage_float(self):
        self.bron_hero.take_damage(10.5)
        self.assertEqual(self.bron_hero.get_health(), 89.5)

    def test_take_more_damage_thane_health(self):
        self.bron_hero.take_damage(101)
        self.assertEqual(self.bron_hero.get_health(), 0)

    def test_take_healing(self):
        self.bron_hero.take_damage(40)
        heal_result = self.bron_hero.take_healing(20)
        self.assertEqual(self.bron_hero.health, 80)
        self.assertTrue(heal_result)

    def test_healing_dead_fucker(self):
        self.bron_hero.take_damage(self.MAX_HEALTH)
        heal_result = self.bron_hero.take_healing(20)
        self.assertEqual(self.bron_hero.health, 0)
        self.assertFalse(heal_result)

    def test_healing_healthy_fucker(self):
        heal_result = self.bron_hero.take_healing(20)
        self.assertEqual(self.bron_hero.health, 100)
        self.assertFalse(heal_result)


if __name__ == '__main__':
    unittest.main()
