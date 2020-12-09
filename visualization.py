import pygame
import sys
from pygame.locals import KEYDOWN, K_q

from Types import *
from Constants import *
from Board import Board


def start_pygame(rows, columns, x_coordinate, y_coordinate):
    height = SIZE
    width = int((height / rows) * columns)
    cell_size = height / rows
    pygame.init()
    surface = pygame.display.set_mode(
        (width + (PADDING * 2), height + (PADDING * 2)))  # ((WIDTH + (PADDING * 2), HEIGHT + (PADDING * 2)))
    pygame.display.set_caption('Maze Solver')
    surface.fill(GREY)
    maze = Board(vertical=rows, horizontal=columns, size=[height, width])
    # a.display_board()
    draw_maze(maze.get_board(), cell_size, surface)
    pygame.display.update()
    run_loop()


def run_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_q:
                pygame.quit()
                sys.exit()


def draw_maze(board, cell_size, surface):
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


def draw_line(surface, x_0, y_0, x_1, y_1):
    pygame.draw.line(surface, BLACK, (int(x_0), int(y_0)), (int(x_1), int(y_1)), 1)
