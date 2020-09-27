################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

import numpy as np
import random

from functions import *

wall = '#'

class Board:


    def __init__(self, horizontal, vertical):
        # creates the board - times two to make space for boarder inside, minus one to get a odd number and pluss two boarder outside
        self.board = np.full((horizontal * 2 - 1 + 2, vertical * 2 - 1 + 2), ' ')
        self.set_boarder()
        self.set_exit_point()
        self.recursive_devide(1, self.board.shape[1] - 2, 1, self.board.shape[0] - 2)


    def set_boarder(self):
        # sets boarder around
        for row in range(self.board.shape[0]):
            self.board[row][0] = wall
            self.board[row][self.board.shape[1] - 1] = wall
        for col in range(self.board.shape[0]):
            self.board[0][col] = wall
            self.board[self.board.shape[0] - 1][col] = wall


    def set_exit_point(self):
        direction = random.randint(1, 4)
        y_coordinate = random_odd_number(1, self.board.shape[0] - 2)
        x_coordinate = random_odd_number(1, self.board.shape[1] - 2)
        if direction == 1:
            self.board[y_coordinate][0] = ' '
        elif direction == 2:
            self.board[y_coordinate][self.board.shape[1] - 1] = ' '
        elif direction == 3:
            self.board[0][x_coordinate] = ' '
        else:
            self.board[self.board.shape[0] - 1][x_coordinate] = ' '


    def recursive_devide(self, x0, x1, y0, y1):
        """
        ----------
        Parameters:
            x0: int - start position for x direction
            x1: int - end position for x direction
            y0: int - start position for y direction
            y1: int - end position for y direction
        """
        print(x0,x1,y0,y1)
        orientation = decide_orientation(x1 - x0, y1 - y0)
        if orientation == 0:
            print(orientation)
            line = random_even_number(y0, y1)
            self.set_line(y0, y1, orientation, line)
        elif orientation == 1:
            print(orientation)
            line = random_even_number(x0, x1)
            self.set_line(x0, x1, orientation, line)


    def set_line(self, min, max, orientation, coordinate):
        opening = random_odd_number(min, max)
        # vertival
        if orientation == 0:
            for cell in range(min, max + 1):
                self.board[coordinate][cell] = '#'
            self.board[coordinate][opening] = ' '
        # horizontal
        else:
            for cell in range(min, max + 1):
                self.board[cell][coordinate] = '#'
            self.board[opening][coordinate] = ' '


    def display_board(self):
        for row in self.board:
            string = ''
            for cell in row:
                string += str(cell) + str(' ')
            print(string)
