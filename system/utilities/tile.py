from pygame import Surface
from system.utilities.spritesheet import SpriteSheet
class Tile():
    def __init__(self,image, passible, typenum) -> None:
        self.image:Surface = image
        self.passible:bool = passible
        self.typenum:int = typenum