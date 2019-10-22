from weapon import Weapon
from sprite import Sprite
from CentSprite import CentSprite
class Enemy():
    def __init__(self,_name,_health, imageFilename, size, cx, cy, _vel):
        self.name = _name
        self.health = _health
        self.sprite = CentSprite(imageFilename, cx, cy)
        self.sprite.change_size(size, size)
        self.sprite.recenter()
        self.vel = _vel
        self.weapon = None
    def follow(self,playerx,playery):
        if self.sprite.cx < playerx:
            self.sprite.x += self.vel
        elif self.sprite.cx > playerx:
            self.sprite.x -= self.vel
        if self.sprite.cy < playery:
            self.sprite.y += self.vel
        elif self.sprite.cy > playery:
            self.y -= self.vel
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
        print("ow")
    
    def holder(self):
        pass
    def helder(self):
        pass