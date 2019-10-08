from sprite import Sprite

"""
This class allows you to define a sprite's location by its
centerpoint rather than its corner. cx and cy are the new
variables for x and y position based on center. After any
transformation that changes the shape, size, or orientation
of the CentSprite, you will need to use the recenter()
function to recenter the image on cx and cy.

"""

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