import random

from Player import Player


class Zombie:
    def __init__(self, name, health, reward, damage):
        self.name = name
        self.health = health
        self.reward = reward
        self.damage = damage

    def takeDamage(self, damage):
        #zombie need to get damage from player
        self.health -= damage
        if self.health <= 0:
            return self.reward
        else:
            return 0

    def zombie_health(self):
        #get the health of zombies
        return self.health

    def attackPlayer(self,Player):
        #get damage and hit player
        Player.health-= self.damage
        zombie_name = self.name
        print(f"You are attacked by {zombie_name} and lose {self.damage} health.")
        print(f"Now,your health is {Player.health}\n")




