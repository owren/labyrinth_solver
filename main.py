################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

from Board import Board
from robust_IO import input_int
from Constants import *
import visualization
from MazeSolver import MazeSolver

import pygame


def main():
    #rows = int(input('Vertical size: '))
    #columns = int(input('Horizontal size: '))
    #y_coordinate = int(input('Y-coordinate for starting point: '))
    #x_coordinate = int(input('X-coordinate for starting point: '))
    x_coordinate = y_coordinate = 10
    rows = 15
    columns = 20

    height = V_SIZE
    width = int((height / rows) * columns)
    cell_size = height / rows

    pygame.init()
    surface = pygame.display.set_mode((width + (PADDING * 2), height + (PADDING * 2)))
    pygame.display.set_caption('Maze Solver')
    surface.fill(GREY)

    text_surface = pygame.font.SysFont('calibri', 30).render('Generating maze, please wait...', False, BLACK)
    surface.blit(text_surface, (10, 10))
    pygame.display.update()
    maze = Board(vertical=rows, horizontal=columns, size=[height, width])
    # a.display_board()

    #pygame.time.wait(2000)

    visualization.draw_maze(maze.get_board(), cell_size, surface)

    solver = MazeSolver(maze.get_board(), cell_size, [y_coordinate, x_coordinate], surface)
    stack = solver.recursive_backtracking(y_coordinate, x_coordinate, surface)

    visualization.run_loop()




if __name__ == "__main__":
    main()
