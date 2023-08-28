from spritesheet import SpriteSheet 
from state import State
directions = "up" or "down" or "left" or "right"
actions = "stop" or "walk"
class Event_Base():
    def __init__(self,name,imageName,x,y,pages,settings):
        self.name = name;
        if imageName != "none":
            self.image = SpriteSheet(imageName)
            self.currentState:State = State('down','stop')
            self.currImage = self.__getImage(0);
        self.x = x;
        self.y = y;
        self.pages = pages;
        self.settings = settings;
    
    def __getImage(self, anim_index:int, frameNumber:int = 4):
        theState:str = self.currentState.__str__();
        width, height = self.image.sprite_sheet.get_size()
        pxwidth, pxheight = width/frameNumber, height/frameNumber

        if self.currentState.direction == "up":
            return self.image.get_image((0+(pxwidth*anim_index)),(0+(pxheight*3)),pxwidth,pxheight)
        elif self.currentState.direction == "down":
            return self.image.get_image((0+(pxwidth*anim_index)),(0+(pxheight*0)),pxwidth,pxheight)
        elif self.currentState.direction == "left":
            return self.image.get_image((0+(pxwidth*anim_index)),(0+(pxheight*1)),pxwidth,pxheight)
        elif self.currentState.direction == "right":
            return self.image.get_image((0+(pxwidth*anim_index)),(0+(pxheight*2)),pxwidth,pxheight)
        
    def setState(self, direction:str, action:str):
        if direction == directions:
            self.currentState.direction = direction
        if action == actions:
            self.action = action
             
    def draw(self):
        pass

    def update(self):
        if self.currentState.action == 'stop':
            self.currImage = self.__getImage(0);