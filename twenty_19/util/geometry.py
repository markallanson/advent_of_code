class Coord:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def north(self):
        """Gets the co-ordinate one step north from the current co-ordinate"""
        return Coord(self.x, self.y - 1)

    def south(self):
        """Gets the co-ordinate one step south from the current co-ordinate"""
        return Coord(self.x, self.y + 1)

    def east(self):
        """Gets the co-ordinate one step east from the current co-ordinate"""
        return Coord(self.x + 1, self.y)

    def west(self):
        """Gets the co-ordinate one step west from the current co-ordinate"""
        return Coord(self.x - 1, self.y)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{},{}".format(self.x, self.y)