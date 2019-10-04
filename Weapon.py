import pygame
import time
from sprite import Sprite

class Weapon:
    def __init__(self, _damage, _magSize, _reserves, _image, _firingImage, _hitImage):
        self.damage = _damage
        self.magSize = _magSize
        self.reserves = _reserves
        self.image = _image
        self.firingImage = _firingImage
        self.hitImage = _hitImage


class ProjWeapon(Weapon):
    def __init__(self, _damage, _magSize, _reserves, _image, _firingImage, _hitImage, projVel, projImage):
        super().__init__(self, _damage, _magSize, _reserves, _image, _firingImage, _hitImage)
        self.projVel = _projVel
        self.projImage = _projImage


class BeamWeapon(Weapon):
    def checkHit():
        if 