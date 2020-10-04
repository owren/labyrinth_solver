################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

import numpy as np
import random

from functions import *
from Types import *

WALL = '#'
EMPTY = ' '

class Board:


    def __init__(self, horizontal, vertical):
        self.board = self.set_board(horizontal, vertical)
        self.set_boarder()
        #self.display_board()
        self.set_exit_point()
        #self.display_board()
        self.recursive_divide(0, self.board.shape[1] - 1, 0, self.board.shape[0] - 1)

    def set_board(self, horizontal, vertical):
        """
        Creates the board
        Times two to make space for boarder inside
        Minus one to get a odd number
        Plus two for boarder outside
        """
        return np.full((vertical * 2 - 1 + 2, horizontal * 2 - 1 + 2), EMPTY)

    def set_boarder(self):
        """
        Sets boarder around the board
        Sets wall on x = 0, y = 0, x max and y max
        """
        for col in range(self.board.shape[0]):
            self.board[col][0] = WALL
            self.board[col][self.board.shape[1] - 1] = WALL
        for row in range(self.board.shape[1]):
            self.board[0][row] = WALL
            self.board[self.board.shape[0] - 1][row] = WALL

    def set_exit_point(self):
        """
        Gets a random (NORTH, SOUTH, WEST, EAST) wall to set an opening
        Gets a random location on given wall to set an opening
        """
        direction = Direction(random.randint(0, 3))
        y_coordinate = random_odd_number(1, self.board.shape[0] - 2)
        x_coordinate = random_odd_number(1, self.board.shape[1] - 2)
        if direction == Direction.NORTH:
            self.board[y_coordinate][0] = EMPTY
        elif direction == Direction.SOUTH:
            self.board[y_coordinate][self.board.shape[1] - 1] = EMPTY
        elif direction == Direction.WEST:
            self.board[0][x_coordinate] = EMPTY
        elif direction == Direction.EAST:
            self.board[self.board.shape[0] - 1][x_coordinate] = EMPTY

    def set_line(self, min_wall, max_wall, orientation, coordinate):
        """
        Sets a line from min_wall to max_wall, in the orientation given, at the given coordinate
        ----------
        Parameters:
            self - Board object
            min_wall - int, the x or y coordinate for the starting point for the wall
            max_wall - int, the x or y coordinate for the ending point for the wall
            orientation - Enum, for what direction the wall should be, vertical or horizontal
            coordinate - int, the x or y coordinate (opposite of min and max) for where the wall should be
        """
        opening = random_odd_number(min_wall, max_wall)
        if orientation == Orientation.VERTICAL:
            for cell in range(min_wall, max_wall + 1):
                self.board[cell][coordinate] = WALL
            self.board[opening][coordinate] = EMPTY
        else:
            for cell in range(min_wall, max_wall + 1):
                self.board[coordinate][cell] = WALL
            self.board[coordinate][opening] = EMPTY

    def recursive_divide(self, x0, x1, y0, y1):
        """
        Recursive divide method
        Checks if there is enough space for a new line
        Gets the orientation for the new line to be set
            if wider than height, the line should be vertical and vice versa
        Gets the coordinate for the new line and sets this line
        Recursive divide on each side of the line
        ----------
        Parameters:
            self - Board object
            x0 - int, starting point in x-direction
            x1 - int, ending point in x-direction
            y0 - int, starting point in y-direction
            y1 - int, ending point in y-direction
        """
        if x1 - x0 <= 3 or y1 - y0 <= 3:
            return
        self.display_board()
        orientation = decide_orientation(x1 - x0, y1 - y0)
        if orientation == Orientation.VERTICAL:
            line = random_even_number(x0, x1)
            self.set_line(y0, y1, orientation, line)
            self.recursive_divide(x0, line, y0, y1)
            self.recursive_divide(line, x1, y0, y1)

        else:
            line = random_even_number(y0, y1)
            self.set_line(x0, x1, orientation, line)
            self.recursive_divide(x0, x1, y0, line)
            self.recursive_divide(x0, x1, line, y1)

    def display_board(self):
        input('')
        clear_screen()
        for row in self.board:
            string = ''
            for cell in row:
                string += str(cell) + str(' ')
            print(string)
