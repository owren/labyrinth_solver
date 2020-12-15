import pygame

from values.Direction import Direction
from values.Constants import *


def draw_maze(board, cell_size, surface):
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
    pygame.draw.line(surface, GREY, (int(x_0), int(y_0)), (int(x_1), int(y_1)), 1)


def draw_rect(surface, colour, x_0, y_0, x_1, y_1, cell_size):
    rectangle = pygame.Rect(x_0 + 1 + (cell_size/4), y_0 + 1 + (cell_size/4), cell_size/2, cell_size/2)
    pygame.draw.rect(surface, colour, rectangle)
