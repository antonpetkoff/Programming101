
class Entity:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._MAX_HEALTH = self.health

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage_points):
        if self.health < damage_points:
            self.health = 0
        else:
            self.health -= damage_points

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        if self.health + healing_points < self._MAX_HEALTH:
            self.health += healing_points
        else:
            self.health = self._MAX_HEALTH
        return True
