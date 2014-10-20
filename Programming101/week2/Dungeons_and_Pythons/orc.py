from entity import Entity
from weapon import Weapon


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.berserk_factor = None
        if berserk_factor > 2:
            self.berserk_factor = 2
        elif berserk_factor < 1:
            self.berserk_factor = 1
        else:
            self.berserk_factor = berserk_factor

    def attack(self):
        if isinstance(self.weapon, Weapon):
            return self.weapon.damage * self.berserk_factor
        else:
            return 0
