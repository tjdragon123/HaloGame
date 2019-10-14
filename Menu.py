from sprite import Sprite
from CentSprite import CentSprite


class Menu:
    def __init__(self, backgroundFileName, _buttons): #takes a background image filename and a list of buttons
        self.background = CentSprite(backgroundFileName, 0, 0)
        self.buttons = _buttons
    
    def draw(self, screen):
        xratio = screen.get_size()[0]/self.background.image.get_size()[0]
        yratio = screen.get_size()[1]/self.background.image.get_size()[1]
        ratio = xratio
        if(yratio > xratio):
            ratio = yratio
        
        self.background.change_size(100*ratio, 100*ratio)
        self.background.cx = screen.get_size()[0]/2
        self.background.cy = screen.get_size()[1]/2
        self.background.recenter()
        self.background.draw(screen)
        for button in self.buttons:
            button.draw(screen)
    
    def checkWhichInside(self, x, y):
        for i in range(len(self.buttons)):
            if self.buttons[i].checkInside(x,y):
                return i
        return -1