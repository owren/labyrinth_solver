# Candidate no: 249

import numpy as np

from maze.Cell import Cell


class Board:
    """
    Class for holding the board
    Hols a np.ndarray object to create the maze on
    """

    def __init__(self, vertical, horizontal):
        self.__board = self.set_board(vertical, horizontal)

    @staticmethod
    def set_board(vertical, horizontal):
        """
        Sets the board to be used for generating a maze
        Creates the Cell object for each cell in the board
        :param vertical: int - the vertical size of the board
        :param horizontal: int - the horizontal size of the board
        :return: board - np.ndarray - the matrix that holds the information about each cell
        """
        board = np.ndarray((vertical, horizontal), dtype=np.object)
        for y in range(board.shape[0]):
            for x in range(board.shape[1]):
                board[y][x] = Cell(y, x)
        return board

    def get_board(self):
        """
        :return board - np.ndarray: the array for holding the board information
        """
        return self.__board
