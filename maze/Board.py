################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

import numpy as np

from maze.Cell import Cell


class Board:

    def __init__(self, vertical, horizontal, height, width, cell_size):
        self.__board_height = height
        self.__board_width = width
        self.__cell_size = cell_size
        self.__board = self.__set_board(vertical, horizontal)

    def __set_board(self, vertical, horizontal):
        # defines the board
        self.__board = np.ndarray((vertical, horizontal), dtype=np.object)
        # creates the cells from Cell class
        for y in range(self.__board.shape[0]):
            for x in range(self.__board.shape[1]):
                self.__board[y][x] = Cell(y, x)
        return self.__board

    def get_board(self):
        return self.__board
