import unittest
import threesgame


class BoardAndTileTest(unittest.TestCase):

    def setUp(self):
        self.board = threesgame.Board()

    def test_board_read_board_method_returns_4_by_4_list_and_array_of_possible_tiles(self):
        # I go to make a board.
        boardoutput = self.board.read_board()

        # It contains four arrays of length four,
        tiles = boardoutput["tiles_layout"]
        for row in tiles:
            self.assertEqual(len(row), 4)

        # and one array of length 1 to 3 to indicate the next possible tile(s)
        next_tiles = boardoutput["next_tiles"]
        self.assertIn(len(next_tiles), [1, 2, 3])

    def test_board_read_board_method_returns_a_4_by_4_list_of_integers_and_array_of_integers(self):
        # The board contains four arrays, where each element is a Tile object
        # I go to make a board.
        boardoutput = self.board.read_board()
        tiles = boardoutput["tiles_layout"]

        # It contains four arrays with four Tiles each,
        for row in tiles:
            for element in row:
                self.assertIsInstance(element, int)

        next_tiles = boardoutput["next_tiles"]

        # and one array of integers denoting the possible next tiles.
        for number in next_tiles:
            self.assertIsInstance(number, int)

    def test_initialized_board_has_three_of_each_starting_tile(self):
        # I start the game and initialize the board.
        self.board.board_init()

        boardoutput = self.board.read_board()
        ones = twos = threes = zeros = 0
        for row in boardoutput["tiles_layout"]:
            ones += row.count(1)
            twos += row.count(2)
            threes += row.count(3)
            zeros += row.count(0)

        # There are three 1s, three 2s, and three 3s to start, and thus 7
        # zeros remaining.
        self.assertEqual(ones, 3)
        self.assertEqual(twos, 3)
        self.assertEqual(threes, 3)
        self.assertEqual(zeros, 7)

    def test_create_tile_with_default_value(self):
        # I create a tile object with default value of 0
        self.test_tile = threesgame.Tile()
        self.assertEqual(self.test_tile.value, 0)

    def test_create_tile_with_nondefault_value(self):
        # I create a tile object with value 3 instead of the default 0
        self.test_tile = threesgame.Tile(value=3)
        self.assertEqual(self.test_tile.value, 3)

    # def test_send_up_move(self):
    #     # With the board initialized, I press up on the board, and the tiles
    #     # all move correctly.
    #     self.board.board_init(test=True)
    #     boardoutput = self.board.read_board()
    #     print(self.board)
    #     # print(boardoutput["tiles_layout"])

    #     self.expectedboard = threesgame.Board()

    #     # set all values for
    #     self.expectedboard.tiles[0][0].value = 0
    #     self.expectedboard.tiles[0][0].value = 0
    #     self.expectedboard.tiles[0][0].value = 0
    #     self.expectedboard.tiles[0][0].value = 0
    #     self.expectedboard.tiles[0][0].value = 0
    #     self.expectedboard.tiles[0][0].value = 0
    #     self.expectedboard.tiles[0][0].value = 0
    #     self.expectedboard.tiles[0][0].value = 0
    #     self.expectedboard.tiles[0][0].value = 0
    #     self.expectedboard.tiles[0][0].value = 0
    #     self.expectedboard.tiles[0][0].value = 0
    #     self.expectedboard.tiles[0][0].value = 0
    #     self.expectedboard.tiles[0][0].value = 0
    #     self.expectedboard.tiles[0][0].value = 0
    #     self.expectedboard.tiles[0][0].value = 0
    #     self.expectedboard.tiles[0][0].value = 0


if __name__ == '__main__':
    unittest.main(warnings='ignore')
