"""
Xander Madsen - March 2018

A clone of the iOS game Threes, to be used in training a neural network.
"""

from random import randint, seed


class Tile():
    def __init__(self, value=0):
        self.value = value

    def __str__(self):
        return(str(self.value))


class Board():

    tiles = [[Tile(), Tile(), Tile(), Tile()],
             [Tile(), Tile(), Tile(), Tile()],
             [Tile(), Tile(), Tile(), Tile()],
             [Tile(), Tile(), Tile(), Tile()]]

    def __str__(self):
        output = ''
        for row in self.tiles:
            output += ('  '.join([str(tile.value) for tile in row])) + '\n'
        return(output)

    def read_board(self):
        output = {}
        output["tiles_layout"] = [[el.value for el in row]
                                  for row in self.tiles]
        output["next_tiles"] = [1, 2, 3]
        return(output)

    def board_init(self, test=False):
        if test:
            self.tiles[0][0].value = 0
            self.tiles[0][1].value = 0
            self.tiles[0][2].value = 0
            self.tiles[0][3].value = 3
            self.tiles[1][0].value = 1
            self.tiles[1][1].value = 0
            self.tiles[1][2].value = 3
            self.tiles[1][3].value = 2
            self.tiles[2][0].value = 3
            self.tiles[2][1].value = 2
            self.tiles[2][2].value = 1
            self.tiles[2][3].value = 0
            self.tiles[3][0].value = 2
            self.tiles[3][1].value = 1
            self.tiles[3][2].value = 0
            self.tiles[3][3].value = 0

        else:
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
