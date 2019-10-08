

class Menu:
    def __init__(self, backgroundFileName, _buttons): #takes a background image filename and a list of buttons
        self.background = Sprite(backgroundFileName, 0, 0)
        self.buttons = _buttons
    
    def draw(self, screen):
        self.background.draw(screen)
        for button in self.buttons:
            button.draw(screen)
    
    