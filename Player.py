from weapon import Weapon
from sprite import Sprite
from CentSprite import CentSprite

class Player():
    def __init__(self):
        self.health = 100
        self.shields = 200
        self.weapons = [Weapon(100,50,12,-1,-1,CentSprite("Sprites/PlayerPistol.png", 0, 0), 50, "hitscan", "magnumFireSound.wav")]
        self.current = self.weapons[0]
        self.lastDamaged = 0
        self.rechargeRate = 0.1 #shield recharge rate in hp per tick
        self.rechargeCD = 5000 #cooldown time after taking damage before shields begin to recharge (measured in ticks)
        self.shieldsLastUpdated = 0
    
    def damaged(self, amtDamaged, currTicks):
        if self.shields > amtDamaged:
            self.shields -= amtDamaged
        elif self.shields > 0:
            self.health -= (amtDamaged - self.shields)
            self.shields = 0
        else:
            self.health -= amtDamaged
        
        self.lastDamaged = currTicks
        
    def draw(self, screen, x, y, direction):
        self.current.draw(screen, x, y, direction)
    
    def shoot(self, enemies, direction, x, y, currTicks):
        self.current.shoot(enemies, direction, x, y, currTicks)
        
        
    def updateShields(self, currTicks):
        if (currTicks - self.lastDamaged) > self.rechargeCD:
            self.shields += (currTicks-self.shieldsLastUpdated)*rechargeRate
            if self.shields > 200:
                self.shields = 200
                
        self.shieldsLastUpdated = currTicks
    
    def heal(self, amtToHeal):
        self.health += amtToHeal
        if self.health > 100:
            self.health = 100