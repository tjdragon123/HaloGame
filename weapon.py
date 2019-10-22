from sprite import Sprite
from CentSprite import CentSprite
import pygame
import math

class Weapon():
    def __init__(self,_range,_damage,_csize,_speed,_reserves,_sprite, firingSprite, spriteSize, _amtype, firingSoundFileName):
        self.range = _range
        self.damage = _damage
        self.clipsize = _csize
        self.amtype = _amtype
        self.bullspeed = _speed
        self.reserves = _reserves
        self.sprite = _sprite
        self.firingSprite = firingSprite
        self.firingSprite.change_size(spriteSize, spriteSize)
        self.sprite.change_size(spriteSize, spriteSize)
        pygame.mixer.init()
        self.firingSound = pygame.mixer.Sound("magnumFireSound.wav")
        self.firing = False
        
    def shoot(self, enemies, direction, x, y, currTicks):
        self.firingSound.play()
        self.firing = True
        if self.amtype == "hitscan":
            for enemy in enemies:
                sizeTuple = enemy.sprite.image.get_size()
                """
                minDeg = 90+math.degrees(math.atan2(enemy.sprite.y - y, enemy.sprite.x - x))
                maxDeg = 90+math.degrees(math.atan2(enemy.sprite.y + sizeTuple[1] - y, enemy.sprite.x + sizeTuple[0]-x))
                if direction > minDeg and direction < maxDeg:
                    enemy.damaged(self.damage, currTicks)
                """
                if enemy.sprite.x > x:
                    if enemy.sprite.y < y:
                        minDeg = 90+math.degrees(math.atan2(enemy.sprite.y - y, enemy.sprite.x - x))
                        maxDeg = 90+math.degrees(math.atan2(enemy.sprite.y + sizeTuple[1] - y, enemy.sprite.x + sizeTuple[0]-x))
                        if direction > minDeg and direction < maxDeg:
                            enemy.damaged(self.damage, currTicks)
                    else:
                        minDeg = 90+math.degrees(math.atan2(enemy.sprite.y - y, enemy.sprite.x + sizeTuple[0] - x))
                        maxDeg = 90+math.degrees(math.atan2(enemy.sprite.y + sizeTuple[1] - y, enemy.sprite.x - x))
                        if direction > minDeg and direction < maxDeg:
                            enemy.damaged(self.damage, currTicks)
                else:
                    if enemy.sprite.y < y:
                        minDeg = 90+math.degrees(math.atan2(enemy.sprite.y + sizeTuple[1] - y, enemy.sprite.x - x))
                        maxDeg = 90+math.degrees(math.atan2(enemy.sprite.y - y, enemy.sprite.x + sizeTuple[0] - x))
                        if direction > minDeg and direction < maxDeg:
                            enemy.damaged(self.damage, currTicks)
                    else:
                        minDeg = 90+math.degrees(math.atan2(enemy.sprite.y + sizeTuple[1] - y, enemy.sprite.x + sizeTuple[0] - x))
                        maxDeg = 90+math.degrees(math.atan2(enemy.sprite.y - y, enemy.sprite.x - x))
                        if direction > minDeg and direction < maxDeg:
                            enemy.damaged(self.damage, currTicks)
            
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
    
    def draw(self, screen, x, y, direction):
        if(self.firing):
            self.firingSprite.setDirection(direction)
            self.firingSprite.cx = x
            self.firingSprite.cy = y
            self.firingSprite.recenter()
            self.firingSprite.draw(screen)   
        else:
            self.sprite.setDirection(direction)
            self.sprite.cx = x
            self.sprite.cy = y
            self.sprite.recenter()
            self.sprite.draw(screen)
        

class projectileBlast():
    def __init__(self, _sprite,_explosive):
        self.sprite = _sprite
        self.explosive = _explosive
        self.radius = _radius
        self.visible = _visible

#rpground = projectileBlast()
#rpg = Explosive(100,100,1,15,20,20,"rpg.png",rpground)

#rpg.rpground.detonate()

#inventory = []
#inventory.append(rpg)

#print(inventory[0])
#print(inventory[0].damage)
#rpg.shoot()