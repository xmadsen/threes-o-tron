import unittest
import threesgame


class BoardAndTileTest(unittest.TestCase):

    def setUp(self):
        self.board = threesgame.Board()

    def test_board_returns_4_by_4_board_and_array_of_possible_next_tiles(self):
        # I go to make a board.
        boardoutput = self.board.read_board()

        # It contains four arrays of length four,
        self.assertEquals(len(boardoutput[0]), 4)
        self.assertEquals(len(boardoutput[1]), 4)
        self.assertEquals(len(boardoutput[2]), 4)
        self.assertEquals(len(boardoutput[3]), 4)

        # and one array of length 1 to 3 to indicate the next possible tile(s)
        self.assertIn(len(boardoutput[4]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main(warnings='ignore')
