import Weapon
class Enemy():
    def __init__(self,_name,_health,_sprite,_x,_y,_vel):
        self.name = _name
        self.health = _health
        self.sprite = _sprite
        self.x = _x
        self.y = _y
        self.location = (self.x,self.y)
        self.vel = _vel
        self.weapon = None
    def follow(self,playerx,playery):
        if self.x < playerx:
            self.x += self.vel
        elif self.x > playerx:
            self.x -= self.vel
        if self.y < playery:
            self.y += self.vel
        elif self.y > playery:
            self.y -= vel
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
    def holder:
        pass
    def helder:
        pass