import random


class Weapon:

    def __init__(self, name, damage, critical_strike_percentage):
        self.name = name
        self.damage = damage
        self.critical_strike_percentage = critical_strike_percentage

    def critical_hit(self):
        if random.random() > self.critical_strike_percentage:
            return False
        return True

