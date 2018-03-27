"""
Xander Madsen - March 2018

A clone of the iOS game Threes, to be used in training a neural network.
"""


class Tile():
    value = 0

    def __str__(self):
        return(str(self.value))


class Board():

    tiles = [[Tile(), Tile(), Tile(), Tile()],
             [Tile(), Tile(), Tile(), Tile()],
             [Tile(), Tile(), Tile(), Tile()],
             [Tile(), Tile(), Tile(), Tile()]]

    def read_board(self):
        output = {}
        output["tiles"] = self.tiles
        output["next_tiles"] = [1, 2, 3]
        return(output)
