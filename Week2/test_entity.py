from orc import Orc
from hero import Hero
import entity
import unittest


class EntityTest(unittest.TestCase):

    def setUp(self):
        self.orc_and_human = entity.Entity("Kondio", 100, "Azis", 250)

    def test_orc_init(self):
        self.assertEqual(self.orc_and_human.hero_name, "Kondio")
        self.assertEqual(self.orc_and_human.hero_health, 100)
        self.assertEqual(self.orc_and_human.orc_name, "Azis")
        self.assertEqual(self.orc_and_human.orc_health, 250)
