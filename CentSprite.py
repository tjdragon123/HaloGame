from sprite import Sprite

class CentSprite(Sprite):
    def __init__(self, filename, _cx, _cy):
        super().__init__(filename, 0, 0)
        self.cx = _cx
        self.cy = _cy
        self.recenter()
    
    def recenter(self):
        sizeTuple = self.image.get_size()
        self.x = self.cx-(sizeTuple[0]/2)
        self.y = self.cy-(sizeTuple[1]/2)