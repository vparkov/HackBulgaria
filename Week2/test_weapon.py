import random
import weapon
import unittest
#from hero import weapon


class TestWeapon(unittest.TestCase):

    def setUp(self):
        self.sword_of_justice = weapon.Weapon("sword", 58, 0.5)

    def test_orc_init(self):
        self.assertEqual(self.sword_of_justice.name, "sword")
        self.assertEqual(self.green_orc.health, 250)
        self.assertEqual(self.green_orc.berserk_factor, 2)

    def test_weapon_crit(self):
        results = []
        for x in range(1000):
            results.append(self.sword_of_justice.critical_hit())

        self.assertTrue(True in results)
        self.assertTrue(False in results)

if __name__ == '__main__':
    unittest.main()
