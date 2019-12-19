from enum import Enum, IntEnum

from twenty_19.day8 import print_image
from twenty_19.util.geometry import Coord
from twenty_19.util.output import ImagePrinter


class Tile(IntEnum):
    UNVISITED = 0
    FLOOR = 1
    WALL = 2
    OXY_SENSOR = 3

class Map():
    def __init__(self, width=100, height=100):
        self.width = width
        self.height = height
        self.map = [0] * (width*height)

    def record(self, co_ord, tile):
        self.map[self._map_offset(co_ord)] = int(tile)

    def at(self, co_ord):
        """Returns the tile at a specific co-ordinate"""
        return Tile(self.map[self._map_offset(co_ord)])

    def _map_offset(self, co_ord):
        """Gets the list offset of a co-ordinate within the map list"""
        return int(self.width * co_ord.y + co_ord.x)

class Navigator:
    def __init__(self, width=100, height=100):
        self.map = Map(width, height)
        self.current = Coord(width/2, height/2)
        self.previous = None
        self.printer = ImagePrinter(width, height, {
            int(Tile.WALL): "░",
            int(Tile.OXY_SENSOR): "O",
            int(Tile.FLOOR): "."
        })
        self.steps = 0

        self.map.record(self.current, Tile.FLOOR)

    def read(self):
        if self.map.at(self.current.north()) == Tile.UNVISITED:
            self.previous = self.current
            self.current = self.current.north()
            return 1
        if self.map.at(self.current.south()) == Tile.UNVISITED:
            self.previous = self.current
            self.current = self.current.south()
            return 2
        if self.map.at(self.current.west()) == Tile.UNVISITED:
            self.previous = self.current
            self.current = self.current.west()
            return 3
        if self.map.at(self.current.east()) == Tile.UNVISITED:
            self.previous = self.current
            self.current = self.current.east()
            return 4
        print("No where to go?")

    def write(self, input):
        if input == 0:
            print("Move hit a wall")
            self.map.record(self.current, Tile.WALL)
            self.current = self.previous
            self.previous = None
        elif input == 1:
            self.map.record(self.current, Tile.FLOOR)
            self.steps += 1
            print("Move success")
        elif input == 2:
            print("Found Oxygen Sensor in {} steps".format(self.steps))
            self.steps += 1
            self.map.record(self.current, Tile.OXY_SENSOR)
        self.printer.print(self.map.map)
