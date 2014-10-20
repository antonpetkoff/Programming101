from random import random


class Fight():

    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def simulate_fight(self):
        coin_flip = random()
        round = 0 if coin_flip < 0.5 else 1
        while(self.hero.is_alive() and self.orc.is_alive()):
            if round % 2 == 0:  # hero attacks
                if self.hero.weapon.critical_hit():
                    damage = self.hero.attack() * 2
                else:
                    damage = self.hero.attack()
                expr = "Hero @ {} health attacks Orc @ {} health with {} damage"
                print(expr.format(self.hero.health, self.orc.health, damage))
                self.orc.take_damage(damage)
            else:               # orc attacks
                if self.orc.weapon.critical_hit():
                    damage = self.orc.attack() * 2
                else:
                    damage = self.orc.attack()
                expr = "Orc @ {} health attacks Hero @ {} health with {} damage"
                print(expr.format(self.orc.health, self.hero.health, damage))
                self.hero.take_damage(damage)
            round += 1
