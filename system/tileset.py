from utilities.tile import Tile
from utilities.spritesheet import SpriteSheet
import json
class Tileset():
    def __init__(self, name: str):
        # settings: {rows:number, columns:number, metadata: list[list[tile:int, impassable:boolean, typenum:int]]}
        self.name = name
        with open("../data/maps/tilesets/{name}.json") as json_file:
            settings = json.load(json_file)
            print(settings)
        self.image = SpriteSheet('../data/graphics/tilesets/{name}.png')
        self.rows:int = settings['rows']
        self.columns:int = settings['columns']
        self.metadata:list[list[int,bool,int]] = settings["metadata"]
        self.tiles:list[Tile] = []
        self.load_tiles()
    
    def load_tiles(self):
        width, height = self.image.sprite_sheet.get_size()
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
                self.tiles.append(Tile(self.image.get_image(startX,startY,pxWidth,pxHeight),nonPassible,typeNum))