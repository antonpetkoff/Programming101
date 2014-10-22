from random import random


class Fight():

    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def handle_hit(self, attacker, opponent):
        if attacker.weapon.critical_hit():
            damage = attacker.attack() * 2
        else:
            damage = attacker.attack()
        expr = "{} ({} Health) attacks {} ({} Health) with {} damage"
        print(expr.format(attacker.name, attacker.health,
                          opponent.name, opponent.health, damage))
        opponent.take_damage(damage)

    def simulate_fight(self):
        coin_flip = random()
        round = 0 if coin_flip < 0.5 else 1
        while(self.hero.is_alive() and self.orc.is_alive()):
            if round % 2 == 0:  # hero attacks
                self.handle_hit(self.hero, self.orc)
            else:               # orc attacks
                self.handle_hit(self.orc, self.hero)
            round += 1
