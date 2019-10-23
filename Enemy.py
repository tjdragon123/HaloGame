from weapon import Weapon
from sprite import Sprite
import math
from CentSprite import CentSprite
class Enemy():
    def __init__(self,_name,_health, imageFilename, size, cx, cy, _vel, points):
        self.name = _name
        self.health = _health
        self.sprite = CentSprite(imageFilename, cx, cy)
        self.sprite.change_size(size, size)
        self.sprite.recenter()
        self.vel = _vel
        self.weapon = None
        self.points = points
    
    def doBehavior(self, player, playerx, playery, lastEnemyTime, currTime):
        if self.name == "Sword Elite":
            self.follow(playerx, playery, lastEnemyTime, currTime)
            if math.sqrt((self.sprite.cx-playerx)**2 + (self.sprite.cy-playery)**2) <= 60:
                player.damaged(9001, currTime)
    
    def follow(self, playerx, playery, lastEnemyTime, currTime):
        angle = 180 + math.degrees(math.atan2((playery - self.sprite.cy), (self.sprite.cx - playerx)))
        self.sprite.cx += (currTime - lastEnemyTime)*math.cos(math.radians(angle))*self.vel
        self.sprite.cy -= (currTime - lastEnemyTime)*math.sin(math.radians(angle))*self.vel
        self.sprite.recenter()
    def typeAssignment():
        if name == "":#jackal
            pass
        if name == "":#grunt plasma pistol
            pass
        if name == "":#grunt needler
            pass
        if name == "":#elite
            pass
        if name == "":#elite melee guy
            self.weapon = Weapon(5,100,0,"melee",100,0,"")
    
    def damaged(self, damage, currTicks):
        self.health -= damage
        print("ow")
    
    def holder(self):
        pass
    def helder(self):
        pass