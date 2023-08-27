from tileset import Tileset
import json
class Map_Base():
    def __init__(self, tilesetName, mapNum: int):
        self.tileset = Tileset(tilesetName)
        with open('../data/maps/map{mapNum}.json') as map_json:
            self.map_settings = json.load(map_json)
        self.map_tile:list[list[list[int]]] = self.map_settings['tiles']
        self.events = []
        
    def load_events():
        pass