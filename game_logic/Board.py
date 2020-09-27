import numpy as np
import random


class Board:

    def __init__(self, horizontal, vertical):
        # creates the board - times two to make space for boarder inside, and pluss two boarder outside
        self.board = np.full((horizontal * 2 + 2, vertical * 2 + 2), ' ')
        self.set_boarder()
        self.set_exit_point()

    def set_boarder(self):
        # sets boarder around
        for y in range(self.board.shape[0]):
            for x in range(self.board.shape[1]):
                if y == 0 or y == self.board.shape[0] - 1:
                    self.board[y][x] = '#'
                if x == 0 or x == self.board.shape[1] - 1:
                    self.board[y][x] = '#'

    def set_exit_point(self):
        direction = random.randint(1, 4)
        y_coordinate = random.randint(1, self.board.shape[0] - 2)
        x_coordinate = random.randint(1, self.board.shape[1] - 2)
        if direction == 1:
            self.board[y_coordinate][0] = ' '
        elif direction == 2:
            self.board[y_coordinate][self.board.shape[1] - 1] = ' '
        elif direction == 3:
            self.board[0][x_coordinate] = ' '
        else:
            self.board[self.board.shape[0] - 1][x_coordinate] = ' '

    def display_board(self):
        for row in self.board:
            string = ''
            for cell in row:
                string += str(cell) + str(' ')
            print(string)

    pass
