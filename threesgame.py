"""
Xander Madsen - March 2018

A clone of the iOS game Threes, to be used in training a neural network.
"""

from random import randint, seed


def can_combine(curr_tile, next_tile):
    if curr_tile.value == 0 or next_tile.value == 0:
        return True
    elif (curr_tile.value == 1 and next_tile.value == 2) or \
            (curr_tile.value == 2 and next_tile.value == 1):
        return True
    elif curr_tile.value == next_tile.value:
        return True
    else:
        return False


def coord_is_wall(dir, row, col):
    # Determine if tile position is a wall if swiping in direction dir
    if dir == "up":
        if row == 0:
            return True
        else:
            return False
    elif dir == "down":
        if row == 3:
            return True
        else:
            return False
    elif dir == "left":
        if col == 0:
            return True
        else:
            return False
    elif dir == "right":
        if col == 3:
            return True
        else:
            return False


class Tile():
    def __init__(self, value=0):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.value == other.value

    # up, down, left, right - initialize to None.
    # True/False once board is initiliazed.
    combinable = [None, None, None, None]


class Board():

    tiles = [[Tile(), Tile(), Tile(), Tile()],
             [Tile(), Tile(), Tile(), Tile()],
             [Tile(), Tile(), Tile(), Tile()],
             [Tile(), Tile(), Tile(), Tile()]]

    def __str__(self):
        """ Represent a board as the values of the tiles
        # in 4 rows of 4 separated by spaces. """
        output = ''
        for row in self.tiles:
            output += ('  '.join([str(tile.value) for tile in row])) + '\n'
        return output

    def read_board(self):
        """ A list of lists containing all the tiles on the board,
        along with a list of the next possible tiles.
        """
        output = {}
        output["tiles"] = [[el.value for el in row]
                           for row in self.tiles]
        output["next"] = [1, 2, 3]
        return output

    def board_init(self, test=False):
        """ Create a board with 3x each of 
        1 tiles, 2 tiles, and 3 tiles, with the rest 0 (empty) tiles.
        """
        if test:
            self.tiles = [[Tile(0), Tile(0), Tile(0), Tile(3)],
                          [Tile(1), Tile(0), Tile(3), Tile(2)],
                          [Tile(3), Tile(2), Tile(1), Tile(0)],
                          [Tile(2), Tile(1), Tile(0), Tile(0)]]
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

    def swipe(self, dir):

        if dir == "up":
            rowdelta = -1
            coldelta = 0
        elif dir == "down":
            rowdelta = 1
            coldelta = 0
        elif dir == "left":
            rowdelta = 0
            coldelta = -1
        elif dir == "right":
            rowdelta = 0
            coldelta = 1

        if dir == "up":
            for i, row in enumerate(self.tiles):
                for j, tile in enumerate(row):
                    # check if current tile is the upper wall
                    if coord_is_wall(dir, i, j):
                        continue
                    # check if the tile above can be combined
                    # with the current tile
                    if can_combine(tile, self.tiles[i-1][j]):
                        # set the above tile to the sum of its current value
                        # and the current tile's value, then set the current
                        # tile to 0.
                        self.tiles[i-1][j] = Tile(tile.value +
                                                  self.tiles[i-1][j].value)
                        self.tiles[i][j] = Tile()
        elif dir == "down":
            for i, row in enumerate(reversed(self.tiles)):
                for j, tile in enumerate(row):
                    # check if current tile is the upper wall
                    if coord_is_wall(dir, 3-i, j):
                        continue
                    # check if the tile below can be combined
                    # with the current tile
                    if can_combine(tile, self.tiles[3-i+1][j]):
                        # set the above tile to the sum of its current value
                        # and the current tile's value, then set the current
                        # tile to 0.
                        self.tiles[3-i+1][j] = Tile(tile.value +
                                                    self.tiles[3-i+1][j].value)
                        self.tiles[3-i][j] = Tile()
        elif dir == "left":
            for i, row in enumerate(self.tiles):
                for j, tile in enumerate(row):
                    # check if current tile is the upper wall
                    if coord_is_wall(dir, i, j):
                        continue
                    # check if the tile below can be combined
                    # with the current tile
                    if can_combine(tile, self.tiles[i][j-1]):
                        # set the above tile to the sum of its current value
                        # and the current tile's value, then set the current
                        # tile to 0.
                        self.tiles[i][j-1] = Tile(tile.value +
                                                  self.tiles[i][j-1].value)
                        self.tiles[i][j] = Tile()
