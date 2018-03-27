import unittest
import threesgame


class BoardAndTileTest(unittest.TestCase):

    def setUp(self):
        self.board = threesgame.Board()

    def test_board_read_board_method_returns_4_by_4_list_and_array_of_possible_tiles(self):
        # I go to make a board.
        boardoutput = self.board.read_board()

        # It contains four arrays of length four,
        tiles = boardoutput["tiles"]
        for row in tiles:
            self.assertEqual(len(row), 4)

        # and one array of length 1 to 3 to indicate the next possible tile(s)
        next_tiles = boardoutput["next_tiles"]
        self.assertIn(len(next_tiles), [1, 2, 3])

    def test_board_tiles_returns_a_4_by_4_list_of_tile_objects(self):
        # The board contains four arrays, where each element is a Tile object
        # I go to make a board.
        boardoutput = self.board.read_board()
        tiles = boardoutput["tiles"]
        # It contains four arrays four Tiles each,
        for row in tiles:
            for element in row:
                self.assertIsInstance(element, threesgame.Tile)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
