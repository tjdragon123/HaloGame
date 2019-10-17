from Weapon import Weapon
from Sprite import Sprite
from CentSprite import CentSprite

class Player():
    def __init__(self):
        self.health = 100
        self.shields = 200
        self.weapons = [Weapon(100,50,12,-1,-1,CentSprite("Sprites/PlayerPistol.png"),"hitscan")]
        self.current = weapons[0]
        self.lastDamaged = 0
        