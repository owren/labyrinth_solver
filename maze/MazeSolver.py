# Candidate no: 249

import time
import pygame

from values.Direction import Direction
from values.Path import Path
from values import Constants
from utils.visualization import draw_rect


class MazeSolver:
    """
    Class for solving the maze
    Includes a method for depth first search algorithm, to solve the maze,
        which uses methods for adding to stack and popping of stack, and visualization
    """

    def __init__(self, board, cell_size, animation):
        # Stack for keeping track of the cell coordinates in the path
        self.__stack = []
        # The board, holding information about the maze
        self.__board = board
        # Size of each cell vertical/horizontal
        self.__cell_size = cell_size
        # If the search should be animated or not
        self.__animation = animation
        # If the search is solved or not
        self.__solved = False

    def depth_first_search(self, y_coordinate, x_coordinate, surface):
        """
        Depth first search algorithm
        Starts in given position and searches for the opening
        First checks north cell of current cell, if no wall and not part of search and not the goal, then goes to next cell
        Adds each new cell to stack
        Checks in given directions: north, east, south, west
        If no where to go, go back to last and pop of stack
        :param y_coordinate: int - position of current cell in y direction
        :param x_coordinate: int - position of current cell in x direction
        :param surface: pygame object
        """
        current_y = y_coordinate
        current_x = x_coordinate
        while not self.__solved:
            # If not in stack, add to stack and visualize
            if [current_y, current_x] not in self.__stack:
                self.__add_to_stack_and_visualize(current_y, current_x, surface)
            # Gets current cell
            cell = self.__board[current_y, current_x]

            # If no wall in given direction and not solved
            if not cell.get_wall(Direction.NORTH) and not self.__solved:
                # If next one is the solution, then break and finished
                if current_y - 1 < 0:
                    self.__solved = True
                    break
                # If next cell is not part of the path - checks for next cell
                next_cell = self.__board[current_y - 1, current_x]
                if next_cell.get_used() == Path.NO:
                    current_y = current_y - 1
                    current_x = current_x
                    continue

            if not cell.get_wall(Direction.EAST) and not self.__solved:
                if current_x + 1 > self.__board.shape[1] - 1:
                    self.__solved = True
                    break
                next_cell = self.__board[current_y, current_x + 1]
                if next_cell.get_used() == Path.NO:
                    current_y = current_y
                    current_x = current_x + 1
                    continue

            if not cell.get_wall(Direction.SOUTH) and not self.__solved:
                if current_y + 1 > self.__board.shape[0] - 1:
                    self.__solved = True
                    break
                next_cell = self.__board[current_y + 1, current_x]
                if next_cell.get_used() == Path.NO:
                    current_y = current_y + 1
                    current_x = current_x
                    continue

            if not cell.get_wall(Direction.WEST) and not self.__solved:
                if current_x - 1 < 0:
                    self.__solved = True
                    break
                next_cell = self.__board[current_y, current_x - 1]
                if next_cell.get_used() == Path.NO:
                    current_y = current_y
                    current_x = current_x - 1
                    continue

            # If no there are no more possibilities for cell, pop of stack and visualize
            if not self.__solved:
                self.__pop_off_stack_and_visualize(current_y, current_x, surface)
                current_y = self.__stack[-1][0]
                current_x = self.__stack[-1][1]

    def __add_to_stack_and_visualize(self, y_coordinate, x_coordinate, surface):
        self.__stack.append([y_coordinate, x_coordinate])
        self.__visualize_rectangle(y_coordinate, x_coordinate, surface, Path.YES, Constants.GREEN)

    def __pop_off_stack_and_visualize(self, y_coordinate, x_coordinate, surface):
        self.__stack.pop()
        self.__visualize_rectangle(y_coordinate, x_coordinate, surface, Path.WAS, Constants.RED)

    def __visualize_rectangle(self, y_coordinate, x_coordinate, surface, path, colour):
        self.__board[y_coordinate, x_coordinate].set_used(path)
        y_0 = y_coordinate * self.__cell_size + Constants.PADDING
        x_0 = x_coordinate * self.__cell_size + Constants.PADDING
        draw_rect(surface, colour, x_0, y_0, self.__cell_size)
        if self.__animation:
            time.sleep(0.05)
            pygame.display.update()

    def get_stack(self):
        """
        Gets the stack of
        :return:
        """
        return self.__stack

    # not used ---------------------------------------------------------------------------------------------------------
    def recursive_backtracking(self, current_y, current_x, surface):
        self.__add_to_stack_and_visualize(current_y, current_x, surface)
        # gets the current cell
        cell = self.__board[current_y, current_x]

        if not cell.get_wall(Direction.NORTH) and not self.__solved:
            if current_y - 1 < 0:
                self.__solved = True
                return
                # found goal
            next_cell = self.__board[current_y - 1, current_x]
            if next_cell.get_used() == Path.NO:
                self.recursive_backtracking(current_y - 1, current_x, surface)

        if not cell.get_wall(Direction.EAST) and not self.__solved:
            if current_x + 1 > self.__board.shape[1] - 1:
                self.__solved = True
                return
            next_cell = self.__board[current_y, current_x + 1]
            if next_cell.get_used() == Path.NO:
                self.recursive_backtracking(current_y, current_x + 1, surface)

        if not cell.get_wall(Direction.SOUTH) and not self.__solved:
            if current_y + 1 > self.__board.shape[0] - 1:
                self.__solved = True
                return
            next_cell = self.__board[current_y + 1, current_x]
            if next_cell.get_used() == Path.NO:
                self.recursive_backtracking(current_y + 1, current_x, surface)

        if not cell.get_wall(Direction.WEST) and not self.__solved:
            if current_x - 1 < 0:
                self.__solved = True
                return
            next_cell = self.__board[current_y, current_x - 1]
            if next_cell.get_used() == Path.NO:
                self.recursive_backtracking(current_y, current_x - 1, surface)

        # set other color and pop off stack
        if not self.__solved:
            self.__pop_off_stack_and_visualize(current_y, current_x, surface)
        else:
            return
