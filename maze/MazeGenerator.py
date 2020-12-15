import random
import pygame

import visualization
from maze.Board import Board
from utils import functions
from values import Constants
from values.Direction import Direction
from values.Orientation import Orientation


class MazeGenerator:

    def __init__(self, board, cell_size, animation=False):
        self.__board = board
        self.__cell_size = cell_size
        self.__animation = animation

    def generate(self, height, width):
        pygame.init()
        self.__surface = pygame.display.set_mode((width + (Constants.PADDING * 2), height + (Constants.PADDING * 2)))
        pygame.display.set_caption('Maze Solver')
        self.__surface.fill(Constants.GREY)
        self.__set_boarder()
        self.__set_opening()
        if self.__animation:
            visualization.draw_maze(self.__board, self.__cell_size, self.__surface)
        self.__recursive_divide(y=[0, self.__board.shape[0]], x=[0, self.__board.shape[1]])

        return self.__surface

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
        orientation = functions.decide_orientation(x[1] - x[0], y[1] - y[0])
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
        if self.__animation:
            visualization.draw_maze(self.__board, self.__cell_size, self.__surface)
            functions.wait(0.05)
