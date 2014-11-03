class Orc:

    def __init__(self, orc_name, orc_health, berserk_factor):
        #self.__setselfberserk_factor(berserk_factor)
        self.name = orc_name
        self.health = orc_health
        self.berserk_factor = berserk_factor
        self.MAX_HEALTH = orc_health

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0
        return self.health

    def take_healing(self, healing_points):
        if self.health == 0:  #i am dead YO
            return False

        elif self.health == self.MAX_HEALTH:  #i dont need you, scum
            return False

        else:
            self.health += healing_points
            return True

