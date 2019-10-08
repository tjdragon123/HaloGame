class Button:
    """
    __init__() takes the name of the button file (use an image),
    x and y positions based on top left corner, and scale of the
    button based on percent of image size (defaults to 100%).
    Make sure your button image is cropped to exactly the size
    you want your button to be (aside from the scaling)."""
    def __init__(self, filename, _x, _y, x_scale=100, y_scale=100):
        self.image = Sprite(filename, _x, _y)
        self.image.change_size(x_scale, y_scale)
    
    #returns a boolean of whether the x and y coordinates are within the button or not
    def checkInside(self, x, y):
        return((x > self.x) and (x < (self.x + self.image.get_size())) and
           (y > self.y) and (y < (self.y + self.image.get_size())))
    
    def draw(self, screen):
        self.image.draw(screen)