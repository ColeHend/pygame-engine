from utilities.tile import Tile
from utilities.spritesheet import SpriteSheet
class Tileset():
    def __init__(self,image,settings):
        # settings: {rows:number, columns:number, metadata: list[list[tile:int, passable:boolean, typenum:int]]}
        self.image = image
        self.rows:int = settings['rows']
        self.columns:int = settings['columns']
        self.colorkey = settings['colorkey']
        self.metadata:list[list[int,int,int]] = settings["metadata"]
        self.tiles:list[Tile] = []
        self.load_tiles()
    
    def load_tiles(self):
        sheet = SpriteSheet(self.image)
        width, height = sheet.get_size()
        pxWidth, pxHeight = width/self.columns, height/self.rows
        for colNum in self.columns:
            for rowNum in self.rows:
                startX = colNum * pxWidth
                startY = rowNum * pxHeight
                currIndex = self.tiles.count()
                nonPassible = False
                typeNum = 0
                for tileInfo in self.metadata:
                    if currIndex == tileInfo[0]:
                        nonPassible = tileInfo[1]
                        typeNum = tileInfo[2]
                self.tiles.append(Tile(sheet.get_image(startX,startY,width,height),nonPassible,typeNum))