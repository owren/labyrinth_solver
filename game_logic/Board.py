import numpy as np
import random

wall = '#'

class Board:

    def __init__(self, horizontal, vertical):
        # creates the board - times two to make space for boarder inside, and pluss two boarder outside
        self.board = np.full((horizontal * 2 + 2, vertical * 2 + 2), ' ')
        self.set_boarder()
        self.set_exit_point()

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

    def decide_orientation(self, width, height):
        if width < height:
            return 'horizontal'
        elif width > height:
            return 'vertical'
        else:
            return 'horizontal' if random.randint(0, 1) == 0 else 'vertical'

    def display_board(self):
        for row in self.board:
            string = ''
            for cell in row:
                string += str(cell) + str(' ')
            print(string)

    pass
