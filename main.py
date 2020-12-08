################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

from Board import Board
from Board_old import Board as Board_old
from robust_IO import input_int
from Constants import *
from Types import *


import pygame
import sys
from pygame.locals import KEYDOWN, K_q

"""
# set up pygame window
WIDTH = 500
HEIGHT = 600
FPS = 30

# Define colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
BLUE = (0, 0, 255)
YELLOW = (255 ,255 ,0)

# initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()
"""
def main():
    #vertical = int(input('Vertical size: '))
    #horizontal = int(input('Horizontal size: '))
    #y_coordinate = int(input('Y-coordinate for starting point: '))
    #x_coordinate = int(input('X-coordinate for starting point: '))
    v = 15
    h = 10
    from datetime import datetime
    #https://medium.com/better-programming/making-grids-in-python-7cf62c95f413
    height = SIZE
    width = int((height / v) * h)
    cell_size = height / v
    print(height, width)
    pygame.init()
    _VARS = {'surf': False}
    #_VARS['surf']
    surface = pygame.display.set_mode((width + (PADDING * 2), height + (PADDING * 2)))#((WIDTH + (PADDING * 2), HEIGHT + (PADDING * 2)))
    pygame.display.set_caption('Maze Solver')
    surface.fill(GREY)
    a = Board(vertical=v, horizontal=h, surface=surface, size=[height, width])
    draw_maze(a.board, cell_size, surface)
    while True:
        check_events()
        # drawLine()
        pygame.display.update()

    
    startTime = datetime.now()
    #a = Board(vertical=v, horizontal=h)
    print(datetime.now() - startTime)
    #a.display_board()


def check_events():
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
                draw_line(surface, y_0, x_0, y_1, x_0)
                # draw line
                pass
            if board[y][x].get_wall(Direction.EAST):
                #draw_line(surface, y_0, x_1, y_1, x_1)
                # draw line
                pass
            if board[y][x].get_wall(Direction.SOUTH):
                #draw_line(surface, y_1, x_0, y_1, x_1)
                # draw line
                pass
            if board[y][x].get_wall(Direction.WEST):
                #draw_line(surface, y_0, x_0, )
                # draw line
                pass


def draw_line(surface, y_0, x_0, y_1, x_1):
    pygame.draw.line(surface, BLACK, (y_0, x_0), (y_1, x_1), 1)


if __name__ == "__main__":
    main()
