
class Weapon():
    def __init__(self,_range,_damage,_csize,_speed,_reserves,_sprite,_amtype):
        self.range = _range
        self.damage = _damage
        self.clipsize = _csize
        self.amtype = _amtype
        self.bullspeed = _speed
        self.reserves = _reserves
        self.sprite = _sprite
    def shoot(self):
        if self.amtype == "hitscan":
            print("pew")
        elif self.amtype == "projectile":
            print ("bang")
        else:
            print("error")
    
    def melee(self):
        if self.amtype == "melee":
            print("whack")
        else:
            print(error)

class projectileBlast():
    def __init__(_sprite,_explosive):
        self.sprite = _sprite
        self.explosive = _explosive
        self.radius = _radius
        self.visible = _visible

rpground = projectileBlast()
rpg = Explosive(100,100,1,15,20,20,"rpg.png",rpground)

rpg.rpground.detonate()

inventory = []
inventory.append(rpg)

print(inventory[0])
print(inventory[0].damage)
rpg.shoot()