"""
Xander Madsen - March 2018

A clone of the iOS game Threes, to be used in training a neural network.
"""


class Board():
    @staticmethod
    def read_board():
        return([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 3]])
