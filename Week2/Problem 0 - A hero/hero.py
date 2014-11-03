class Hero:

    def __init__(self, hero_name, hero_health, nickname):
        self.name = hero_name
        self.health = hero_health
        self.nickname = nickname
        self.MAX_HEALTH = hero_health

    def know_as(self):
        return "{} the {}".format(self.name, self.nickname)

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


