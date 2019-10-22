from weapon import Weapon
from sprite import Sprite
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
    
    def doBehavior(self, player, playerx, playery, currTime):
        if self.name == "Sword Elite":
            self.follow(playerx, playery)
            if self.sprite.is_touching(player.current.sprite):
                player.damaged(9001, currTime)
    
    def follow(self, playerx, playery):
        if self.sprite.x < playerx:
            self.sprite.x += self.vel
        elif self.sprite.x > playerx:
            self.sprite.x -= self.vel
        if self.sprite.y < playery:
            self.sprite.y += self.vel
        elif self.sprite.y > playery:
            self.sprite.y -= self.vel
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