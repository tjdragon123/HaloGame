from sprite import Sprite

class Menu:
    def __init__(self, backgroundFileName, _buttons): #takes a background image filename and a list of buttons
        self.background = Sprite(backgroundFileName, 0, 0)
        self.buttons = _buttons
    
    def draw(self, screen):
        #self.background.change_size(100*scree.get_size()[0]/self.background.image.get_size()[0], 100*scree.get_size()[1]/self.background.image.get_size()[1]
        self.background.draw(screen)
        for button in self.buttons:
            button.draw(screen)
    
    def checkWhichInside(self, x, y):
        for i in range(len(self.buttons)):
            if self.buttons[i].checkInside(x,y):
                return i
        return -1