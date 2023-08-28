from system.utilities.event_base import Event_Base
from tileset import Tileset
import json
eventType = Event_Base
class Map_Base():
    def __init__(self, tilesetName, mapNum: int):
        self.tileset = Tileset(tilesetName)
        self.mapNum = mapNum
        with open(f'../data/maps/map{self.mapNum}.json') as map_json:
            self.map_settings = json.load(map_json)
        self.map_tile:list[list[list[int]]] = self.map_settings['tiles']
        self.events:eventType = []

    def __load_events():
        pass

    def draw_map(self,draw_layer: int):
        for yColum in self.map_tile:
            for tile_cell_arr in yColum:
                if len(tile_cell_arr) > draw_layer:
                    self.tileset.tiles[tile_cell_arr[draw_layer]].image.blit()
                            
    def draw(self):
        self.draw_map(0)
        self.draw_map(1)
        for event in self.events:
            event.draw()
        self.draw_map(2)
        self.draw_map(3)

    
    def update(self):
        for event in self.events:
            event.update()