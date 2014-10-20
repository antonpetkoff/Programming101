
class Hero:
    def __init__(self, name, health, nickname):
        self.name = name
        self.health = health
        self.nickname = nickname
        self.MAX_HEALTH = self.health

    def known_as(self):
        return "{} the {}".format(self.name, self.nickname)

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage_points):
        if self.health - damage_points < 0:
            self.health = 0
        else:
            self.health -= damage_points

    def take_healing(self, healing_points):
        if self.health + healing_points < self.MAX_HEALTH:
            self.health += healing_points
        return self.is_alive()
