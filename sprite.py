'''
Mr. Lindsay's Sprite Class
VERSION 1.0 -- 10/29/18 7pm
  * TO SET UP AND CREATE A SPRITE
    * Copy this file (sprite.py) to your working directory
    * IMPORT LINE: from sprite import Sprite
    * CREATE A SPRITE: s = Sprite(filename, x, y)
  * METHODS:
    * DRAW:   s.draw(screen) -- draws at current x,y
    * DETECT COLLISION: s.is_touching(other_sprite) -- returns boolean
    * HIDE:   s.hide() -- hides the sprite
    * SHOW:   s.show() -- shows the sprite
    * RESIZING: s.change_size(x_percent, y_percent)
  * ATTRIBUTES:
      x, y...........the x and y coordinates
      image..........The image we have loaded
      is_visible.....True if it is visible
  * METHODS TO DO: (methods we want, but not implemented yet)
      move_towards(otherSprite, velocity)
      rotate(degreesClockwise)
      move(speed) # in the current direction
      setDirection(degrees) #where 0-degrees is straight up
      setup_animation(images)
      goto_next_image()
'''
import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, filename, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.image = pygame.image.load(filename)
        self.original = self.image
        print("This is a Sprite loading from file", filename)
        self.is_visible = True
        
    def draw(self, screen):
        if self.is_visible:
            screen.blit(self.image, (self.x, self.y))
        
    def is_touching(self, other_sprite):
        if self.is_visible and other_sprite.is_visible:
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
            other_sprite.rect = other_sprite.image.get_rect()
            other_sprite.rect.x = other_sprite.x
            other_sprite.rect.y = other_sprite.y
            return pygame.sprite.collide_rect(self, other_sprite)
        else: return False
        
    def hide(self):
        self.is_visible = False
    
    def show(self):
        self.is_visible = True
    
    # Thanks James Johnson, class of 2020
    def change_size(self, x_percent, y_percent):
        w = self.image.get_width()
        h = self.image.get_height()
        new_w = int(w * x_percent / 100)
        new_h = int(h * y_percent / 100)
        self.image = pygame.transform.scale(self.image,(new_w,new_h))
        
        ow = self.original.get_width()
        oh = self.original.get_height()
        self.original = pygame.transform.scale(self.original,(new_w,new_h))
    
    
    def setDirection(self, degreesClockwise):
        self.image = pygame.transform.rotate(self.original,-degreesClockwise)
    