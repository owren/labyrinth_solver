################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

import numpy as np
import random

from functions import *

wall = '#'
N, S, E, W = 1, 2, 3, 4
VER, HOR = 0, 1

class Board:


    def __init__(self, horizontal, vertical):
        self.board = self.set_board(horizontal, vertical)
        self.set_boarder()
        self.set_exit_point()
        self.recursive_divide(0, self.board.shape[1] - 1, 0, self.board.shape[0] - 1)

    def set_board(self, horizontal, vertical):
        """
        Creates the board
        Times two to make space for boarder inside
        Minus one to get a odd number
        Plus two for boarder outside
        """
        return np.full((vertical * 2 - 1 + 2, horizontal * 2 - 1 + 2), ' ')

    def set_boarder(self):
        """
        Sets boarder around the board
        """
        for col in range(self.board.shape[0]):
            self.board[col][0] = wall
            self.board[col][self.board.shape[1] - 1] = wall
        for row in range(self.board.shape[1]):
            self.board[0][row] = wall
            self.board[self.board.shape[0] - 1][row] = wall

    def set_exit_point(self):
        direction = random.randint(1, 4)
        y_coordinate = random_odd_number(1, self.board.shape[0] - 2)
        x_coordinate = random_odd_number(1, self.board.shape[1] - 2)
        if direction == N:
            self.board[y_coordinate][0] = ' '
        elif direction == S:
            self.board[y_coordinate][self.board.shape[1] - 1] = ' '
        elif direction == W:
            self.board[0][x_coordinate] = ' '
        elif direction == E:
            self.board[self.board.shape[0] - 1][x_coordinate] = ' '

    def set_line(self, min, max, orientation, coordinate):
        opening = random_odd_number(min, max)
        print_orientation(orientation)
        # vertical
        for cell in range(min, max):
            if orientation == VER:
                self.board[cell][coordinate] = wall
            else:
                self.board[coordinate][cell] = wall


    def recursive_divide(self, x0, x1, y0, y1):
        t = .5
        print(x0, x1, y0, y1)
        orientation = decide_orientation(x1 - x0, y1 - y0)
        print_orientation(orientation)
        if x1 - x0 <= 3 or y1 - y0 <= 3:
            print('hei')
            return
            print('heh')
        if orientation == VER:
            if x1 - x0 <= 3:
                return
            line = random_even_number(y0, y1)
            print('set line ', y0, y1)
            self.set_line(y0, y1, orientation, line)
            #clear_screen()
            wait(t)
            self.display_board()
            print(x0, line, x1)
            self.recursive_divide(x0 + 1, line - 1, y0 + 1, y1 - 1)
            self.recursive_divide(line + 1, x1 - 1, y0 + 1, y1 - 1)

        else:
            if y1 - y0 <= 3:
                return
            line = random_even_number(x0, x1)
            self.set_line(x0, x1, orientation, line)
            #clear_screen()
            wait(t)
            self.display_board()
            print(y0, line, y1)
            self.recursive_divide(x0 + 1, x1 - 1, y0 + 1, line - 1)
            self.recursive_divide(x0 + 1, x1 - 1, line + 1, y1 - 1)


    def recursive_divide_fail(self, x0, x1, y0, y1):
        """
        ----------
        Parameters:
            x0: int - start position for x direction
            x1: int - end position for x direction
            y0: int - start position for y direction
            y1: int - end position for y direction
        """
        t = .5
        print(x0, x1, y0, y1)
        orientation = decide_orientation(x1 - x0, y1 - y0)
        print(orientation)
        self.highlight_usage(x0, x1, y0, y1)
        if orientation == HOR:
            if y1 - y0 <= 2:
                print('sup')
                return
                print('ups')
            print(orientation)
            line = random_even_number(y0 + 1, y1 - 1)
            self.set_line(y0, y1, orientation, line)
            clear_screen()
            self.display_board()
            wait(t)
            self.recursive_divide(x0, line, y0, y1)
            self.recursive_divide(line, x1, y0, y1)
        elif orientation == VER:
            if x1 - x0 <= 2:
                print('sup2')
                return
                print('ups2')
            print(orientation)
            line = random_even_number(x0 + 1, x1 - 1)
            self.set_line(x0, x1, orientation, line)
            clear_screen()
            self.display_board()
            wait(t)
            self.recursive_divide(x0, x1, y0, line)
            self.recursive_divide(x0, x1, line, y1)
    
    def highlight_usage(self, x0, x1, y0, y1):
        for x in range((self.board.shape[1])):
            for y in range((self.board.shape[0])):
                if x in range(x0, x1) and y in range(y0, y1):
                    if self.board[y][x] == ' ':
                        self.board[y][x] = '-' 
        self.display_board()
        wait(2)
        for x in range((self.board.shape[1])):
            for y in range((self.board.shape[0])):
                if x in range(x0, x1) and y in range(y0, y1):
                    if self.board[y][x] == '-':
                        self.board[y][x] = ' '
        self.display_board()
        wait(2)

    def display_board(self):

        print(self.board.shape)

        for row in self.board:
            string = ''
            for cell in row:
                string += str(cell) + str(' ')
            print(string)
