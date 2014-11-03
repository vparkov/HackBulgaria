from orc import Orc
from hero import Hero


class Entity(Orc, Hero):

    def __init__(self, hero_name, hero_health, nickname, orc_name, orc_health, berserk_factor):
        super(). __init__(hero_name, hero_health, orc_name, orc_health)
