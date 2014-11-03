import orc
import unittest


class OrcTests(unittest.TestCase):

    def setUp(self):
        self.green_orc = orc.Orc("Rekrak", 250, 2)
        self.MAX_HEALTH = self.green_orc.health

    #def test_orc_berserc_factor(self):
    #    with self.assertRaises()

    def test_orc_init(self):
        self.assertEqual(self.green_orc.name, "Rekrak")
        self.assertEqual(self.green_orc.health, 250)
        self.assertEqual(self.green_orc.berserk_factor, 2)

    def test_get_health(self):
        self.assertEqual(self.green_orc.get_health(), 250)

    def test_is_alive(self):
        self.assertTrue(self.green_orc.is_alive())
        self.green_orc.health = 0
        self.assertFalse(self.green_orc.is_alive())

    def test_take_damage_int(self):
        self.green_orc.take_damage(10)
        self.assertEqual(self.green_orc.get_health(), 240)

    def test_take_damage_float(self):
        self.green_orc.take_damage(10.5)
        self.assertEqual(self.green_orc.get_health(), 239.5)

    def test_take_more_damage_thane_health(self):
        self.green_orc.take_damage(251)
        self.assertEqual(self.green_orc.get_health(), 0)

    def test_take_healing(self):
        self.green_orc.take_damage(40)
        heal_result = self.green_orc.take_healing(20)
        self.assertEqual(self.green_orc.health, 230)
        self.assertTrue(heal_result)

    def test_healing_dead_fucker(self):
        self.green_orc.take_damage(self.MAX_HEALTH)
        heal_result = self.green_orc.take_healing(20)
        self.assertEqual(self.green_orc.health, 0)
        self.assertFalse(heal_result)

    def test_healing_healthy_fucker(self):
        heal_result = self.green_orc.take_healing(20)
        self.assertEqual(self.green_orc.health, 250)
        self.assertFalse(heal_result)


if __name__ == '__main__':
    unittest.main()
