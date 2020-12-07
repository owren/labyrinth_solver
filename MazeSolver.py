
from Types import *

class MazeSolver:
    # depth search
    def __init__(self, board, starting_position):
        """
        :param starting_position: list of y- and x-coordinate for starting position
        """
        self.stack = [starting_position]
        self.board = board
        current_position = starting_position
        while True:
            self.check_next(current_position[0], current_position[1])
            pass
            # solve

    def check_next(self, current_y, current_x):
        # gets the current cell
        cell = self.board[current_y, current_x]
        if not cell.get_wall(Direction.NORTH) and current_x > 0:
            pass
            #if board[] cell.get_used() == 0:
                # go to next
                #pass
        elif not cell.get_wall(Direction.EAST) and current_y < self.board.shape[0]:
            if cell.get_used() == 0:
                # go to next
                pass
        elif not cell.get_wall(Direction.SOUTH) and current_x < self.board.shape[1]:
            if cell.get_used() == 0:
                # go to next
                pass
        elif not cell.get_wall(Direction.WEST) and current_y > 0:
            if cell.get_used() == 0:
                # go to next
                pass


    def add_to_stack(self, pos):
        cell = self.board[pos]
