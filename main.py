################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

from Board import Board
from robust_IO import input_int
import Constants
import visualization
from MazeSolver import MazeSolver

import pygame


def main():

    rows = input_int('Vertical size: ', 2, 10000)
    columns = input_int('Horizontal size: ', 2, 10000)
    y_coordinate = input_int('Y-coordinate starting point: ', 0, rows - 1)
    x_coordinate = input_int('X-coordinate starting point: ', 0, columns - 1)
    """
    rows = 50
    columns = 100
    x_coordinate = int(columns / 2)
    y_coordinate = int(rows / 2)
    """
    height = int(Constants.V_SIZE)
    width = int((height / rows) * columns)
    cell_size = int(height / rows)

    pygame.init()
    surface = pygame.display.set_mode((width + (Constants.PADDING * 2), height + (Constants.PADDING * 2)))
    pygame.display.set_caption('Maze Solver')
    surface.fill(Constants.GREY)

    text_surface = pygame.font.SysFont('calibri', 30).render('Generating maze, please wait...', False, Constants.BLACK)
    surface.blit(text_surface, (10, 10))
    pygame.display.update()
    maze = Board(vertical=rows, horizontal=columns, size=[height, width])

    visualization.draw_maze(maze.get_board(), cell_size, surface)

    solver = MazeSolver(maze.get_board(), cell_size, [y_coordinate, x_coordinate], surface)

    solver.depth_first_search(y_coordinate, x_coordinate, surface)

    stack = solver.get_stack()
    pygame.display.update()
    visualization.run_loop()


if __name__ == "__main__":
    main()
