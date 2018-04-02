import unittest
from threesgame import Board, Tile, can_combine


def boards_match(board, expectedboard):
    for index, board_row in enumerate(board.tiles):
        if [tile.value for tile in board_row] != [
                tile.value for tile in expectedboard.tiles[index]]:
            return False
    return True


class BoardAndTileTest(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_board_read_board_method_returns_4_by_4_list_and_array_of_possible_tiles(self):
        # I go to make a board.
        boardoutput = self.board.read_board()

        # It contains four arrays of length four,
        tiles = boardoutput["tiles"]
        for row in tiles:
            self.assertEqual(len(row), 4)

        # and one array of length 1 to 3 to indicate the next possible tile(s)
        next_tiles = boardoutput["next"]
        self.assertIn(len(next_tiles), [1, 2, 3])

    def test_board_read_board_method_returns_a_4_by_4_list_of_integers_and_array_of_integers(self):
        # The board contains four arrays, where each element is a Tile object
        # I go to make a board.
        boardoutput = self.board.read_board()
        tiles = boardoutput["tiles"]

        # It contains four arrays with four Tiles each,
        for row in tiles:
            for element in row:
                self.assertIsInstance(element, int)

        next_tiles = boardoutput["next"]

        # and one array of integers denoting the possible next tiles.
        for number in next_tiles:
            self.assertIsInstance(number, int)

    def test_initialized_board_has_three_of_each_starting_tile(self):
        # I start the game and initialize the board.
        self.board.board_init()

        boardoutput = self.board.read_board()
        ones = twos = threes = zeros = 0
        for row in boardoutput["tiles"]:
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
        self.test_tile = Tile()
        self.assertEqual(self.test_tile.value, 0)

    def test_create_tile_with_nondefault_value(self):
        # I create a tile object with value 3 instead of the default 0
        self.test_tile = Tile(3)
        self.assertEqual(self.test_tile.value, 3)

    def test_tile_combinations_work(self):
        # Given different combos of tiles, they combine properly.

        self.tile1 = Tile(0)
        self.tile2 = Tile(0)
        # Two empty tiles can combine.
        self.assertTrue(can_combine(self.tile1, self.tile2))

        self.tile1 = Tile(1)
        self.tile2 = Tile(2)
        # 1s and 2s can combine.
        self.assertTrue(can_combine(self.tile1, self.tile2))

        self.tile1 = Tile(2)
        self.tile2 = Tile(1)
        # 1s and 2s can combine, regardless of order.
        self.assertTrue(can_combine(self.tile1, self.tile2))

        self.tile1 = Tile(3)
        self.tile2 = Tile(3)
        # Twins can combine.
        self.assertTrue(can_combine(self.tile1, self.tile2))

        self.tile1 = Tile(1)
        self.tile2 = Tile(3)
        # 1 and 3 cannot combine.
        self.assertFalse(can_combine(self.tile1, self.tile2))

    def test_swipe_up_one_tile_not_on_edge(self):
        # With the board initialized, I press up on the board, and the tiles
        # all move correctly.

        # Start with just one 1 tile in the middle, see if it moves properly.
        self.board.tiles = [[Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(1), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)]]

        self.expectedboard = Board()
        self.expectedboard.tiles = [[Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(1), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)]]

        self.board.swipe("up", add_new_tile=False)

        # Check if the 1 tile moved up properly.
        self.assertTrue(boards_match(self.board, self.expectedboard))

    def test_swipe_up_one_tile_on_edge(self):
        # With the board initialized, I swipe up on the board, and the tiles
        # all move correctly.

        # Start with just one 1 tile on the top wall, see if it moves properly.
        self.board.tiles = [[Tile(0), Tile(1), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)]]

        self.expectedboard = Board()
        self.expectedboard.tiles = [[Tile(0), Tile(1), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)]]

        self.board.swipe("up", add_new_tile=False)
        # Check if the 1 tile moved up properly.
        # for index, board_row in enumerate(self.board.tiles):
        #     self.assertEqual([tile.value for tile in board_row], [
        #                      tile.value for tile in self.expectedboard.tiles[index]])

        self.assertTrue(boards_match(self.board, self.expectedboard))

    def test_swipe_up_initialized_board(self):
        self.board.board_init(test=True)
        self.expectedboard = Board()
        self.expectedboard.tiles = [[Tile(1), Tile(0), Tile(2), Tile(6)],
                                    [Tile(3), Tile(2), Tile(1), Tile(0)],
                                    [Tile(2), Tile(1), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)]]
        self.board.swipe("up", add_new_tile=False)
        self.assertTrue(boards_match(self.board, self.expectedboard))

    def test_swipe_down_one_tile_not_on_edge(self):
        # With the board initialized, I press up on the board, and the tiles
        # all move correctly.

        # Start with just one 1 tile in the middle, see if it moves properly.
        self.board.tiles = [[Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(1), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)]]

        self.expectedboard = Board()
        self.expectedboard.tiles = [[Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(1), Tile(0), Tile(0)]]

        self.board.swipe("down", add_new_tile=False)
        # Check if the 1 tile moved up properly.
        self.assertTrue(boards_match(self.board, self.expectedboard))

    def test_swipe_down_one_tile_on_edge(self):
        # With the board initialized, I swipe up on the board, and the tiles
        # all move correctly.

        # Start with just one 1 tile on the top wall, see if it moves properly.
        self.board.tiles = [[Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(1), Tile(0), Tile(0)]]

        self.expectedboard = Board()
        self.expectedboard.tiles = [[Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(1), Tile(0), Tile(0)]]

        self.board.swipe("down", add_new_tile=False)

        # Check if the 1 tile moved up properly.
        self.assertTrue(boards_match(self.board, self.expectedboard))

    def test_swipe_down_initialized_board(self):
        self.board.board_init(test=True)
        self.expectedboard = Board()
        self.expectedboard.tiles = [[Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(1), Tile(0), Tile(0), Tile(3)],
                                    [Tile(3), Tile(0), Tile(2), Tile(3)],
                                    [Tile(2), Tile(3), Tile(1), Tile(0)]]

        self.board.swipe("down", add_new_tile=False)

        self.assertTrue(boards_match(self.board, self.expectedboard))

    def test_swipe_left_one_tile_not_on_edge(self):
        # With the board initialized, I press up on the board, and the tiles
        # all move correctly.

        # Start with just one 1 tile in the middle, see if it moves properly.
        self.board.tiles = [[Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(1), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)]]

        self.expectedboard = Board()
        self.expectedboard.tiles = [[Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(1), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)]]
        self.board.swipe("left", add_new_tile=False)
        # Check if the 1 tile moved up properly.
        self.assertTrue(boards_match(self.board, self.expectedboard))

    def test_swipe_left_one_tile_on_edge(self):
        # With the board initialized, I swipe up on the board, and the tiles
        # all move correctly.

        # Start with just one 1 tile on the top wall, see if it moves properly.
        self.board.tiles = [[Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(1), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)]]

        self.expectedboard = Board()
        self.expectedboard.tiles = [[Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(1), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)]]
        self.board.swipe("left", add_new_tile=False)
        # Check if the 1 tile moved up properly.
        self.assertTrue(boards_match(self.board, self.expectedboard))

    def test_swipe_left_initialized_board(self):
        self.board.board_init(test=True)
        self.expectedboard = Board()
        self.expectedboard.tiles = [[Tile(0), Tile(0), Tile(3), Tile(0)],
                                    [Tile(1), Tile(2), Tile(3), Tile(0)],
                                    [Tile(3), Tile(3), Tile(0), Tile(0)],
                                    [Tile(3), Tile(0), Tile(0), Tile(0)]]
        self.board.swipe("left", add_new_tile=False)
        self.assertTrue(boards_match(self.board, self.expectedboard))

    def test_swipe_right_one_tile_not_on_edge(self):
        # With the board initialized, I press up on the board, and the tiles
        # all move correctly.

        # Start with just one 1 tile in the middle, see if it moves properly.
        self.board.tiles = [[Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(1), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)]]

        self.expectedboard = Board()
        self.expectedboard.tiles = [[Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(1), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)]]
        self.board.swipe("right", add_new_tile=False)
        # Check if the 1 tile moved up properly.
        self.assertTrue(boards_match(self.board, self.expectedboard))

    def test_swipe_right_one_tile_on_edge(self):
        # With the board initialized, I swipe up on the board, and the tiles
        # all move correctly.

        # Start with just one 1 tile on the top wall, see if it moves properly.
        self.board.tiles = [[Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(1)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)]]

        self.expectedboard = Board()
        self.expectedboard.tiles = [[Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)],
                                    [Tile(0), Tile(0), Tile(0), Tile(1)],
                                    [Tile(0), Tile(0), Tile(0), Tile(0)]]
        self.board.swipe("right", add_new_tile=False)
        # Check if the 1 tile moved up properly.
        self.assertTrue(boards_match(self.board, self.expectedboard))

    def test_swipe_right_initialized_board(self):
        self.board.board_init(test=True)
        self.expectedboard = Board()
        self.expectedboard.tiles = [[Tile(0), Tile(0), Tile(0), Tile(3)],
                                    [Tile(0), Tile(1), Tile(2), Tile(3)],
                                    [Tile(0), Tile(3), Tile(2), Tile(1)],
                                    [Tile(0), Tile(2), Tile(1), Tile(0)]]
        self.board.swipe("right", add_new_tile=False)
        self.assertTrue(boards_match(self.board, self.expectedboard))

    def test_board_knows_max_tile_value_after_swipe(self):
        # I swipe a direction on the board, and the board's
        # max_tile_value is updated.
        self.board.board_init(test=True)

        # this should be 3
        oldmaxvalue = self.board.max_tile_value
        self.assertEqual(oldmaxvalue, 3)

        self.board.swipe("up")
        newmaxvalue = self.board.max_tile_value
        self.assertEqual(newmaxvalue, 6)

    def test_swipe_down_adds_new_tile(self):
        # With the board initialized, I swipe on the board, and a new tile
        # is added properly at the opposite edge

        # Start with all zeroes.
        self.board.tiles = [[Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(1), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)],
                            [Tile(0), Tile(0), Tile(0), Tile(0)]]
        self.board.swipe("down")
        non_zero = []
        for tile in self.board.tiles[0]:
            if tile.value != 0:
                non_zero.append(tile.value)
        # Check if a new tile has been generated.
        self.assertTrue(len(non_zero) > 0)

    def test_swipe_down_with_illegal_move_doesnt_add_new_tile(self):
            # Swiping down in an illegal move, a new tile
            # is NOT added at the opposite edge

            # Start with all zeroes.
        self.board.tiles = [[Tile(0), Tile(0), Tile(0), Tile(99)],
                            [Tile(0), Tile(0), Tile(0), Tile(98)],
                            [Tile(0), Tile(0), Tile(0), Tile(97)],
                            [Tile(0), Tile(0), Tile(0), Tile(96)]]
        self.board.swipe("down")
        non_zero = []
        for tile in self.board.tiles[0]:
            if tile.value != 0:
                non_zero.append(tile.value)
        # Check if a new tile has been generated.
        self.assertTrue(len(non_zero) == 1 and non_zero[0] == 99)

    def test_swipe_down_adds_new_tile_in_correct_spot(self):
        # With the board initialized, I swipe on the board, and a new tile
        # is initilalized properly at the opposite edge in the only open slot

        # Start with all zeroes.
        self.board.tiles = [[Tile(0), Tile(1), Tile(1), Tile(1)],
                            [Tile(2), Tile(1), Tile(1), Tile(1)],
                            [Tile(1), Tile(1), Tile(1), Tile(1)],
                            [Tile(1), Tile(1), Tile(1), Tile(1)]]
        self.board.swipe("down")
        non_zero = []
        for tile in self.board.tiles[0]:
            if tile.value != 0:
                non_zero.append(tile.value)
        # Check if a new tile has been generated.
        self.assertTrue(len(non_zero) == 4)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
