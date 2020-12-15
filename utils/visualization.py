# Candidate no: 249

import pygame

from values.Direction import Direction
from values.Constants import *


def draw_maze(board, cell_size, surface):
    """
    Draws the maze on a pygame object
    Uses draw_line as well
    :param board: np.ndarray - the matrix holding information about each cell
    :param cell_size: int - the size of the cell in vertical/horizontal size
    :param surface: pygame object - to be drawn on
    """
    surface.fill(BLACK)
    for y in range(board.shape[0]):
        for x in range(board.shape[1]):
            y_0 = y * cell_size + PADDING
            y_1 = (y + 1) * cell_size + PADDING
            x_0 = x * cell_size + PADDING
            x_1 = (x + 1) * cell_size + PADDING
            if board[y][x].get_wall(Direction.NORTH):
                draw_line(surface, x_0, y_0, x_1, y_0)
            if board[y][x].get_wall(Direction.EAST):
                draw_line(surface, x_1, y_0, x_1, y_1)
            if board[y][x].get_wall(Direction.SOUTH):
                draw_line(surface, x_0, y_1, x_1, y_1)
            if board[y][x].get_wall(Direction.WEST):
                draw_line(surface, x_0, y_0, x_0, y_1)
    pygame.display.update()


def draw_line(surface, x_0, y_0, x_1, y_1):
    """
    Draws a line from (x_0, y_0) to (x_1, y_1) on a pygame object surface
    Only being used by draw_maze method
    :param surface: pygame object - to be drawn on
    :param x_0: int - starting x position
    :param y_0: int - starting y position
    :param x_1: int - ending x position
    :param y_1: int - ending y position
    """
    pygame.draw.line(surface, GREY, (int(x_0), int(y_0)), (int(x_1), int(y_1)), 1)


def draw_rect(surface, colour, x_0, y_0, cell_size):
    """
    Draws a rectangle at given position with given colour on a pygame surface
    Only being used by MazeSolver.__visualize_rectangle in depth_first_search algorithm
    :param surface: pygame object - to be drawn on
    :param colour: tuple - the colour codes for given colour
    :param x_0: int - starting x position
    :param y_0: int - starting y position
    :param cell_size: int - the size of the a cell
    :return:
    """
    rectangle = pygame.Rect(x_0 + 1 + (cell_size/4), y_0 + 1 + (cell_size/4), cell_size/2, cell_size/2)
    pygame.draw.rect(surface, colour, rectangle)
