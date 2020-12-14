################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

import numpy as np

from maze.Cell import Cell
from values.Direction import Direction
from values.Orientation import Orientation
from functions import *
from Constants import *


class Board:

    def __init__(self, vertical, horizontal, size):
        self.__board_height = size[0]
        self.__board_width = size[1]
        self.__cell_size = self.__board_width / vertical
        self.__set_board(vertical, horizontal)
        self.__set_boarder()
        self.__set_opening()
        self.__recursive_divide(y=[0, self.__board.shape[0]], x=[0, self.__board.shape[1]])

    def __set_board(self, vertical, horizontal):
        # defines the board
        self.__board = np.ndarray((vertical, horizontal), dtype=np.object)
        # creates the cells from Cell class
        for y in range(self.__board.shape[0]):
            for x in range(self.__board.shape[1]):
                self.__board[y][x] = Cell(y, x)

    def __set_boarder(self):
        for y in range(self.__board.shape[0]):
            self.__board[y][0].update_wall(Direction.WEST, True)
            self.__board[y][self.__board.shape[1] - 1].update_wall(Direction.EAST, True)
        for x in range(self.__board.shape[1]):
            self.__board[0][x].update_wall(Direction.NORTH, True)
            self.__board[self.__board.shape[0] - 1][x].update_wall(Direction.SOUTH, True)

    def __set_opening(self):
        direction = Direction(random.randint(0, 3))
        y_coordinate = random.randint(0, self.__board.shape[0] - 1)
        x_coordinate = random.randint(0, self.__board.shape[1] - 1)
        if direction == Direction.NORTH:
            self.__board[0][x_coordinate].update_wall(direction, False)
        elif direction == Direction.SOUTH:
            self.__board[self.__board.shape[0] - 1][x_coordinate].update_wall(direction, False)
        elif direction == Direction.WEST:
            self.__board[y_coordinate][0].update_wall(direction, False)
        elif direction == Direction.EAST:
            self.__board[y_coordinate][self.__board.shape[1] - 1].update_wall(direction, False)

    def __recursive_divide(self, y, x):
        if y[1] - y[0] < 2 or x[1] - x[0] < 2:
            return
        orientation = decide_orientation(x[1] - x[0], y[1] - y[0])
        if orientation == Orientation.VERTICAL:
            line = random.randint(x[0], x[1] - 2)
            self.__set_line(y, orientation, line)
            self.__recursive_divide(y, [x[0], line + 1])
            self.__recursive_divide(y, [line + 1, x[1]])
        else:
            line = random.randint(y[0], y[1] - 2)
            self.__set_line(x, orientation, line)
            self.__recursive_divide([y[0], line + 1], x)
            self.__recursive_divide([line + 1, y[1]], x)

    def __set_line(self, size, orientation, coordinate):
        opening = random.randint(size[0], size[1] - 1)
        if orientation == Orientation.VERTICAL:
            for cell in range(size[0], size[1]):
                self.__board[cell][coordinate].update_wall(Direction.EAST, True)
                self.__board[cell][coordinate + 1].update_wall(Direction.WEST, True)
            self.__board[opening][coordinate].update_wall(Direction.EAST, False)
            self.__board[opening][coordinate + 1].update_wall(Direction.WEST, False)
        else:
            for cell in range(size[0], size[1]):
                self.__board[coordinate][cell].update_wall(Direction.SOUTH, True)
                self.__board[coordinate + 1][cell].update_wall(Direction.NORTH, True)
            self.__board[coordinate][opening].update_wall(Direction.SOUTH, False)
            self.__board[coordinate + 1][opening].update_wall(Direction.NORTH, False)

    def get_board(self):
        return self.__board

    def display_board(self):
        clear_screen()
        for y in range(self.__board.shape[0]):
            s1 = WALL + EMPTY
            s2 = ''
            for x in range(self.__board.shape[1]):
                # north
                if self.__board[y][x].get_wall(Direction.NORTH):
                    s1 += WALL + EMPTY
                else:
                    s1 += EMPTY + EMPTY
                s1 += WALL + EMPTY

                # west
                if self.__board[y][x].get_wall(Direction.WEST):
                    s2 += WALL + EMPTY
                else:
                    s2 += EMPTY + EMPTY
                s2 += EMPTY + EMPTY

                # east
                if x == self.__board.shape[1] - 1 and self.__board[y][x].get_wall(Direction.EAST):
                    s2 += WALL + EMPTY

            print(s1)
            print(s2)
        # south
        s3 = WALL + EMPTY
        for x in range(self.__board.shape[1]):
            if self.__board[self.__board.shape[0] - 1][x].get_wall(Direction.SOUTH):
                s3 += WALL + EMPTY
            else:
                s3 += EMPTY + EMPTY
            s3 += WALL + EMPTY
        print(s3)
