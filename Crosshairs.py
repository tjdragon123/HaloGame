import pygame
from CentSprite import CentSprite

class Crosshairs:
    def __init__(self):
        self.crosshairs = CentSprite("haloCrosshairs.png", 0, 0)
        self.crosshairs.change_size(100,80)
        self.crosshairs.recenter()
    
    def run(self, screen):
        self.crosshairs.cx = pygame.mouse.get_pos()[0]
        self.crosshairs.cy = pygame.mouse.get_pos()[1]
        self.crosshairs.recenter()
        self.crosshairs.draw(screen)