"""
Xander Madsen - March 2018

A clone of the iOS game Threes, to be used in training a neural network.
"""

from random import randint


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
        output["tiles_layout"] = [[el.value for el in row]
                                  for row in self.tiles]
        output["next_tiles"] = [1, 2, 3]
        return(output)

    def board_init(self):
        coords_to_change = []

        # Pick 9 tiles to be initialized with nonzero values
        while len(coords_to_change) < 9:
            coord = (randint(0, 3), randint(0, 3))
            if coord not in coords_to_change:
                coords_to_change.append(coord)

        initial_values = [1, 1, 1, 2, 2, 2, 3, 3, 3]

        for coord in coords_to_change:
            self.tiles[coord[0]][coord[1]].value = initial_values.pop(
                randint(0, len(initial_values) - 1))
