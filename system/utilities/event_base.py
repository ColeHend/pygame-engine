from spritesheet import SpriteSheet
class Event_Base():
    def __init__(self,name,imageName,x,y,pages,settings):
        self.name = name;
        self.image = SpriteSheet(imageName)
        self.x = x;
        self.y = y;
        self.pages = pages;
        self.settings = settings;